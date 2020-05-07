import requests

def main():
    print('Hello World')
    response = requests.get('https://api.exchangeratesapi.io/latest')
    if response.status_code != 200:
        raise Exception('La richiesta non è andata a buon fine. Codice di errore',response.status_code)
    else:
        data = response.json()
        print('Status code', response.status_code)
        print('Contenuto JSON', data)


if __name__ == '__main__':
    main()