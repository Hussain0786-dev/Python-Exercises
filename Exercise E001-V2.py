class Category:
    def __init__(self, name, code, no_of_pproducts=0, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.children = []
        self.display_name = self.generate_display_name()
        self.no_of_products = []
        
    def generate_display_name(self):
        if self.parent:
            return f"{self.parent.generate_display_name()} > {self.name}"
        else:
            return self.name
        
    def add_child(self, child_category):
        self.children.append(child_category)
    
    def add_product(self, product):
        self.no_of_products.append(product)
        
    def calculate_no_of_products(self):
        return len(self.no_of_products)
    
    def __repr__(self):
        return f"{self.name},code: {self.code}, Display Name: {self.display_name}, Number of Products: {self.calculate_no_of_products()})"

class Product:         # Define Product Class
    def __init__(self, name, code, category, price):  #Initializing Product Calass
        self.name = name
        self.code = code
        self.category = category
        self.price = price

        # add product category's list
        category.add_product(self)
    #String representation of Product  
    def __repr__(self):
        return f"{self.name} (code: {self.code}, Category: {self.category.name}, Price: {self.price})"

vehicle_category = Category("Vehicle", "V001")
car_category = Category("Car", "C004", parent=vehicle_category)
petrol_category = Category("Petrol", "P001", parent=car_category)
bike_category = Category("Bike", "B001", parent=vehicle_category)
diesel_category = Category("Diesel", "D002", parent=car_category)
category1 = Category("Cross", "C001")
category2 = Category("Hatchback","H003")
category3 = Category("SUV","S009")


vehicle_category.add_child(car_category)
vehicle_category.add_child(bike_category)
car_category.add_child(petrol_category)
car_category.add_child(diesel_category)
bike_category.add_child(petrol_category)



product1 = Product("BMWi7" , "C002", category1, 120000)
product2 = Product("VolvoH" , "H002", category2, 230000)
product3 = Product("Gwagoon" , "S000", category3, 200000)
product4 = Product("Audih8" , "H001", category2, 250000)
product5 = Product("AudiQ7" , "S005", category3, 260000)
product6 = Product("SkodaH7" , "H007", category2, 180000)
product7 = Product("SkodaS2" , "S009", category3, 90000)
product8 = Product("Mercedes X8" , "C008", category1, 280000)
product9 = Product("MercedesH3" , "H002", category2, 220000)
product10 = Product("WolkswagonH00" , "H006", category2, 100000)
product11 = Product("DucatiS4", "B004", bike_category, 800000)
product12 = Product("Honda Cb300f" , "B005", bike_category, 190000)
product13 = Product("Fzs V4", "B009", bike_category, 150000)
product14 = Product("Endeavour", "S007", diesel_category, 160000)
product15 = Product("Fortuner", "S010", diesel_category, 250000)
product16 = Product("Hilux", "S011", diesel_category, 300000)
product17 = Product("VolvoV10", "H003", petrol_category, 290000)
product18 = Product("Mercedes Xm10", "C010", petrol_category, 310000)
product19 = Product("Nexon", "C011", petrol_category, 50000)
product20 = Product("Truck", "TRUCK001", vehicle_category, 58000)
product21 = Product("Electric Bike", "EBIKE001", vehicle_category, 67000)
product22 = Product("Electric Car", "ECAR001", vehicle_category, 48000)


products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13, product14, product15, product16, product17, product18, product19, product20, product21, product22]

print("Category Information:")
for category in [category1, category2, category3]:
    print(category)
    
ssearch = input("Do you wnat to  see based on price , Type LOW for low to high and Type HIGH For high to low: ")

# it will sort and print product in lower to higher order
if ssearch == 'low':
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            if products[i].price > products[j].price:
                # Swap the products in the list if the price is lower
                products[i], products[j] = products[j], products[i]
    for product in products:
        print(product)

# it will sort and print products in higher to lower order      
elif ssearch == 'high':
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            if products[i].price < products[j].price:
                products[i], products[j] = products[j], products[i]
    for product in products:
        print(product)   
        
        
        
        
#  program will execute this statement if input is given incorrectly 
csearch = input("Please Enter the code for search: ")
found = None
for product in products:
    if product.code == csearch:
        found = product
        break
if found:
    print(found)
else:
    print("Please Enter Valid Code")

# Display Category with Code, Display Name, and all product details inside that category    
all_categories = [category1, category2, category3, vehicle_category, car_category, petrol_category, bike_category, diesel_category]
all_categories.sort(key=lambda x: x.name)

for category in all_categories:
    print(category)
    print("\nProducts:")
    for product in category.no_of_products:
        print(product)
    print("\n" + "="*40)

# Display product list by category (group by category, order by category name)    
for category in all_categories:
    print(f"\nProducts in {category.display_name}:")
    for product in category.no_of_products:
        print(product)
    print("\n" + "="*40)

