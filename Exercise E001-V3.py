class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def __str__(self):
        return f"{self.name} ({self.code})"


class Movement:
    movements = []
    stock_at_location = {}
    
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        
        if self.product not in Movement.stock_at_location:
            Movement.stock_at_location[self.product] = {}
        for location in [self.from_location, self.to_location]:
            if self.from_location.name not in Movement.stock_at_location[self.product]:
                Movement.stock_at_location[self.product][self.from_location.name] = 0
        for location in [self.from_location, self.to_location]:
            if self.to_location.name not in Movement.stock_at_location[self.product]:
                Movement.stock_at_location[self.product][self.to_location.name] = 0
        
        if Movement.stock_at_location[self.product][self.from_location.name] < self.quantity:
            print("Not enough stock of {self.product} at {self.from_location.name}")
            
        
        initial_stock = Movement.stock_at_location[self.product][self.to_location.name]
        Movement.stock_at_location[self.product][self.from_location.name] -= self.quantity
        Movement.stock_at_location[self.product][self.to_location.name] += self.quantity
        
        Movement.movements.append(self)
        
        print(f"Moved {self.quantity} units of {self.product} from {self.from_location} to {self.to_location}")
        print(f"Initial stock at {self.to_location}: {initial_stock}, Updated stock: {Movement.stock_at_location[self.product][self.to_location.name]}\n")
        
    @staticmethod    
    def movements_by_product(products):
        return [movement for movement in Movement.movements if movement.product == products]
    
def movements(products):
    for product in products:
        print(f"Movements for {product}:")
        for movement in Movement.movements_by_product(product):
            print(f"From {movement.from_location} to {movement.to_location}: {movement.quantity} units")

def display_stock():
    print("\nStock at Locations: ")
    for product, stock_at_location in Movement.stock_at_location.items():
        print(f"\n{product}: {stock_at_location}")
        
def list_by_location(locations):
    print("\nProduct List by Location:")
    for location in locations:
        print(f"{location}:")
        for product, stock in Movement.stock_at_location.items():
            print(f"   {product}: Initial Stock: {stock.get(location.name, 0)}, Updated Stock: {stock.get(location.name, 0)} units")

    
    

l1 = Location("Rajkot", "L001")
l2 = Location("Ahmedabad", "L002")
l3 = Location("surendrangar", "L003")
l4 = Location("Gandhinagar", "L004")

locations = [l1, l2, l3, l4] 

p1 = "Tv"
p2 = "Fridge"
p3 = "Washing Machine"
p4 = "Microwave"
p5 = "table"

products = [p1, p2, p3, p4, p5]

Movement.stock_at_location = {
    p1 : {l1.name: 200, l2.name: 40, l3.name: 80, l4.name: 45},
    p2 : {l1.name: 60, l2.name: 80, l3.name: 78, l4.name: 67},
    p3 : {l1.name: 58, l2.name: 34, l3.name: 56, l4.name: 90},
    p4 : {l1.name: 69, l2.name: 78, l3.name:23, l4.name: 89},
}

try: 
    movement1 = Movement(l1, l2, p1, 30)
    movement2 = Movement(l2, l3, p2, 30)
    movement3 = Movement(l3, l4, p3, 30)
    movement4 = Movement(l4, l3, p4, 30)
    movement5 = Movement(l2, l3, p5, 30)
except ValueError as e:
    print(e)



movements(products)

display_stock()

list_by_location(locations)


