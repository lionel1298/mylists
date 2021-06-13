"""student=["maggy","muthoni","Rashida","Raphael"]
#mutable
print(student[0])
student[0]="cate"
print(student[0])
#duplicate
student.append("Rashida")
print(student[0])
#pop
student.pop(2)#specify the index
print(student)
#write a function that takes a list of exclusive prices and tax rates as parameters 
# calculate ans returnthe VAT amount of each inclusive prices of each value in the list
#return a list of inclusive prices and a list of VAT amount
"""
def calculate_VAT(excl,rate):
    incl=[]
    VAtamount=[]

    for x in excl:
        vat=x*rate
        VAtamount.append(vat)
        incl.append(x+vat)
    return[incl,VAtamount] 

print(calculate_VAT([100,200,50], 0.16))      


"""write a function takesa list of year of birth and the current year as cy as parameters
calculate and return and calculate and return a list containing age of each year of birth """

def user_age(cy,yob):
    age=[] 
    for x in yob:
        year_of_birth=cy-x
        age.append(year_of_birth)
    return[age]
print(user_age(2021,[1996,2005,2004]))  

