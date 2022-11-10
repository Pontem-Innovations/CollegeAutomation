import logging
import logging.handlers
import os
import json
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    

    r = requests.get('https://crdhaportal.azurewebsites.net/automation/renewal/DwDpmP7ClwXz3B6b4uQb')
    #r = requests.get('https://crdhaportal.azurewebsites.net/automation/renewal/DwDpmP7ClwXz3B6b4uQb')
    #r = requests.get('http://localhost:5005/automation/renewal/DwDpmP7ClwXz3B6b4uQb')
    
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://crdhaportal.azurewebsites.net/automation/removal/DwDpmP7ClwXz3B6b4uQb')
    #r = requests.get('https://crdhaportal.azurewebsites.net/automation/removal/DwDpmP7ClwXz3B6b4uQb')
    #r = requests.get('http://localhost:5005/automation/removal/DwDpmP7ClwXz3B6b4uQb')
    
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://cdhnsportal.azurewebsites.net/automation/renewal/DwDpmP7ClwXz3B6b4uQb')
    #r = requests.get('http://localhost:5005/automation/renewal/DwDpmP7ClwXz3B6b4uQb')
    
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://cdhnsportal.azurewebsites.net/automation/removal/DwDpmP7ClwXz3B6b4uQb')
    #r = requests.get('http://localhost:5005/automation/removal/DwDpmP7ClwXz3B6b4uQb')
    
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)
    
    print('hello')
