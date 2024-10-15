import requests
from libs import pyess

def get_raw_user_data(email:str):
    data = {"email": email}

    res = requests.post(f"https://service.blocksi.net/config/v2/api/users/license", json=data)

    if res.status_code != 200:
        return False
    else:
        return res.json()

def get_token(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["accessToken"]
    else:
        return False

def get_name(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return f'{raw_data["data"]["user"]["FirstName"]} {raw_data["data"]["user"]["LastName"]}'
    else:
        return False

def get_company_id(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["user"]["CompanyId"]
    else:
        return False

def get_google_id(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["user"]["GoogleUserId"]
    else:
        return False

def get_user_id(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["user"]["_id"]
    else:
        return False

def get_orgUnit(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["user"]["OrganizationUnit"]
    else:
        return False

def get_policy(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["user"]["Policy"]
    else:
        return False

def get_version(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["user"]["Version"]
    else:
        return False

def get_last_sync_id(email:str):
    raw_data = get_raw_user_data(email)
    if raw_data != False and raw_data.get("license") == True:
        return raw_data["data"]["user"]["LastSyncId"]
    else:
        return False