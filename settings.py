from dotenv import dotenv_values
import logging

logging.basicConfig(
    encoding= 'utf-8',
    filename='log.log',
    format='%(asctime)s [%(module)s] %(levelname)s: %(message)s', 
    datefmt='%d-%m-%Y %H:%M', 
    level=logging.INFO,
)

logger = logging.getLogger("log.log")
config = dotenv_values()

MONGO_HOST = config.get("HOST_MONGO")
MONGO_DATABASE = config.get("DATABASE_MONGO")
TOKEN = config.get("TOKEN_VALIDATION_CPF")