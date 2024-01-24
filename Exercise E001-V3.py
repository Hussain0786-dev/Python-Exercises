class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def __str__(self):
        return f"{self.name} ({self.code})"

        
class Product:         # Define Product Class
    def __init__(self, name, code, price, stock_at_location):  #Initializing Product Calass
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_location = stock_at_location
        # self.stock_at_location = {}
        
    
    
    def product_at_location():
        for pro in products:
            print(pro.name, pro.code, pro.price)
            print(pro.stock_at_location)
            print("\n")
        
class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
    
    def movement_by_product(p):
        for mov in movements:
            if mov.product.name == p.name:
                print(mov.from_location.name, mov.product.name, mov.to_location.name)
                if p.stock_at_location == {}:
                    for loc in locations:
                        if loc.name == mov.to_location.name:
                            # pr.stock_at_location[loc.name] = mov.quantity
                            pr.stock_at_location[mov.to_location.name] = mov.quantity
                            # print(pr.stock_at_location)
                        else:
                            pr.stock_at_location[loc.name] = 0
                            # print(pr.stock_at_location)
                else:    
                    for loc in locations:
                        if loc.name == mov.to_location.name:
                            pr.stock_at_location[loc.name] += mov.quantity
                            # print(pr.stock_at_location)
                            
                        elif loc.name == mov.from_location.name:
                            pr.stock_at_location[loc.name] -= mov.quantity
                            # print(pr.stock_at_location)
                        else:
                            continue                
        print("\n")

    
l1 = Location("Rajkot", "L001")
l2 = Location("Ahmedabad", "L002")
l3 = Location("surendrangar", "L003")
l4 = Location("Gandhinagar", "L004")

locations = [l1, l2, l3, l4] 



# p1 = Product("TV" , "C002", 12000, {l1.name: 200, l2.name: 40, l3.name: 80, l4.name: 45})
# p2 = Product("Fridge" , "H002", 23000, {l1.name: 60, l2.name: 80, l3.name: 78, l4.name: 67})
# p3 = Product("Washing Machine" , "S000", 20000, {l1.name: 58, l2.name: 34, l3.name: 56, l4.name: 90})
# p4 = Product("Microwave" , "H001", 25000, {l1.name: 69, l2.name: 78, l3.name:23, l4.name: 89})
# p5 = Product("Table" , "S005", 26000, {l1.name: 98, l2.name:86, l3.name: 45, l4.name: 78})

# p1 = Product("TV" , "C002", 12000)
# p2 = Product("Fridge" , "H002", 23000)
# p3 = Product("Washing Machine" , "S000", 20000)
# p4 = Product("Microwave" , "H001", 25000)
# p5 = Product("Table" , "S005", 26000)

p1 = Product("TV" , "C002", 12000, {l1.name: 200, l2.name: 40, l3.name: 80, l4.name: 45})
p2 = Product("Fridge" , "H002", 23000, {})
p3 = Product("Washing Machine" , "S000", 20000, {l1.name: 58, l2.name: 34, l3.name: 56, l4.name: 90})
p4 = Product("Microwave" , "H001", 25000, {})
p5 = Product("Table" , "S005", 26000, {l1.name: 98, l2.name:86, l3.name: 45, l4.name: 78})


products = [p1, p2, p3, p4, p5]



movement1 = Movement(l1, l2, p1, 30)
movement2 = Movement(l2, l3, p2, 50)
movement3 = Movement(l3, l4, p3, 30)
movement4 = Movement(l4, l3, p4, 60)
movement5 = Movement(l2, l3, p5, 70)

movements = [movement1, movement2, movement3, movement4, movement5]

# Product.stock_at_location = {
#     p1.name : {l1.name: 200, l2.name: 40, l3.name: 80, l4.name: 45},
#     p2.name : {l1.name: 60, l2.name: 80, l3.name: 78, l4.name: 67},
#     p3.name : {l1.name: 58, l2.name: 34, l3.name: 56, l4.name: 90},
#     p4.name : {l1.name: 69, l2.name: 78, l3.name:23, l4.name: 89},
#     p5.name : {l1.name: 98, l2.name:86, l3.name: 45, l4.name: 78}
# }

Product.product_at_location()
print()

for pr in products:
    print(pr.name)
    Movement.movement_by_product(pr)
    
    
# print(p2.stock_at_location)
Product.product_at_location()




