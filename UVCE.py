from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://sagnikuvce.firebaseio.com/', None)
resultz = firebase.patch('/uvce/9448608894',{
    'Name' : 'UVCE',
    'Phone_no' : '9448608894',
    'Money' : '1'
    })
print(resultz)
