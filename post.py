from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://sagnikuvce.firebaseio.com/', None)
result = firebase.patch('/users/9436492115/',{
    'Name' : 'Sagnik',
    'Address':'Ramnagar',
    'Phone_no':'9448608894',
    'Amount':'57895320'
    })
resultz = firebase.patch('/UVCE/9448608894',{
    'Name' : 'UVCE',
    'Phone_no' : '9448608894',
    'Balance' : '0'
    })
print(result)
