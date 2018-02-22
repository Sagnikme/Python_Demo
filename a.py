from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://sagnikuvce.firebaseio.com/', None)
g = input('Enter your ID Number:   ' )

f = str(g)
a = f + '/' + 'Name'
b = f + '/' + 'Phone_no'
c = f + '/' + 'Address'
d = f + '/' + 'Amount'
e = f + '/' + 'Money'


name = firebase.get('/users',a)
print('Hello', name)
phone = firebase.get('/users',b)
add = firebase.get('/users',c)

#############################################

amount = firebase.get('/users',d)
sree = int(amount)
payment = input('Enter the Payable Amount:   ')
pay = int(payment)
to = int(pay)
hi = sree - pay

##############################################
balance = firebase.get('/uvce','9448608894/Money')
bal = int(balance)
ji = bal + to
#print (ji)


#print (name)
#print (phone)
#print (add)
#print (amount)
#print (sree - payment)
shit = firebase.put('/users',g,{
    'Name': name,
    'Phone_no' : phone,
    'Address' : add,
    'Amount' : hi
    })
ass = firebase.put('/uvce','9448608894',{
    'Name' : 'UVCE',
    'Phone_no': '9448608894',
    'Money' : ji
    
    })
#print(ass)
print('Thank You for payment :) Have an awesome day', name)
