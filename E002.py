from datetime import datetime, timedelta
import re

class Customer:
    def __init__(self, name, email, phone, street, city, state, country, customer_type, company=None):
        self.name = self.validate_name(name)
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.street = self.validate_name(street)
        self.city = self.validate_name(city)
        self.state = self.validate_name(state)
        self.country = self.validate_name(country)
        self.company = company
        self.type = customer_type
        
    def __repr__(self):
        return f"{self.name}, {self.email}, {self.phone}, {self.street}, {self.city}, {self.state}, {self.country}, {self.company}, {self.type}"
        
    def valid_type(self):
        if Customer.customer_type not in ["company", "contact", "billing", "shipping"]:
            return"Invalid customer type. Choose from 'company', 'contact', 'billing', 'shipping'."

        
    def validate_name(self, value):
        if any(char.isdigit() for char in value):
                print("name, street, city, state cannot contain numbers")
        return value
    
    def validate_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return"Invalid Email Address"
        
        return email
    
    def validate_phone(self, phone):
        if re.match(r"\d{10}", phone):
            return"Invalid Phone Number"
        return phone

class OrderLine:
    def __init__(self, order, product, quantity, price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.calculate_subtotal()
    
    def calculate_subtotal(self):
        return self.quantity * self.price

class Order:
    def __init__(self, number, date, company, billing, shipping, order_line):
        self.number = number
        self.date = self.validate_date(date)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = order_line
        self.total_amount = self.calculate_total_amount()
        
    def __repr__(self):
        return f'Order({self.number}, {self.date}, {self.company}, {self.billing} {self.shipping} {self.order_lines}'
        
    def validate_date(self, date):
        if date <= datetime.now().date():
            print("Invalid date given, it must be of today or of the future")
        return date   

    def calculate_total_amount(self):
        return sum(order_line.subtotal for order_line in self.order_lines)

company_customer1 = Customer("Company XYZ", "info@companyxyz.com", "1234567890", "Main St", "Cityville", "CA", "USA", None, "company")
billing_customer1 = Customer("John Doe", "john.doe@email.com", "987654321", "Oak St", "Townsville", "NY", "USA", "company", "billing")
shipping_customer1 = Customer("Jane Doe", "jane.doe@email.com", "567890123", "Pine St", "Villageton", "TX", "USA", "company", "shipping")
shipping_customer2 = Customer("John vajlani", "vajnlani@gmail.com", "9808608334", "Navri ST", "Jamnagar", "Gujarat", "India", "company" "shipping")
billing_customer2 = Customer("Dhansukhlal", "Dhansukh@gmail.com", "1245663778", "PostST", "Gorakpur", "Maharashtra", "India", "company" "billing")
company_customer2 = Customer("Raj Ansari", "rajansari@gmail.com", "9898535691", "LalrajST", "Gurgaon", "Maharashtra", "India", None, "company")




order_line1 = OrderLine(None, "TV", 5, 65000)
order_line2 = OrderLine(None, "Mixture Grinder", 3, 350)
order_line3 = OrderLine(None, "Laptop", 8, 38000)
order_line4 = OrderLine(None, "Combat Keychain", 6, 250)
order_line5 = OrderLine(None, "Chair", 4, 2500)
order_line6 = OrderLine(None, "Bedsheets", 10, 1500)

olllist = [order_line1, order_line2, order_line3, order_line4, order_line5, order_line6]

order1 = Order("ORD001",  datetime(2024, 1, 24).date(), None,  billing_customer1.name, shipping_customer2.name)
order2 = Order("ORD002", datetime(2024, 3, 25).date(), None, billing_customer2.name, shipping_customer2.name)
order3 = Order("ORD003", datetime(2024, 4, 3).date(), None,  billing_customer1.name, shipping_customer1.name)
order4 = Order("ORD010", datetime(2024, 1, 28).date(), None,  billing_customer2.name, shipping_customer1.name)
order5 = Order("ORD012", datetime(2024, 6, 30).date(), None,  billing_customer1.name, shipping_customer2.name)
order6 = Order("ORD005", datetime(2024, 5, 10).date(), None,  billing_customer2.name, shipping_customer1.name)

orders = [order1, order2, order3, order4, order5, order6]


def list_order(self):
    for items in olllist:
        orders.append(items)
        return orders
    










    
