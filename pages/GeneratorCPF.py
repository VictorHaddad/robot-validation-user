import requests
from settings import *
def generator_cpf() -> dict:
    """
    Gera um CPF (Cadastro de Pessoas Físicas) simulado utilizando a API Invertexto.

    Retorna:
        Um dicionário com as seguintes informações:
            * `error` (bool): Indica se ocorreu algum erro (True) ou não (False).
            * `message` (str): Mensagem de erro, caso `error` seja True.
            * `data` (dict): Dicionário contendo os dados do CPF simulado (se a requisição foi bem-sucedida).
    """
    try:
        url = f"https://api.invertexto.com/v1/faker?token={TOKEN}&locale=pt_BR"

        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        }

        response = requests.get(url, headers=headers)
        status = response.status_code

        if status != 200:
            return {'error': True,'message': response.json(), 'data': None}
        
        data = response.json()

    except Exception as e:
        logger.error(e)
        return {'error': True,'message': str(e), 'data': None}

    return {'error': False,'message': None, 'data': data}