from datetime import datetime

class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.last_service_date = None
        self.service_history = []
        
    def service(self, service_date):
        self.last_service_date = service_date
        self.service_history.append(service_date)
        print('Car serviced successfully!')
        
    def contact_manufacturer(self, message):
        print(f'Message sent to manufacturer: {message}')

class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Salesperson:
    def __init__(self, name, commission_rate):
        self.name = name
        self.commission_rate = commission_rate

class Sale:
    def __init__(self, car, customer, salesperson, sale_date):
        self.car = car
        self.customer = customer
        self.salesperson = salesperson
        self.sale_date = sale_date

cars = []
customers = []
salespersons = []
sales = []

authorized = False  # authentication flag

def authenticate():
    global authorized
    password = input('Enter password: ')
    if password == 'admin':
        authorized = True
    else:
        print('Invalid password. Access denied.')

def add_car():
    if not authorized:
        print('Access denied. Please authenticate.')
        authenticate()
        if not authorized:
            return
    make = input('Enter make: ')
    model = input('Enter model: ')
    year = input('Enter year: ')
    price = input('Enter price: ')
    car = Car(make, model, year, price)
    cars.append(car)
    print('Car added successfully!')

def add_customer():
    if not authorized:
        print('Access denied. Please authenticate.')
        authenticate()
        if not authorized:
            return
    name = input('Enter name: ')
    address = input('Enter address: ')
    phone = input('Enter phone: ')
    customer = Customer(name, address, phone)
    customers.append(customer)
    print('Customer added successfully!')

def add_salesperson():
    if not authorized:
        print('Access denied. Please authenticate.')
        authenticate()
        if not authorized:
            return
    name = input('Enter name: ')
    commission_rate = input('Enter commission rate: ')
    salesperson = Salesperson(name, commission_rate)
    salespersons.append(salesperson)
    print('Salesperson added successfully!')

def make_sale():
    if not authorized:
        print('Access denied. Please authenticate.')
        authenticate()
        if not authorized:
            return
    make = input('Enter make: ')
    model = input('Enter model: ')
    year = input('Enter year: ')
    price = input('Enter price: ')
    car = Car(make, model, year, price)
    customer_name = input('Enter customer name: ')
    customer = next((c for c in customers if c.name == customer_name), None)
    salesperson_name = input('Enter salesperson name: ')
    salesperson = next((s for s in salespersons if s.name == salesperson_name), None)
    sale = Sale(car, customer, salesperson, datetime.now())
    sales.append(sale)
    print('Sale made successfully!')

def view_information():
    if not authorized:
        print('Access denied. Please authenticate.')
        authenticate()
        if not authorized:
            return
    print('Cars:')
    for car in cars:
        print(f'{car.make} {car.model} {car.year} ${car.price} Last serviced on: {car.last_service_date} Service history: {car.service_history}')
    print('Customers:')
    for customer in customers:
        print(f'{customer.name} {customer.address} {customer.phone}')
    print('Salespersons:')
    for salesperson in salespersons:
        print(f'{salesperson.name} {salesperson.commission_rate}%')

def view_cars():
    print('Cars:')
    for car in cars:
        print(f'{car.make} {car.model} {car.year} ${car.price}')

def service_car():
    if not authorized:
        print('Access denied. Please authenticate.')
        authenticate()
        if not authorized:
            return
    make = input('Enter make: ')
    model = input('Enter model: ')
    year = input('Enter year: ')
    car = next((c for c in cars if c.make == make and c.model == model and c.year == year), None)
    if car is None:
        print('Car not found.')
        return
    service_date = datetime.now()
    car.service(service_date)

def contact_manufacturer():
    if not authorized:
        print('Access denied. Please authenticate.')
        authenticate()
        if not authorized:
            return
    make = input('Enter make: ')
    model = input('Enter model: ')
    year = input('Enter year: ')
    message = input('Enter message: ')
    car = next((c for c in cars if c.make == make and c.model == model and c.year == year), None)
    if car is None:
        print('Car not found.')
        return
    car.contact_manufacturer(message)
    print('Message sent successfully!')

while True:
    print('1. Add car')
    print('2. Add customer')
    print('3. Add salesperson')
    print('4. Make sale')
    print('5. View information')
    print('6. View cars')
    print('7. Service car')
    print('8. Contact manufacturer')
    print('9. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        add_car()
    elif choice == '2':
        add_customer()
    elif choice == '3':
        add_salesperson()
    elif choice == '4':
        make_sale()
    elif choice == '5':
        view_information()
    elif choice == '6':
        view_cars()
    elif choice == '7':
        service_car()
    elif choice == '8':
        contact_manufacturer()
    elif choice == '9':
        break
    else:
        print('Invalid choice. Please try again.')
