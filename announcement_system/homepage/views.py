from django.shortcuts import render, redirect
from .models import Category, Subcategory

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
        message = subcategory.template
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                message = message.replace(f'[{key}]', value)
        request.session['message'] = message
        return redirect('confirmation')
    return render(request, 'homepage/announcement.html', {'subcategory': subcategory})

def confirmation(request):
    message = request.session.get('message', '')
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Process the confirmed message (e.g., send it to the announcement system)
            pass
        return redirect('index')
    return render(request, 'homepage/confirmation.html', {'message': message})