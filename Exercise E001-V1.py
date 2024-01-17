class Category:
  def __init__(self, name, code, no_of_products=0):
    self.name = name
    self.code = code
    self.no_of_products = []
  
  def calculate_no_of_products(self):
    return len(self.no_of_products)
    
  def __repr__(self):
    return f"{self.name} (Code: {self.code}, Number of Products: {self.calculate_no_of_products()})"

class Product:
  def __init__(self, name, code, category, price):
    self.name = name
    self.code = code
    self.category = category
    self.price = price
    category.no_of_products.append(self)
    
  def __repr__(self):
    return f"{self.name} (code: {self.code}, Category: {self.category.name}, Price: {self.price})"

category1 = Category("Cross", "C001")
category2 = Category("Hatchback","H003")
category3 = Category("SUV","S009")

categories = [category1, category2, category3]

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
# product11 = Product("YezdiHaatch" , "H006", category2, 100000)


products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]

print("Category Information:")
for category in [category1, category2, category3]:
    print(category)

ssearch = input("Do you wnat to  see based on price , Type LOW for low to high and Type HIGH For high to low: ")
if ssearch == 'low':
  products = [] 
  for category in [category1, category2, category3]:
    products.extend(category.no_of_products) 
  for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if products[i].price > products[j].price:
            # Swap the products in the list if the price is lower
            products[i], products[j] = products[j], products[i]

  for product in products:
      print(product)
      
elif ssearch == 'high':
  products = [] 
  for category in [category1, category2, category3]:
    products.extend(category.no_of_products)
  for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if products[i].price < products[j].price:

            products[i], products[j] = products[j], products[i]

for product in products:
    print(product)
  
else:
  print("Please enter valid option")

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


