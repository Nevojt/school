class MoneyMachine:
    
    """CURRENCY: Змінна класу, яка визначає валюту, в якій показуються гроші. У вашому випадку це "$"."""
    CURRENCY = "$"
    
    """COIN_VALUES: Словник, що визначає вартість кожного типу монети. """
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    """Ініціалізує два атрибути екземпляру:
        profit: Зберігає загальний прибуток від усіх успішних транзакцій.
        money_received: Зберігає загальну суму грошей, отриманих в поточній транзакції."""
    def __init__(self) -> None:
        self.profit = 0
        self.money_received = 0
        
    """Виводить загальний прибуток машини, що використовує валюту, вказану в CURRENCY."""
    def report(self):
        # Друкуємо скільки ми заробили
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    """Запрошує користувача вставити монети і підраховує загальну суму внесених грошей на основі значень в COIN_VALUES.
        Для кожного типу монети запитує кількість монет і враховує їх вартість у money_received.
        Повертає загальну суму внесених грошей.""" 
    def process_coins(self):
        # Повертаємо суму підраховану з повернених монет
        print("Please insert coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
    
    
    """Спочатку обробляє внесені монети за допомогою process_coins().
        Перевіряє, чи достатньо грошей, внесених для покриття вартості cost.
        Якщо грошей достатньо:
        Розраховує решту і видає її.
        Додає вартість покупки до profit.
        Скидає money_received до 0.
        Повертає True, що позначає успішний платіж.
        Якщо грошей не достатньо:
        Інформує користувача про недостатню кількість грошей і повертає їх.
        Скидає money_received до 0.
        Повертає False, що позначає невдалу спробу платежу.
        """
    def make_payment(self, cost):
        # Перевіряємо чи є достатньо коштів для оплати
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False