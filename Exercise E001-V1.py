class Category:          #Define Category Class
  def __init__(self, name, code, no_of_products=0):   #Initializing Category Class
    self.name = name                                  #Set name
    self.code = code                                  #Set Code
    self.no_of_products = []                          #Initialize list for products
  
  def calculate_no_of_products(self):
    return len(self.no_of_products)
  
  # String representation of Category
  def __repr__(self):
    return f"{self.name} (Code: {self.code}, Number of Products: {self.calculate_no_of_products()})"

def code(csearch):
  found = None
  for product in products:
    if product.code == csearch:
      found = product
      break
  if found:
    print(found)
  else:
    print("Please Enter Valid Code")
  

class Product:         # Define Product Class
  def __init__(self, name, code, category, price):  #Initializing Product Calass
    self.name = name
    self.code = code
    self.category = category
    self.price = price
    
    # add product category's list
    category.no_of_products.append(self)
  
  #String representation of Product  
  def __repr__(self):
    return f"{self.name} (code: {self.code}, Category: {self.category.name}, Price: {self.price})"
    
def sort_asc(ssearch):
    for i in range(len(products)):
      for j in range(i + 1, len(products)):
          if products[i].price > products[j].price:
              # Swap the products in the list if the price is lower
              products[i], products[j] = products[j], products[i]
    for product in products:
        print(product)
        
def sort_desc(ssearch):
    for i in range(len(products)):
      for j in range(i + 1, len(products)):
          if products[i].price < products[j].price:
              products[i], products[j] = products[j], products[i]
    for product in products:
        print(product)



# Define Category Objects
category1 = Category("Cross", "C001")
category2 = Category("Hatchback","H003")
category3 = Category("SUV","S009")


# Define Product Objects
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
# product11 = Product("YezdiHaatch" , "H006", category2, 100000)  put intentionally to show it works dynamically

products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]

# it will print all category with no_of_products in dynamic manner
print("Category Information:")
for category in [category1, category2, category3]:
    print(category)

# it will print all products in low to high and higher to lower order
ssearch = input("Do you wnat to  see based on price , Type LOW for low to high and Type HIGH For high to low: ")

# it will sort and print product in lower to higher order
if ssearch == 'low':
  sort_asc(ssearch)

# it will sort and print products in higher to lower order      
elif ssearch == 'high':
  sort_desc(ssearch)
      
# program will execute this statement if input is given incorrectly 
else:
  print("Please enter valid option")
  
  
# it will print product details based code given as input 
csearch = input("Please Enter the code for search: ")
code(csearch)


