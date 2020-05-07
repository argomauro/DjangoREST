import requests

def main():
    prima_valuta = input('Inserisci la prima valuta: ')
    seconda_valuta = input('Inserisci la seconda valuta: ')
    payload = {'base': prima_valuta, 'symbols':seconda_valuta}
    response = requests.get('https://api.exchangeratesapi.io/latest',
                            params=payload)
    if response.status_code != 200:
        raise Exception('La richiesta non è andata a buon fine. Codice di errore',response.status_code)
    else:
        data = response.json()
        tasso_di_cambio = data['rates'][seconda_valuta]
        data_di_cambio = data['date']
        print('Status code', response.status_code)
        print('Contenuto JSON', data)
        print('Tasso di cambio estratto: ', tasso_di_cambio)
        print('Data di cambio', data_di_cambio)
        print(f'1 {prima_valuta} corrisponde a {tasso_di_cambio} {seconda_valuta}')


if __name__ == '__main__':
    main()