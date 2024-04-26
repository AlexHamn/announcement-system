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
          'template': '      flight [flight_number] from [origin] to [destination], is now arriving at gate [gate_number].',
          'template_ru': 'рейс [flight_number] из [origin] в [destination] прибывает на гейт [gate_number].',
          'template_kg': '[flight_number] рейси [origin] - [destination], [gate_number]-тарзда.',
        },
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Final Boarding Call',
          'template': 'final boarding call for flight [flight_number] to [destination]. proceed to gate [gate_number] immediately. gate closes in [time_remaining].',
          'template_ru': 'заканчивается посадка на рейс [flight_number] в [destination]. пройдите к гейту [gate_number] сейчас. гейт закроется через [time_remaining].',
          'template_kg': '[flight_number] рейсине [destination] акыркы чакырык. дароо [gate_number]-тарзына өтүңүз. тарз [time_remaining] ичинде жабылат.',
        },
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Flight Delay',
          'template': 'flight [flight_number] to [destination] delayed due to [reason]. new departure time is [new_time].',
          'template_ru': 'рейс [flight_number] в [destination] задерживается из-за [reason]. новое время вылета - [new_time].',
          'template_kg': '[flight_number] рейси [destination] шаарына [reason] себептен кечиктирилди. жаңы чыгуу убактысы [new_time].',
        },
        {
          'category': 'Security and Safety Announcements',
          'name': 'Weapons Prohibited',
          'template': 'firearms and weapons are strictly prohibited in the airport.',
          'template_ru': 'огнестрельное оружие и другие виды оружия запрещены в аэропорту.',
          'template_kg': 'аэропорт аймагында курал-жарактар жана башка куралдар катуу тыюу салынган.',
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