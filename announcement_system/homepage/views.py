from django.shortcuts import render, redirect
from .models import Category, Subcategory

import re

# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'homepage/index.html', context)

def subcategory(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategories = Subcategory.objects.filter(category=category)
    return render(request, 'homepage/subcategory.html', {'category': category, 'subcategories': subcategories})

def announcement(request, subcategory_id):
    subcategory = Subcategory.objects.get(id=subcategory_id)
    
    if request.method == 'POST':
        message = subcategory.template
        message_ru = subcategory.template_ru
        message_kg = subcategory.template_kg
        
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                placeholder = f'[{key}]'
                message = message.replace(placeholder, value)
                message_ru = message_ru.replace(placeholder, value)
                message_kg = message_kg.replace(placeholder, value)
        
        print("Message:", message)
        print("Message (RU):", message_ru)
        print("Message (KG):", message_kg)
        
        request.session['message'] = message
        request.session['message_ru'] = message_ru
        request.session['message_kg'] = message_kg
        request.session.modified = True
        
        return redirect('confirmation')
    
    placeholder_pattern = re.compile(r'\[.*?\]')
    variables = [var.strip('[]') for var in placeholder_pattern.findall(subcategory.template)]
    context = {'subcategory': subcategory, 'variables': variables}
    
    return render(request, 'homepage/announcement.html', context)

def confirmation(request):
    message = request.session.get('message', '')
    message_ru = request.session.get('message_ru', '')
    message_kg = request.session.get('message_kg', '')
    
    print("Message (from session):", message)
    print("Message (RU) (from session):", message_ru)
    print("Message (KG) (from session):", message_kg)
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Process the confirmed message (e.g., send it to the announcement system)
            pass
        return redirect('index')
    
    return render(request, 'homepage/confirmation.html', {'message': message, 'message_ru': message_ru, 'message_kg': message_kg})