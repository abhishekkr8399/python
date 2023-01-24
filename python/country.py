class Country:
 def __init__(self,name,capital,population):
  self.name=name
  self.capital=capital
  self.population=population
 def printDetails(self):
  print("Country:", self.name, " Capital:", self.capital, " Population:", self.population)
country=[]
while True:
 print("\n1.Add country 2.Display details 3.Display highest population 4.Exit");
 ch=int(input("Enter your choice : "))
 if ch==1:
  name=input("Enter country name : ")
  cap=input("Enter capital : ")
  pop=int(input("Enter the population : "))
  country.append(Country(name,cap,pop))
 elif ch==2:
  name=input("Enter country name : ")
  found=False
  for c in country:
   if c.name==name:
     c.printDetails()
     found=True
     break
  if found==False:
   print("Country not found!")
 elif ch==3:
  if len(country)==0:
   print("List doesnt contain any country details.")
   continue
  high=0
  for c in country: #to obtain highest population
   if c.population>high:
     high=c.population
  for c in country: #To get all contries which have highest population
       if c.population==high:
         c.printDetails()
 elif ch==4:
  break
 else:
  print("Invalid choice!")
