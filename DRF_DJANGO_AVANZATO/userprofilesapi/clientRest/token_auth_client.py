import requests

def clientGetToken():
    credentials = {'username':'argomauro','password':'gnometto'}
    response = requests.post('http://localhost:8080/api/rest-auth/login/', data=credentials)
    print('Risposta Status: ', response.status_code)
    response_data = response.json()
    print('Risposta Dati: ', response_data)
    
    
def clientGetListToken():
    token_header = 'token cf073c821450254312aec4e716783a3f42bc5314'
    headers = {'Authorization':token_header}

    response = requests.get('http://localhost:8080/api/profile/list/', headers=headers)
    print('Risposta Status: ', response.status_code)
    response_data = response.json()
    print('Risposta Dati: ', response_data)
    
if __name__ == '__main__':
    clientGetListToken()
