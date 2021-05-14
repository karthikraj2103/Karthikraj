import fpdf
import random
f=print("WELCOME TO LARGEST VACCINE DRIVE")
name=input("enter your name")
age=int(input("enter your age"))
dob= str(input('Enter date(dd-mm-yyyy)'))
print("select the photo id proff")
phto_proof=int(input("type 1 for aadhaar card\n type 2 for pan card \n type 3 for driving lincease"))
if(phto_proof==1):
     ac=int(input("enter aadhaar card number"))
elif (phto_proof==2):
    ac=int(input("enter pan card number"))
elif (phto_proof==3):
    ac=int(input("enter  driving licence number"))
else:
    print("invalid proof")
if(age>=18):
    print("Your are eligilble for getting vaccination")
    r_num= random.randint(0,1000)
else:
    print("you are not eligible to get vacination")
c_s=1000
c_v=2
print("Choose a vacine to wear")
ty =int(input("type 1 for covaxin\nenter 2 to for covid shield"))
if(ty==1):
    print("Thankyou for choicing Covidshield")
    c_s=c_s-1
    if(c_s==0):
        print("Sorry the particular vaccine which you have selected is out of stock \nWe will inform you whenever the stock is avaiable")
elif(ty==2):
    print("Thankyou for choicing Covaxin")
    c_v=c_v-1
    if(c_v==0):
        print("Sorry the particular vaccine which you have selected is out of stock \nWe will inform you whenever the stock is avaiable")
else:
    print("Please select a correct option")
print(c_s)
print(c_v)
# data=[name,age,dob,ac,r_num]
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt = "WELCOME TO LARGEST VACCINE DRIVE",
         ln = 1, align = 'C')
pdf.cell(100,5,txt="name:",ln=2,align='L')
pdf.write(5,"name:",name)
pdf.output("exam.pdf")







