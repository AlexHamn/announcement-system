from django.core.management.base import BaseCommand
from homepage.models import Category, Subcategory

class Command(BaseCommand):
    help = 'Populates the database with categories and subcategories'

    def handle(self, *args, **options):
      # Create categories
      categories = [
          'Arrival and Departure Announcements',
          'Security and Safety Announcements',
      ]
      
      for category_name in categories:
          Category.objects.create(name=category_name)

        # Create subcategories
      subcategories = [
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Flight arrival',
          'template': 'Flight [flight number] from [origin] to [destination] is now arriving at Gate [gate number].',
          'template_ru': 'Рейс [flight number] из [origin] в [destination] прибывает на Гейт [gate number].',
          'template_kg': '[flight number] рейси [origin] - [destination], [gate number]-тарзда.',
        },
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Final Boarding Call',
          'template': 'Final boarding call for Flight [flight number] to [destination]. Proceed to Gate [gate number] immediately. Gate closes in [time remaining].',
          'template_ru': 'Заканчивается посадка на Рейс [flight number] в [destination]. Пройдите к Гейту [gate number] сейчас. Гейт закроется через [time remaining].',
          'template_kg': '[flight number] рейсине [destination] акыркы чакырык. Дароо [gate number]-тарзына өтүңүз. Тарз [time remaining] ичинде жабылат.',
        },
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Flight Delay',
          'template': 'Flight [flight number] to [destination] delayed due to [reason]. New departure time is [new time].',
          'template_ru': 'Рейс [flight number] в [destination] задерживается из-за [reason]. Новое время вылета - [new time].',
          'template_kg': '[flight number] рейси [destination] шаарына [reason] себептен кечиктирилди. Жаңы чыгуу убактысы [new time].',
        },
        {
          'category': 'Security and Safety Announcements',
          'name': 'Weapons Prohibited',
          'template': 'Firearms and weapons are strictly prohibited in the airport.',
          'template_ru': 'Огнестрельное оружие и другие виды оружия запрещены в аэропорту.',
          'template_kg': 'Аэропорт аймагында курал-жарактар жана башка куралдар катуу тыюу салынган.',
        },
      ]
      
      for subcategory_data in subcategories:
        category = Category.objects.get(name=subcategory_data['category'])
        Subcategory.objects.create(
            category=category,
            name=subcategory_data['name'],
            template=subcategory_data['template'],
            template_ru=subcategory_data['template_ru'],
            template_kg=subcategory_data['template_kg']
        )

      self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))