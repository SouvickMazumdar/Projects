# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:41:50 2021

@author: SOUVICK MAZUMDAR
"""

print("\t\tWelcome To Apple Grocery\t\t")
name=input("Dear customer Please Enter your name: ")
print(f"Hello {name}.\nApple's Grocery Shop provides all the necessary items. Hope so we can satisfy your need.")
product={'Soap':["Soap",{'Lux':["Lux",55],'Wildstone':["Wildstone",80],'Margo':["Margo",30],'Neem':["Neem",50]}],'Chocolate':['Chocolate',{'Diarymilk':["Diarymilk",100],'Milkybar':["Milkybar",50],'Perk':["Perk",30],'Munch':["Munch",10]}],'Pen':['Pen',{'Trimax':["Trimax",100],'Ballpen':["Ballpen",50],'Butterflow':["Butterflow",60],'Parker':["Parker",180]}],'Perfume':['Perfume',{'Parkavenue':["Parkavenue",120],'Secret':["Secret",90],'Spince':["Spince",150],'Axe':["Axe",200]}]}
p1=["1.Soap\t2.Chocolate\t3.Pen\t4.Perfume"]
b1={'Soap':"1.Lux\t\t\t55\n2.Wildstone\t\t\t80\n3.Margo\t\t\t30\n4.Neem\t\t\t55",'Chocolate':"1.Diarymilk\t\t\t100\n2.Milkybar\t\t\t50\n3.Perk\t\t\t30\n4.Munch\t\t\t10",'Pen':"1.Trimax\t\t\t100\n2.Ballpen\t\t\t50\n3.Butterflow\t\t\t60\n4.Parker\t\t\t180",'Perfume':"1.Parkavenue\t\t\t120\n2.Secret\t\t\t90\n3.Spince\t\t\t150\n4.Axe\t\t\t200"}
p=['0','Soap','Chocolate','Pen','Perfume']
b=[[],['','Lux','Wildstone','Margo','Neem'],['','Diarymilk','Milkybar','Perk','Munch'],['','Trimax','Ballpen','Butterflow','Parker'],['','Parkavenue','Secret','Spince','Axe']]
b2=['Lux','Wildstone','Margo','Neem','Diarymilk','Milkybar','Perk','Munch','Trimax','Ballpen','Butterflow','Parker','Parkavenue','Secret','Spince','Axe']
l=[]
add=0
while True:
    print("These are our products:\n",p1[0])
    choice=input("Enter your choice:").capitalize()
    if choice=='1' or choice=='2' or choice=='3' or choice=='4':
       choice=p[int(choice)] 
    if choice not in p:
        print ("Ooops!!!\nWrong choice. \nEnter again!!!")
        continue
    print("These are the brands with prize:\n",b1[choice])
    brand=input("Enter your brand:").capitalize()
    if brand=='1' or brand=='2' or brand=='3' or brand=='4':
       brand=b[p.index(choice)][int(brand)] 
    if brand not in b2:
        print ("Ooops!!!\nWrong brand. \nEnter from start!!!")
        continue
    l.append([product[choice][0],product[choice][1][brand][0],product[choice][1][brand][1]])
    add+=product[choice][1][brand][1]
    t=input("Enter Yes to continue else no to obtain the bill: ").capitalize()
    if t=="Yes":
        continue
    else:
        break
print(10*"\t","BILL")
print("Customer's Name",3*"\t","Product Name",4*"\t","Brand Name",4*"\t",f"Prize\n{name}")
for i in l:
   print(3*"\t",i[0],5*"\t",i[1],5*"\t",i[2])
print("\n",19*"\t","Total Sum: ",add)
print(9*"\t","Thank you")
    
    
    
    
    