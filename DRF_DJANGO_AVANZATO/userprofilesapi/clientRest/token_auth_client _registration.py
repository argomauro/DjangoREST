import requests

def clientRegistration():
    data = {'username':'restoken','password1':'gnometto','password2':'gnometto', 'email':'m@a.it'}
    response = requests.post('http://localhost:8080/api/rest-auth/registration/', data=data)
    print('Risposta Status: ', response.status_code)
    response_data = response.json()
    print('Risposta Dati: ', response_data)
    
    

    
if __name__ == '__main__':
    clientRegistration()
