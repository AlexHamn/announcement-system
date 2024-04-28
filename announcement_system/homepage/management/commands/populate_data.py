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
          'template': 'Attention, passengers. Flight [flight_number] from [origin] to [destination] is now arriving at Gate [gate_number]. Please proceed to the designated gate for boarding.',
          'template_ru': 'Внимание, пассажиры. Рейс [flight_number] из [origin] в [destination] прибывает на Гейт [gate_number]. Просьба пройти к указанному гейту для посадки.',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. [flight_number] рейси [origin] шаарынан [destination] шаарына [gate_number]-тарзында келип жатат. Белгиленген тарзга өтүп, отурушуңузду өтүнөбүз.',
        },
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Final Boarding Call',
          'template': 'This is a final boarding call for Flight [flight_number] to [destination]. All remaining passengers, please proceed to Gate [gate_number] immediately. The gate will close in [time_remaining].',
          'template_ru': 'Заканчивается посадка на Рейс [flight_number] в [destination]. Все оставшиеся пассажиры, просьба немедленно пройти к Гейту [gate_number]. Гейт закроется через [time_remaining].',
          'template_kg': '[flight_number] рейсине [destination] шаарына акыркы чакырык. Калган бардык жолоочулар, дароо [gate_number]-тарзына өтүшүңүздү суранабыз. Бул тарз [time_remaining] ичинде жабылат.',
        },
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Flight Delay',
          'template': 'Attention, passengers. Flight [flight_number] to [destination] has been delayed due to [reason]. The new estimated departure time is [new time]. We apologize for the inconvenience.',
          'template_ru': 'Внимание, пассажиры. Рейс [flight_number] в [destination] задерживается из-за [reason]. Новое расчетное время вылета - [new time]. Приносим извинения за неудобства.',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. [flight_number] рейси [destination] шаарына [reason] себептен кечиктирилди. Жаңы чыгуу убактысы [new time] болот. Келбетсиздик үчүн кечирим суранабыз.',
        },
        {
          'category': 'Arrival and Departure Announcements',
          'name': 'Flight Cancellation',
          'template': 'Ladies and gentlemen, we regret to inform you that Flight [flight_number] to [destination] has been canceled due to [reason]. Please proceed to the airline\'s counter for rebooking or refund assistance.',
          'template_ru': 'Дамы и господа, мы с сожалением сообщаем, что Рейс [flight_number] в [destination] отменен по причине [reason]. Просьба обратиться к стойке авиакомпании для повторного бронирования или возврата.',
          'template_kg': 'Урматтуу жолоочулар, [flight_number] рейси [destination] шаарына [reason] себептен жокко чыгарылганын билдирүүгө күйүнөбүз. Кайра брондоо же төлөмдү кайтарып алуу үчүн авиакомпаниянын столуна барыңыз.',
        },
        {
          'category': 'Security and Safety Announcements',
          'name': 'Security Reminder',
          'template': 'Attention, passengers. For your safety and security, please keep your belongings with you at all times and report any unattended bags or suspicious activity to the nearest security personnel.',
          'template_ru': 'Внимание, пассажиры. Для вашей безопасности просьба всегда держать свои вещи при себе и сообщать об оставленных без присмотра сумках или подозрительной активности ближайшему сотруднику службы безопасности.',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. Коопсуздугуңуз үчүн, өз буюмдарыңызды дайыма жанында кармап жүрүңүз жана көзөмөлсүз баштыктар же шектүү аракеттер тууралуу жакын жердеги коопсуздук кызматкерлерине кабарлаңыз.',
        },
        {
          'category': 'Security and Safety Announcements',
          'name': 'Weapons Prohibited',
          'template': 'This is a security announcement. All passengers and visitors are reminded that firearms and other weapons are strictly prohibited in the airport premises. Please cooperate with security personnel during screening procedures.',
          'template_ru': 'Это объявление о безопасности. Все пассажиры и посетители должны помнить, что огнестрельное оружие и другие виды оружия строго запрещены на территории аэропорта. Просьба сотрудничать с персоналом службы безопасности во время проверок.',
          'template_kg': 'Бул коопсуздук жөнүндөгү кабарлоо. Бардык жолоочулар жана келүүчүлөр аэропорт аймагында ыктыярдуу түрдө ооздукталган курал-жарактар жана башка куралдар катуу тыюу салынгандыгын билишүүсү керек. Текшерүү жол-жоболорунда коопсуздук кызматкерлери менен кызматташуу сунушталат.',
        },
        {
          'category': 'Security and Safety Announcements',
          'name': 'Emergency Situation',
          'template': 'Attention, passengers. Due to [weather_condition_or_emergency], all flights have been temporarily suspended. Please remain in the designated areas and follow the instructions of airport staff for your safety.',
          'template_ru': 'Внимание, пассажиры. Из-за [weather_condition_or_emergency] все рейсы временно приостановлены. Просьба оставаться в специально отведенных зонах и следовать указаниям персонала аэропорта для вашей безопасности.',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. [weather_condition_or_emergency] себептүү бардык учуулар убактылуу токтотулду. Коопсуздугуңуз үчүн белгиленген аймактарда калып, аэропорт кызматкерлеринин көрсөтмөлөрүн аткарыңыз.',
        },
        {
          'category': 'Lost and Found Announcements',
          'name': 'Found Item',
          'template': 'Attention, passengers. A [description_of_item] was found at [location] within the airport premises. If this item belongs to you, please proceed to the Lost and Found counter with proper identification.',
          'template_ru': 'Внимание, пассажиры. [description_of_item] нашли в [location] на территории аэропорта. Если эта вещь принадлежит вам, просьба обратиться на стойку находок с соответствующим удостоверением личности.',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. [description_of_item] аэропорт аймагындагы [location] жерде табылды. Эгер бул буюм сизге таандык болсо, тиешелүү документ менен Жоголгон жана Табылган нерселер столуна барыңыз.',
        },
        {
          'category': 'Lost and Found Announcements',
          'name': 'Lost Item',
          'template': 'This is an announcement for the owner of a [description_of_item] found at [location]. If you have lost this item, please report to the Lost and Found counter immediately.',
          'template_ru': 'Это объявление для владельца [description_of_item], найденного в [location]. Если вы потеряли эту вещь, просьба немедленно обратиться на стойку находок.',
          'template_kg': 'Бул [location] жерде табылган [description of item] ээсине арналган кабарлама. Эгер сиз ушул буюмду жоготкон болсоңуз, дароо Жоголгон жана Табылган нерселер столуна кайрылыңыз.',
        },
        {
          'category': 'Gate Change Announcements',
          'name': 'Gate Reassignment',
          'template': 'Attention, passengers. Flight [flight_number] to [destination] has been reassigned to Gate [new_gate_number]. Please proceed to the new gate for boarding.',
          'template_ru': 'Внимание, пассажиры. Рейс [flight_number] в [destination] был переназначен на Гейт [new_gate_number]. Просьба пройти к новому гейту для посадки.',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. [flight_number] рейси [destination] шаарына [new_gate_number]-тарзына кайра бөлүштүрүлдү. Отуруш үчүн жаңы тарзга өтүңүз.',
        },
        {
          'category': 'Gate Change Announcements',
          'name': 'Gate Rerouting',
          'template': 'This is an announcement for passengers on Flight [flight_number] to [destination]. Your flight has been rerouted to Gate [new_gate_number]. Please make your way to the new gate immediately.',
          'template_ru': 'Это объявление для пассажиров Рейса [flight_number] в [destination]. Ваш рейс был переведен на Гейт [new_gate_number]. Просьба незамедлительно пройти к новому гейту.',
          'template_kg': 'Бул [flight number] рейсине [destination] шаарына жолоочулар үчүн. Сиздин учуш [new_gate_number]-тарзга кайта багытталды. Зарыл болсо, дароо жаңы тарзга өтүңүз.',
        },
        {
          'category': 'Baggage Claim Announcements',
          'name': 'Baggage Available',
          'template': 'Attention, passengers. Baggage from Flight [flight_number] from [origin] is now available for pickup at the conveyour belt number [carousel_number].',
          'template_ru': 'Внимание, пассажиры. Багаж с Рейса [flight_number] из [origin] сейчас доступен для получения на конвеерной ленте номер [carousel_number].',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. [origin] шаарынан келген [flight_number] рейсинин багажы азыр [carousel_number]-караусел үстүндө алынышы мүмкүн.',
        },
        {
          'category': 'Baggage Claim Announcements',
          'name': 'Baggage Unloading',
          'template': 'This is an announcement for passengers who arrived on Flight [flight_number] from [origin]. Your baggage is being unloaded and will be available shortly at the conveyour belt [carousel_number].',
          'template_ru': 'Это объявление для пассажиров, прибывших Рейсом [flight_number] из [origin]. Ваш багаж выгружается и будет доступен в ближайшее время на конвеерной ленте номер [carousel_number].',
          'template_kg': 'Бул [origin] шаарынан келген [flight_number] рейсинин жолоочулары үчүн кабарлоо. Сиздин багаждар түшүрүлүп жатат жана кыска арада [carousel_number]-караусел үстүндө алынышы мүмкүн.',
        },
        {
          'category': 'General Announcements',
          'name': 'Airport Closing',
          'template': 'Attention, passengers. The airport will be closing in [time_remaining] due to [reason]. All remaining passengers are kindly requested to proceed to the departure gates as soon as possible.',
          'template_ru': 'Внимание, пассажиры. Аэропорт будет закрыт через [time_remaining] по причине [reason]. Все оставшиеся пассажиры просьба как можно скорее пройти к выходам на посадку.',
          'template_kg': 'Жолоочулар, көңүлүңүздү бурабыз. [reason] себептен аэропорт [time_remaining] ичинде жабылат. Калган бардык жолоочулар мүмкүн болушунча тездетип чыгуу тарзына өтүшүңүздү сунушубуз.',
        },
        {
          'category': 'General Announcements',
          'name': 'No Smoking Reminder',
          'template': 'This is a reminder for all passengers. Smoking is strictly prohibited inside the airport premises, except in designated smoking areas.',
          'template_ru': 'Это напоминание для всех пассажиров. Курение строго запрещено на территории аэропорта, за исключением специально отведенных для этого зон.',
          'template_kg': 'Бул бардык жолоочулар үчүн эскертүү. Аэропорт аймагында белгиленген тамеки тартуу жайларынан тышкары, тамеки тартуу катуу тыюу салынат.',
        },
        {
          'category': 'General Announcements',
          'name': 'Wi-Fi Access',
          'template': 'Attention, visitors. For your convenience, complimentary Wi-Fi is available throughout the airport. To connect, select the network named [network_name] and follow the on-screen instructions.',
          'template_ru': 'Внимание, посетители. Для вашего удобства по всему аэропорту предоставляется бесплатный Wi-Fi. Чтобы подключиться, выберите сеть с названием [network_name] и следуйте инструкциям на экране.',
          'template_kg': 'Келүүчүлөр, көңүлүңүздү бурабыз. Ыңгайлуулук үчүн, аэропорт аймагында акысыз Wi-Fi тармагы бар. Туташуу үчүн [network_name] деген тармакты тандап, экрандагы көрсөтмөлө',
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