import pyrebase
import joblib

firebaseConfig = joblib.load("firebase_config.priom")
# {'apiKey': 'AI9Hjo',
#         'authDomain': 'birth-regiapp.com',
#         'databaseURL': 'https://birthtdb.firebaseio.com',
#         'projectId': 'birth-r10b84',
#         'storageBucket': 'birth-t.com',
#         'messagingSenderId': '445',
#         'appId': '1:416024293945:web:da1a13e8',
#         'measurementId': 'G-GF0',
#         'serviceAccount': 'birth-registra-admins5e.json'}

def initialize():
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase




































