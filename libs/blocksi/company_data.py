import requests
from libs import pyess

# Raw Data
def get_raw_company_data(email:str):
    res = requests.get(f"https://service.blocksi.net/config/getCompanyByDomain/{email}")

    if res.status_code != 200:
        return False
    else:
        return res.json()