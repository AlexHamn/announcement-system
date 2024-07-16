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
    "template_zh": "注意乘客们。[flight number]航班从[origin]飞往[destination]的登机口现在是[gate number]号。请前往指定登机口登机。"
  },
  {
    "category": "Arrival Announcements",
    "name": "Arrival Notification",
    "template": "Attention, passengers! We are pleased to announce the arrival of Flight [Flight Number] from [Departure City].",
    "template_ru": "Уважаемые пассажиры! Мы рады сообщить о прибытии рейса [Номер рейса] из [Город отправления].",
    "template_zh": "尊敬的乘客们！我们很高兴地宣布，来自[Departure City]的[Flight Number]航班已经抵达。"
  },
  {
    "category": "Boarding Announcements",
    "name": "Final Call",
    "template": "This is a final boarding call for Flight [flight number] to [destination]. All remaining passengers, please proceed to Gate [gate number] immediately.",
    "template_ru": "Заканчивается посадка на Рейс [flight number] в [destination]. Все оставшиеся пассажиры, просьба немедленно пройти к Гейту [gate number].",
    "template_zh": "这是[flight number]航班飞往[destination]的最后登机通知。所有剩余乘客，请立即前往[gate number]登机口。"
  },
  {
    "category": "Delay Announcements",
    "name": "Delay Notification",
    "template": "Attention, passengers. Flight [flight number] to [destination] has been delayed. The new estimated departure time is [new time]. We apologize for the inconvenience.",
    "template_ru": "Внимание, пассажиры. Рейс [flight number] в [destination] задерживается. Новое расчетное время вылета - [new time]. Приносим извинения за неудобства.",
    "template_zh": "注意乘客们。飞往[destination]的[flight number]航班已经延误。新的预计起飞时间是[new time]。我们为给您带来的不便深表歉意。"
  },
  {
    "category": "Cancellation Announcements",
    "name": "Cancellation Notification",
    "template": "Attention, pessengers. We regret to inform you that Flight [flight number] to [destination] has been canceled.",
    "template_ru": "Дамы и господа, мы с сожалением сообщаем, что Рейс [flight number] в [destination] был отменен.",
    "template_zh": "注意乘客们。我们很遗憾地通知您，飞往[destination]的[flight number]航班已经取消。"
  },
  {
    "category": "Check-in Announcements",
    "name": "Check-in Open",
    "template": "Dear passengers! Registration for Flight [Flight Number] is now open at the check-in counter [check-in counter number]. Passengers are kindly requested to proceed to the counter for check-in and document verification.",
    "template_ru": "Уважаемые пассажиры! Регистрация на рейс [номер рейса] открыта на стойке регистрации [номер стойки регистрации]. Просим пассажиров пройти к стойке для регистрации и проверки документов.",
    "template_zh": "尊敬的乘客们！[Flight Number]航班的登记手续现在在[check-in counter number]号登记柜台开始。请乘客前往柜台办理登记手续和文件验证。"
  },
  {
    "category": "Priority Boarding",
    "name": "Assistance and Children Boarding",
    "template": "We are now inviting passengers with small children and those needing special assistance to board Flight [number] to [destination] at Gate [number]",
    "template_ru": "Мы приглашаем пассажиров с маленькими детьми и тех, кто нуждается в специальной помощи, на посадку на рейс [номер] в [пункт назначения] у выхода [номер].",
    "template_zh": "我们现在邀请带小孩的乘客和需要特别协助的乘客登上飞往[destination]的[number]航班，请到[number]号登机口。"
  },
  {
    "category": "Priority Boarding",
    "name": "VIP Boarding Call",
    "template": "We are now inviting our first-class passengers and VIP members to board Flight [number] to [destination].",
    "template_ru": "Мы приглашаем наших пассажиров первого класса и VIP-персон на борт рейса [номер] в [пункт назначения].",
    "template_zh": "我们现在邀请头等舱乘客和VIP会员登上飞往[destination]的[number]航班。"
  },
  {
    "category": "Security Announcements",
    "name": "Unattended Baggage Warning",
    "template": "Attention, passengers. For your safety and security, please keep your belongings with you at all times and report any unattended bags or suspicious activity to the nearest security personnel.",
    "template_ru": "Внимание, пассажиры. Для вашей безопасности просьба всегда держать свои вещи при себе и сообщать об оставленных без присмотра сумках или подозрительной активности ближайшему сотруднику службы безопасности.",
    "template_zh": "注意乘客们。为了您的安全，请随时保管好您的个人物品，如发现无人看管的行李或可疑活动，请立即向最近的安保人员报告。"
  },
  {
    "category": "Security Announcements",
    "name": "Evacuation Order",
    "template": "Attention, due to an emergency, please evacuate the terminal immediately and follow the directions of airport staff.",
    "template_ru": "Внимание, в связи с чрезвычайной ситуацией, пожалуйста, немедленно эвакуируйтесь из терминала и следуйте указаниям сотрудников аэропорта.",
    "template_zh": "注意，由于紧急情况，请立即撤离航站楼，并按照机场工作人员的指示行动。"
  },
  {
    "category": "Security Announcements",
    "name": "Liquid Restrictions",
    "template": "For your safety and security, please remember that liquids, gels, and aerosols must be in containers of 100ml or less and placed in a single quart-sized zip-top bag",
    "template_ru": "Для вашей безопасности и сохранности, пожалуйста, помните, что жидкости, гели и аэрозоли должны быть в емкостях объемом не более 100 мл и помещены в один квартовый пакет с застежкой-молнией",
    "template_zh": "为了您的安全，请记住液体、凝胶和喷雾剂必须装在100毫升或更小的容器中，并放在一个夸脱大小的拉链袋中。"
  },
  {
    "category": "Security Announcements",
    "name": "Weapons Prohibition",
    "template": "All passengers and visitors are reminded that firearms and other weapons are strictly prohibited in the airport premises. Please cooperate with security personnel during screening procedures.",
    "template_ru": "Все пассажиры и посетители должны помнить, что огнестрельное оружие и другие виды оружия строго запрещены на территории аэропорта. Просьба сотрудничать с персоналом службы безопасности во время проверок.",
    "template_zh": "提醒所有乘客和访客，机场范围内严禁携带枪支和其他武器。请在安检程序中配合安保人员。"
  },
  {
    "category": "Weather and Emergency Announcements",
    "name": "Flight Suspension",
    "template": "Attention, passengers. Due to weather conditions, all flights have been temporarily suspended. Please remain in the designated areas and follow the instructions of airport staff for your safety.",
    "template_ru": "Внимание, пассажиры. Из-за погодных условий все рейсы временно приостановлены. Просьба оставаться в специально отведенных зонах и следовать указаниям персонала аэропорта для вашей безопасности.",
    "template_zh": "注意乘客们。由于天气条件，所有航班暂时停飞。为了您的安全，请留在指定区域并遵循机场工作人员的指示。"
  },
  {
    "category": "Gate Change Announcements",
    "name": "Gate Reassignment",
    "template": "Attention, passengers. Flight [flight number] to [destination] has been reassigned to Gate [new gate number]. Please proceed to the new gate for boarding.",
    "template_ru": "Внимание, пассажиры. Рейс [flight number] в [destination] был переназначен на Гейт [new gate number]. Просьба пройти к новому гейту для посадки.",
    "template_zh": "注意乘客们。飞往[destination]的[flight number]航班已被重新分配到[new gate number]登机口。请前往新的登机口登机。"
  },
  {
    "category": "Baggage Claim Announcements",
    "name": "Baggage Unloading",
    "template": "This is an announcement for passengers who arrived on Flight [flight number] from [origin]. Your baggage is being unloaded and will be available shortly at the conveyour belt [carousel number].",
    "template_ru": "Это объявление для пассажиров, прибывших Рейсом [flight number] из [origin]. Ваш багаж выгружается и будет доступен в ближайшее время на конвеерной ленте номер [carousel number].",
    "template_zh": "这是对从[origin]乘坐[flight number]航班抵达的乘客的通知。您的行李正在卸载，很快将在[carousel number]号传送带上提取。"
  },
  {
    "category": "Airport Closure Announcements",
    "name": "Airport Closing",
    "template": "Attention, passengers. The airport will be closing in [time remaining] due to [reason]. All remaining passengers are kindly requested to proceed to the departure gates as soon as possible.",
    "template_ru": "Внимание, пассажиры. Аэропорт будет закрыт через [time remaining] по причине [reason]. Все оставшиеся пассажиры просьба как можно скорее пройти к выходам на посадку.",
    "template_zh": "注意乘客们。由于[reason]，机场将在[time remaining]后关闭。请所有剩余乘客尽快前往出发登机口。"
  },
  {
    "category": "Security Announcements",
    "name": "No Smoking Reminder",
    "template": "This is a reminder for all passengers. Smoking is strictly prohibited inside the airport premises, except in designated smoking areas.",
    "template_ru": "Это напоминание для всех пассажиров. Курение строго запрещено на территории аэропорта, за исключением специально отведенных для этого зон.",
    "template_zh": "这是对所有乘客的提醒。除指定吸烟区外，机场范围内严禁吸烟。"
  },
  {
    "category": "Lost and Found Announcements",
    "name": "Lost Item Instructions",
    "template": "If you have lost an item, please check with the Lost and Found office",
    "template_ru": "Если вы потеряли какой-либо предмет, обратитесь в бюро находок.",
    "template_zh": "如果您丢失了物品，请到失物招领处查询。"
  },
  {
    "category": "Flight Information Announcements",
    "name": "Check Flight Screens",
    "template": "Please check the flight information screens for the latest updates on your flight status",
    "template_ru": "Пожалуйста, проверяйте информацию о статусе вашего рейса на экранах информации о рейсах.",
    "template_zh": "请查看航班信息屏幕以获取您的航班状态的最新更新。"
  },
  {
    "category": "Lost Child Announcements",
    "name": "Lost Child Instructions",
    "template": "Attention, if you see a lost child, please contact the nearest airport staff member.",
    "template_ru": "Внимание, если вы видите потерявшегося ребенка, пожалуйста, свяжитесь с ближайшим сотрудником аэропорта.",
    "template_zh": "注意，如果您看到迷路的儿童，请联系最近的机场工作人员。"
  },
  {
    "category": "Passenger Paging Announcements",
    "name": "Passenger Paging",
    "template": "Paging passenger [name], please report to the nearest information desk",
    "template_ru": "Вызывается пассажир [имя], пожалуйста, подойдите к ближайшей стойке информации",
    "template_zh": "呼叫[name]乘客，请到最近的问询台报到"
  },
  {
    "category": "Airport Services Announcements",
    "name": "Wi-Fi Information",
    "template": "Attention, visitors. For your convenience, complimentary Wi-Fi is available throughout the airport. To connect, select the network named [network name] and follow the on-screen instructions.",
    "template_ru": "Внимание, посетители. Для вашего удобства по всему аэропорту предоставляется бесплатный Wi-Fi. Чтобы подключиться, выберите сеть с названием [network name] и следуйте инструкциям на экране.",
    "template_zh": "注意，访客们。为了您的便利，机场全区提供免费Wi-Fi。要连接，请选择名为[network name]的网络，并按照屏幕上的说明进行操作。"
  }
]

      for subcategory_data in subcategories:
        category = Category.objects.get(name=subcategory_data['category'])
        Subcategory.objects.create(
            category=category,
            name=subcategory_data['name'],
            template=subcategory_data['template'],
            template_ru=subcategory_data['template_ru'],
            template_chinese=subcategory_data['template_chinese']
        )

      self.stdout.write(self.style.SUCCESS('Successfully populated the database with categories and subcategories.'))