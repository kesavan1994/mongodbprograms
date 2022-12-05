
import re
reg=re.compile(r'([a-zA-Z],{1,})*([0-9.-_])*[a-zA-Z0-9]+@([a-zA-Z]{2,5})+[.a-zA-Z]+')
def create():
  Name=input("Enter the Name: ")
  Phno=input("Enter the Phno: ")
  Mail_id=input("Enter the Mail-id: ")

  if re.fullmatch(reg,Mail_id):
    phoneNumber={"Name":Name,"Phno":Phno,"Mail_id":Mail_id}
    records.insert_one(phoneNumber)

    print("Email is Valid")
    
  else:
    print("Email is Invalid") 
    
   

#Search
def search():
  Nam=input("Enter the Search Name Or Phno: ")
  a={"$or":[{"Name":Nam},{"Phno":Nam}]}
  for i in records.find(a):
    print(i)
def delete():
  Nam=input("Enter the Delete  Name Or Phno: ")
  a={"$or":[{"Name":Nam},{"Phno":Nam}]}
  records.delete_one(a)
#Update/Edit
def update():
  Nam=input("Enter the Name or Phno or Mail-id")# Give Finding Values
  Key=input("Enter the Key to Update: ")
  Value=input("Enter the Value to Update: ")
  a={"$or":[{"Name":Nam},{"Phno":Nam},{"Mail_id":Nam}]}
  b={"$set":{Key:Value}}
  records.update_one(a,b)
def display():
  for i in records.find():
    print(i)

if __name__=="__main__":
    print("""please select one option :
              
              1.create
              2.search
              3.delete
              4.update
              5.display
          
          """)
    option = int(input("Enter your option: "))
    if option==1:
        create()
    elif option==2:
        search()
    elif option==3:
        delete()
    elif option==4:
        update()  
    elif option==5:
        display()      
    else:
        print("invalid option")
 