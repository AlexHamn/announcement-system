from django.core.management.base import BaseCommand
from homepage.models import Category, Subcategory

class Command(BaseCommand):
    help = 'Populates the database with categories and subcategories'

    def handle(self, *args, **options):
      # Create categories
      categories = [
          'Arrival and Departure Announcements',
          'Security and Safety Announcements', 
          'Lost and Found Announcements',
          'Gate Change Announcements',
          'Baggage Claim Announcements',
          'General Announcements',
      ]

      for category_name in categories:
          Category.objects.create(name=category_name)

      # Create subcategories
      subcategories = [
          {
              'category': 'Arrival and Departure Announcements',
              'name': 'Flight arrival',
              'template': 'Attention, passengers. Flight [flight number] from [origin] to [destination] is now arriving at Gate [gate number]. Please proceed to the designated gate for boarding.',
          },
          {
              'category': 'Arrival and Departure Announcements',
              'name': 'Final Boarding Call',
              'template': 'This is a final boarding call for Flight [flight number] to [destination]. All remaining passengers, please proceed to Gate [gate number] immediately. The gate will close in [time remaining].',
          },
          {
              'category': 'Arrival and Departure Announcements',
              'name': 'Flight Delay',
              'template': 'Attention, passengers. Flight [flight number] to [destination] has been delayed due to [reason]. The new estimated departure time is [new time]. We apologize for the inconvenience.',
          },
          {
              'category': 'Arrival and Departure Announcements',
              'name': 'Flight Cancellation',
              'template': 'Ladies and gentlemen, we regret to inform you that Flight [flight number] to [destination] has been canceled due to [reason]. Please proceed to the airline\'s counter for rebooking or refund assistance.',
          },
          {
              'category': 'Security and Safety Announcements',
              'name': 'Security Reminder',
              'template': 'Attention, passengers. For your safety and security, please keep your belongings with you at all times and report any unattended bags or suspicious activity to the nearest security personnel.',
          },
          {
              'category': 'Security and Safety Announcements',
              'name': 'Weapons Prohibited',
              'template': 'This is a security announcement. All passengers and visitors are reminded that firearms and other weapons are strictly prohibited in the airport premises. Please cooperate with security personnel during screening procedures.',
          },
          {
              'category': 'Security and Safety Announcements',
              'name': 'Emergency Situation',
              'template': 'Attention, passengers. Due to [weather condition or emergency], all flights have been temporarily suspended. Please remain in the designated areas and follow the instructions of airport staff for your safety.',
          },
          {
              'category': 'Lost and Found Announcements',
              'name': 'Found Item',
              'template': 'Attention, passengers. A [description of item] was found at [location] within the airport premises. If this item belongs to you, please proceed to the Lost and Found counter with proper identification.',
          },
          {
              'category': 'Lost and Found Announcements',
              'name': 'Lost Item',
              'template': 'This is an announcement for the owner of a [description of item] found at [location]. If you have lost this item, please report to the Lost and Found counter immediately.',
          },
          {
              'category': 'Gate Change Announcements',
              'name': 'Gate Reassignment',
              'template': 'Attention, passengers. Flight [flight number] to [destination] has been reassigned to Gate [new gate number]. Please proceed to the new gate for boarding.',
          },
          {
              'category': 'Gate Change Announcements',
              'name': 'Gate Rerouting',
              'template': 'This is an announcement for passengers on Flight [flight number] to [destination]. Your flight has been rerouted to Gate [new gate number]. Please make your way to the new gate immediately.',
          },
          {
              'category': 'Baggage Claim Announcements',
              'name': 'Baggage Available',
              'template': 'Attention, passengers. Baggage from Flight [flight number] from [origin] is now available for pickup at Carousel [carousel number].',
          },
          {
              'category': 'Baggage Claim Announcements',
              'name': 'Baggage Unloading',
              'template': 'This is an announcement for passengers who arrived on Flight [flight number] from [origin]. Your baggage is being unloaded and will be available shortly at Carousel [carousel number].',
          },
          {
              'category': 'General Announcements',
              'name': 'Airport Closing',
              'template': 'Attention, passengers. The airport will be closing in [time remaining] due to [reason]. All remaining passengers are kindly requested to proceed to the departure gates as soon as possible.',
          },
          {
              'category': 'General Announcements',
              'name': 'No Smoking Reminder',
              'template': 'This is a reminder for all passengers. Smoking is strictly prohibited inside the airport premises, except in designated smoking areas.',
          },
          {
              'category': 'General Announcements',
              'name': 'Wi-Fi Access',
              'template': 'Attention, visitors. For your convenience, complimentary Wi-Fi is available throughout the airport. To connect, select the network named [network name] and follow the on-screen instructions.',
          },
      ]

      for subcategory_data in subcategories:
          category = Category.objects.get(name=subcategory_data['category'])
          Subcategory.objects.create(
              category=category,
              name=subcategory_data['name'],
              template=subcategory_data['template']
          )

      self.stdout.write(self.style.SUCCESS('Successfully populated the database with categories and subcategories.'))