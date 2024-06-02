from playwright.sync_api import Page, expect
from locators.locators import LocatorsPage
from settings import *

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = LocatorsPage()

    def register(self, data: dict) -> dict:
        """
        Tenta registrar um novo usuário no Discord usando o Playwright.

        Esta função simula a interação do usuário com o formulário de registro do Discord
        preenchendo o e-mail, nome de usuário, senha e data de nascimento fornecidos.

        Argumentos:
            data (dict): Dicionário contendo informações de registro do usuário.
                * `email` (str): Endereço de e-mail do usuário.
                * `name` (str): Nome completo do usuário.
                * `username` (str): Nome de usuário desejado para o Discord.
                * `password` (str): Senha escolhida pelo usuário.
                * `birth_date` (str, formato AAAA-MM-DD): Data de nascimento do usuário.

        Retorna:
            dict: Dicionário indicando sucesso ou falha.
                * `error` (bool): True se ocorreu um erro, False caso contrário.
                * `message` (str, opcional): Mensagem de erro se `error` for True.

        Levanta:
            PlaywrightException: Se ocorrer um erro inesperado durante a interação com o navegador.
        """
        try:
            self.page.goto("https://discord.com/register", wait_until="load")

            self.page.get_by_label("E-mail*").type(data['email'], delay=200)
            
            self.page.get_by_label("Nome exibido").type(data['name'], delay=200)
            self.page.get_by_label("Nome de usuário*").type(data['username'], delay=200)
            self.page.get_by_label("Senha*").type(data['password'], delay=200)

            birth_date = data['birth_date'].split("-")

            self.page.get_by_label("Dia").type(birth_date[1], delay=150)
            self.page.get_by_label("Mês").type("janeiro", delay=100)
            self.page.get_by_label("Ano").type(birth_date[0], delay=100)
        
        except Exception as e:
            logger.error(e)
            return {'error': True, 'message': str(e), 'data': None}
        
        return {'error': False, 'message': None, 'data': None}