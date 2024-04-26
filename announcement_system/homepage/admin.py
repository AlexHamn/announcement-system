import json
from django.contrib import admin
from django.http import HttpResponse
from .models import Category, Subcategory

def export_data(modeladmin, request, queryset):
    data = {
        'categories': [],
        'subcategories': [],
    }

    # Export Category data
    categories = Category.objects.all()
    for category in categories:
        data['categories'].append({
            'id': category.id,
            'name': category.name,
        })

    # Export Subcategory data
    subcategories = Subcategory.objects.all()
    for subcategory in subcategories:
        data['subcategories'].append({
            'id': subcategory.id,
            'category_id': subcategory.category_id,
            'name': subcategory.name,
            'template': subcategory.template,
            'template_ru': subcategory.template_ru,
            'template_kg': subcategory.template_kg,
        })

    # Create HTTP response with JSON data
    response = HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
    return response

export_data.short_description = 'Export selected data to JSON'

class CategoryAdmin(admin.ModelAdmin):
    actions = [export_data]

class SubcategoryAdmin(admin.ModelAdmin):
    actions = [export_data]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)