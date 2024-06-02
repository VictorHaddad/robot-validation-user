from playwright.sync_api import Playwright, sync_playwright
from pages.RegisterPage import RegisterPage
from pages.GeneratorCPF import generator_cpf
from pages.ValidateCPF import validation_cpf

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    login_user = RegisterPage(page)

    new_people = generator_cpf()
    if new_people["error"]:
        return new_people
    
    validate_people = validation_cpf(new_people['data'])
    if validate_people["error"]:
        return validate_people

    register_people = login_user.register(new_people['data'])
    if register_people["error"]:
        return register_people
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)