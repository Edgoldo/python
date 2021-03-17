"""
    Test of inheritance. Defining of base class called ControlDates
    that is compose of dates field to control creation and update of
    registers.

    This base class is used to make some depending classes that are
    related between them
"""
from datetime import datetime

class ControlDates:
    """!
    Model to set control dates to registers of models
    """

    def __init__(self):
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def getControlDates(self):
        """!
        Function to show string
        """
        return 'Creado el ' + self.created_at.strftime('%Y-%m-%d') + \
               ' Actualizado el ' + self.updated_at.strftime('%Y-%m-%d')

class Country(ControlDates):
    """!
    Model to manage Countries registers
    """

    def __init__(self):
        super().__init__()
        self.name = ''
        self.code = ''

    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code

    def __str__(self):
        """!
        Function to show string
        """
        return self.name + ' ' + self.getControlDates()

class State(ControlDates):
    """!
    Model to manage States registers
    """

    def __init__(self):
        super().__init__()
        self.name = ''
        self.country = Country()

    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country

    def __str__(self):
        """!
        Function to show string
        """
        return self.name + ' ' + self.getControlDates()


class City(ControlDates):
    """!
    Model to manage Cities registers
    """

    def __init__(self):
        super().__init__()
        self.name = ''
        self.state = State()

    def __init__(self, name, state):
        super().__init__()
        self.name = name
        self.state = state

    def __str__(self):
        """!
        Function to show string
        """
        return self.name + ' ' + self.getControlDates()

class Currency(ControlDates):
    """!
    Object to manage Currencies registers
    """

    def __init__(self):
        super().__init__()
        self.name = ''
        self.code = ''
        self.default = False
        self.country = Country()

    def __init__(self, name, code, default, country):
        super().__init__()
        self.name = name
        self.code = code
        self.default = default if default else False
        self.country = country

    def __str__(self):
        """!
        Function to show string
        """
        return self.name + ' ' + self.getControlDates()

class ExchangeRate(ControlDates):
    """!
    Object to manage Currencies registers
    """

    def __init__(self):
        super().__init__()
        self.name = ''
        self.code = ''
        self.rate = 0
        self.default = False
        self.currency = Currency()

    def __init__(self, name, code, rate, default, currency):
        super().__init__()
        self.name = name
        self.code = code
        self.rate = rate
        self.default = default if default else False
        self.currency = currency

    def __str__(self):
        """!
        Function to show string
        """
        return self.name + ' ' + self.getControlDates()

class Bank(ControlDates):
    """!
    Object to manage Banks registers
    """

    def __init__(self):
        super().__init__()
        self.name = ''
        self.code = ''
        self.country = Country()
        self.currency = Currency()

    def __init__(self, name, code, country, currency):
        super().__init__()
        self.name = name
        self.code = code
        self.country = country
        self.currency = currency

    def __str__(self):
        """!
        Function to show string
        """
        return self.name + ' ' + self.getControlDates()

control_dates = ControlDates()

name, code = 'Venezuela', 'VE'
country = Country(name, code)

name = 'Merida'
state = State(name, country)

name = 'Ejido'
city = City(name, state)

name, code, default = 'Dolar', 'USD', True
currency = Currency(name, code, default, country)

name, code, rate, default = 'Bolivar oficial', 'VES', 8.333333333333334e-06, True
exchange_rate = ExchangeRate(name, code, rate, default, currency)

name, code = 'Banco Mercantil', '0105'
bank = Bank(name, code, country, currency)

print('control_dates -> ', control_dates.getControlDates())
print('country -> ', country)
print('state -> ', state)
print('city -> ', city)
print('currency -> ', currency)
print('exchange_rate -> ', exchange_rate)
print('bank -> ', bank)
