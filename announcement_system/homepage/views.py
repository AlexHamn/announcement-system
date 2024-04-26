# homepage/views.py

from django.shortcuts import render, redirect
from .models import Category, Subcategory
from .forms import AnnouncementForm
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
    placeholder_pattern = re.compile(r'\[.*?\]')
    variables = [var.strip('[]') for var in placeholder_pattern.findall(subcategory.template)]

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, variables=variables)
        if form.is_valid():
            message = subcategory.template
            message_ru = subcategory.template_ru
            message_kg = subcategory.template_kg

            for key, value in form.cleaned_data.items():
                placeholder = f'[{key}]'
                message = message.replace(placeholder, value)
                message_ru = message_ru.replace(placeholder, value)
                message_kg = message_kg.replace(placeholder, value)

            request.session['message'] = message
            request.session['message_ru'] = message_ru
            request.session['message_kg'] = message_kg
            request.session.modified = True

            return redirect('confirmation')
    else:
        form = AnnouncementForm(variables=variables)

    context = {'subcategory': subcategory, 'form': form}
    return render(request, 'homepage/announcement.html', context)

def confirmation(request):
    message = request.session.get('message', '')
    message_ru = request.session.get('message_ru', '')
    message_kg = request.session.get('message_kg', '')
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            return redirect('generate_audio')
        return redirect('index')
    
    return render(request, 'homepage/confirmation.html', {'message': message, 'message_ru': message_ru, 'message_kg': message_kg})
