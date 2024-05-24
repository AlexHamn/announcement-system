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
    "category": "Boarding Announcements",
    "name": "Boarding Call",
    "template": "Attention, passengers. Flight [flight number] from [origin] to [destination] is now at Gate [gate number]. Please proceed to the designated gate for boarding.",
    "template_ru": "Внимание, пассажиры. Началась посадка на рейс [flight number] в [destination]. Просьба пройти на выход посадки [gate number].",
    "template_kg": ""
  },
  {
    "category": "Arrival Announcements",
    "name": "Arrival Notification",
    "template": "Attention, passengers! We are pleased to announce the arrival of Flight [Flight Number] from [Departure City].",
    "template_ru": "Уважаемые пассажиры! Мы рады сообщить о прибытии рейса [Номер рейса] из [Город отправления].",
    "template_kg": ""
  },
  {
    "category": "Boarding Announcements",
    "name": "Final Call",
    "template": "This is a final boarding call for Flight [flight number] to [destination]. All remaining passengers, please proceed to Gate [gate number] immediately.",
    "template_ru": "Заканчивается посадка на Рейс [flight number] в [destination]. Все оставшиеся пассажиры, просьба немедленно пройти к Гейту [gate number].",
    "template_kg": ""
  },
  {
    "category": "Delay Announcements",
    "name": "Delay Notification",
    "template": "Attention, passengers. Flight [flight number] to [destination] has been delayed. The new estimated departure time is [new time]. We apologize for the inconvenience.",
    "template_ru": "Внимание, пассажиры. Рейс [flight number] в [destination] задерживается. Новое расчетное время вылета - [new time]. Приносим извинения за неудобства.",
    "template_kg": ""
  },
  {
    "category": "Cancellation Announcements",
    "name": "Cancellation Notification",
    "template": "Attention, pessengers. We regret to inform you that Flight [flight number] to [destination] has been canceled.",
    "template_ru": "Дамы и господа, мы с сожалением сообщаем, что Рейс [flight number] в [destination] был отменен.",
    "template_kg": ""
  },
  {
    "category": "Check-in Announcements",
    "name": "Check-in Open",
    "template": "Dear passengers! Registration for Flight [Flight Number] is now open at the check-in counter [check-in counter number]. Passengers are kindly requested to proceed to the counter for check-in and document verification.",
    "template_ru": "Уважаемые пассажиры! Регистрация на рейс [номер рейса] открыта на стойке регистрации [номер стойки регистрации]. Просим пассажиров пройти к стойке для регистрации и проверки документов.",
    "template_kg": ""
  },
  {
    "category": "Priority Boarding",
    "name": "Assistance and Children Boarding",
    "template": "We are now inviting passengers with small children and those needing special assistance to board Flight [number] to [destination] at Gate [number]",
    "template_ru": "Мы приглашаем пассажиров с маленькими детьми и тех, кто нуждается в специальной помощи, на посадку на рейс [номер] в [пункт назначения] у выхода [номер].",
    "template_kg": ""
  },
  {
    "category": "Priority Boarding",
    "name": "VIP Boarding Call",
    "template": "We are now inviting our first-class passengers and VIP members to board Flight [number] to [destination].",
    "template_ru": "Мы приглашаем наших пассажиров первого класса и VIP-персон на борт рейса [номер] в [пункт назначения].",
    "template_kg": ""
  },
  {
    "category": "Security Announcements",
    "name": "Unattended Baggage Warning",
    "template": "Attention, passengers. For your safety and security, please keep your belongings with you at all times and report any unattended bags or suspicious activity to the nearest security personnel.",
    "template_ru": "Внимание, пассажиры. Для вашей безопасности просьба всегда держать свои вещи при себе и сообщать об оставленных без присмотра сумках или подозрительной активности ближайшему сотруднику службы безопасности.",
    "template_kg": ""
  },
  {
    "category": "Security Announcements",
    "name": "Evacuation Order",
    "template": "Attention, due to an emergency, please evacuate the terminal immediately and follow the directions of airport staff.",
    "template_ru": "Внимание, в связи с чрезвычайной ситуацией, пожалуйста, немедленно эвакуируйтесь из терминала и следуйте указаниям сотрудников аэропорта.",
    "template_kg": ""
  },
  {
    "category": "Security Announcements",
    "name": "Liquid Restrictions",
    "template": "For your safety and security, please remember that liquids, gels, and aerosols must be in containers of 100ml or less and placed in a single quart-sized zip-top bag",
    "template_ru": "Для вашей безопасности и сохранности, пожалуйста, помните, что жидкости, гели и аэрозоли должны быть в емкостях объемом не более 100 мл и помещены в один квартовый пакет с застежкой-молнией",
    "template_kg": ""
  },
  {
    "category": "Security Announcements",
    "name": "Weapons Prohibition",
    "template": "All passengers and visitors are reminded that firearms and other weapons are strictly prohibited in the airport premises. Please cooperate with security personnel during screening procedures.",
    "template_ru": "Все пассажиры и посетители должны помнить, что огнестрельное оружие и другие виды оружия строго запрещены на территории аэропорта. Просьба сотрудничать с персоналом службы безопасности во время проверок.",
    "template_kg": ""
  },
  {
    "category": "Weather and Emergency Announcements",
    "name": "Flight Suspension",
    "template": "Attention, passengers. Due to weather conditions, all flights have been temporarily suspended. Please remain in the designated areas and follow the instructions of airport staff for your safety.",
    "template_ru": "Внимание, пассажиры. Из-за погодных условий все рейсы временно приостановлены. Просьба оставаться в специально отведенных зонах и следовать указаниям персонала аэропорта для вашей безопасности.",
    "template_kg": ""
  },
  {
    "category": "Gate Change Announcements",
    "name": "Gate Reassignment",
    "template": "Attention, passengers. Flight [flight number] to [destination] has been reassigned to Gate [new gate number]. Please proceed to the new gate for boarding.",
    "template_ru": "Внимание, пассажиры. Рейс [flight number] в [destination] был переназначен на Гейт [new gate number]. Просьба пройти к новому гейту для посадки.",
    "template_kg": ""
  },
  {
    "category": "Baggage Claim Announcements",
    "name": "Baggage Unloading",
    "template": "This is an announcement for passengers who arrived on Flight [flight number] from [origin]. Your baggage is being unloaded and will be available shortly at the conveyour belt [carousel number].",
    "template_ru": "Это объявление для пассажиров, прибывших Рейсом [flight number] из [origin]. Ваш багаж выгружается и будет доступен в ближайшее время на конвеерной ленте номер [carousel number].",
    "template_kg": ""
  },
  {
    "category": "Airport Closure Announcements",
    "name": "Airport Closing",
    "template": "Attention, passengers. The airport will be closing in [time remaining] due to [reason]. All remaining passengers are kindly requested to proceed to the departure gates as soon as possible.",
    "template_ru": "Внимание, пассажиры. Аэропорт будет закрыт через [time remaining] по причине [reason]. Все оставшиеся пассажиры просьба как можно скорее пройти к выходам на посадку.",
    "template_kg": ""
  },
  {
    "category": "Security Announcements",
    "name": "No Smoking Reminder",
    "template": "This is a reminder for all passengers. Smoking is strictly prohibited inside the airport premises, except in designated smoking areas.",
    "template_ru": "Это напоминание для всех пассажиров. Курение строго запрещено на территории аэропорта, за исключением специально отведенных для этого зон.",
    "template_kg": ""
  },
  {
    "category": "Lost and Found Announcements",
    "name": "Lost Item Instructions",
    "template": "If you have lost an item, please check with the Lost and Found office",
    "template_ru": "Если вы потеряли какой-либо предмет, обратитесь в бюро находок.",
    "template_kg": ""
  },
  {
    "category": "Flight Information Announcements",
    "name": "Check Flight Screens",
    "template": "Please check the flight information screens for the latest updates on your flight status",
    "template_ru": "Пожалуйста, проверяйте информацию о статусе вашего рейса на экранах информации о рейсах.",
    "template_kg": ""
  },
  {
    "category": "Lost Child Announcements",
    "name": "Lost Child Instructions",
    "template": "Attention, if you see a lost child, please contact the nearest airport staff member.",
    "template_ru": "Внимание, если вы видите потерявшегося ребенка, пожалуйста, свяжитесь с ближайшим сотрудником аэропорта.",
    "template_kg": ""
  },
  {
    "category": "Passenger Paging Announcements",
    "name": "Passenger Paging",
    "template": "Paging passenger [name], please report to the nearest information desk",
    "template_ru": "Вызывается пассажир [имя], пожалуйста, подойдите к ближайшей стойке информации",
    "template_kg": ""
  },
  {
    "category": "Airport Services Announcements",
    "name": "Wi-Fi Information",
    "template": "Attention, visitors. For your convenience, complimentary Wi-Fi is available throughout the airport. To connect, select the network named [network name] and follow the on-screen instructions.",
    "template_ru": "Внимание, посетители. Для вашего удобства по всему аэропорту предоставляется бесплатный Wi-Fi. Чтобы подключиться, выберите сеть с названием [network name] и следуйте инструкциям на экране.",
    "template_kg": ""
  }
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

      self.stdout.write(self.style.SUCCESS('Successfully populated the database with categories and subcategories.'))