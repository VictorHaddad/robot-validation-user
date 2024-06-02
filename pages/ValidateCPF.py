from settings import *
from wasabi import msg
import requests

def validation_cpf(data: dict) -> dict:
    """
    Valida um CPF (Cadastro de Pessoas Físicas) fornecido em um dicionário utilizando a API Invertexto.

    Argumento:
        data (dict): Dicionário contendo a chave `'cpf'` com o CPF a ser validado.

    Retorna:
        Um dicionário com as seguintes informações:
            * `error` (bool): Indica se ocorreu algum erro (True) ou não (False).
            * `message` (str): Mensagem de erro, caso `error` seja True.
            * `data` (dict, opcional): Dicionário contendo dados adicionais da resposta da API (pode ser nulo em caso de erro).
    """
    try:
        url = f"https://api.invertexto.com/v1/validator?token={TOKEN}&value={data['cpf']}&type=cpf"

        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        }

        response = requests.get(url, headers=headers)
        status = response.status_code
        
        if status != 200:
            return {'error': True, 'message': response.json(), 'data': None}

        data = response.json()

        if data['valid']:
            msg.good(data["formatted"])

        else:
            logger.info(f"Result: {data}")
            return {'error': True, 'message': None, 'data': None}
        
    except Exception as e:
        logger.error(e)
        return {'error': True,'message': str(e), 'data': None} 
    
    return {'error': False,'message':None, 'data': data}