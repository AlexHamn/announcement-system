from django.shortcuts import render, redirect
from .models import Category, Subcategory

import re

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'homepage/index.html', {'categories': categories})

def subcategory(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategories = Subcategory.objects.filter(category=category)
    return render(request, 'homepage/subcategory.html', {'category': category, 'subcategories': subcategories})

def announcement(request, subcategory_id):
    subcategory = Subcategory.objects.get(id=subcategory_id)
    
    if request.method == 'POST':
        
        flight_number = request.POST.get('flight_number', '')
        origin = request.POST.get('origin', '')
        destination = request.POST.get('destination', '')
        
        if not re.match(r'^[A-Z]{2,3}\d{1,4}$', flight_number):
            # Handle invalid flight number format
            return render(request, 'homepage/announcement.html', {'subcategory': subcategory, 'error': 'Invalid flight number format'})
        if not re.match(r'^[A-Z]{3}$', origin):
            return render(request, 'homepage/announcement.html', {'subcategory': subcategory, 'error': 'Invalid origin format'})
        if not re.match(r'^[A-Z]{3}$', destination):
            return render(request, 'homepage/announcement.html', {'subcategory': subcategory, 'error': 'Invalid destination format'})
        
        message = subcategory.template
        message_ru = subcategory.template_ru
        message_kg = subcategory.template_kg
        
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken' and key != 'flight_number':
                placeholder = f'[{key}]'
                message = message.replace(placeholder, value)
                message_ru = message_ru.replace(placeholder, value)
                message_kg = message_kg.replace(placeholder, value)
        
        # Replace flight number placeholder separately
        message = message.replace('[flight number]', flight_number)
        message_ru = message_ru.replace('[flight number]', flight_number)
        message_kg = message_kg.replace('[flight number]', flight_number)
        
        message = message.replace('[origin]', origin)
        message_ru = message_ru.replace('[origin]', origin)
        message_kg = message_kg.replace('[origin]', origin)
        
        message = message.replace('[destination]', destination)
        message_ru = message_ru.replace('[destination]', destination)
        message_kg = message_kg.replace('[destination]', destination)
        
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
    
    # Remove 'flight number' from the variables list
    variables = [var for var in variables if var not in ['flight number', 'origin', 'destination']]
    
    context = {'subcategory': subcategory, 'variables': variables}
    return render(request, 'homepage/announcement.html', context)

def confirmation(request):
    message = request.session.get('message', '')
    message_ru = request.session.get('message_ru', '')
    message_kg = request.session.get('message_kg', '')
    
    #print("Message (from session):", message)
    #print("Message (RU) (from session):", message_ru)
    #print("Message (KG) (from session):", message_kg)
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Process the confirmed message (e.g., send it to the announcement system)
            pass
        return redirect('index')
    
    return render(request, 'homepage/confirmation.html', {'message': message, 'message_ru': message_ru, 'message_kg': message_kg})