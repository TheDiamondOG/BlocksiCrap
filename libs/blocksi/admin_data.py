import requests
from libs import pyess

# Raw Data
def get_raw_admin_data(email:str):
    res = requests.get(f"https://service.blocksi.net/config/getCompanyByDomain/{email}")

    if res.status_code != 200:
        return False
    else:
        return res.json()

def get_admin_id(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        admin_id = admin_data["adminAccount"]["_id"]

        return admin_id
    else:
        return False
    
def get_company_id(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        company_id = admin_data["adminAccount"]["CompanyId"]

        return company_id
    else:
        return False
    
def get_admin_name(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        name = f'{admin_data["adminAccount"]["FirstName"]} {admin_data["adminAccount"]["LastName"]}'

        return name
    else:
        return False
    
def get_admin_org(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        org = admin_data["adminAccount"]["OrganizationName"]

        return org
    else:
        return False
    
def get_admin_phone_number(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        org = admin_data["adminAccount"]["Phone"]

        return org
    else:
        return False
    
def get_admin_location_data(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        location = {
            "country": admin_data["adminAccount"]["Country"],
            "state": admin_data["adminAccount"]["State"],
            "city": admin_data["adminAccount"]["City"],
        }

        return location
    else:
        return False
    
def get_admin_ip(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        ip = admin_data["adminAccount"]["IP"]

        return ip
    else:
        return False
    
def get_chromebook_count(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        count = admin_data["adminAccount"]["Chromebooks"]

        return count
    else:
        return False
    
def get_admin_timezone(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        timezone = admin_data["adminAccount"]["TimezoneLoc"].replace("||", "/")

        return timezone
    else:
        return False
    
def get_admin_domains(email: str):
    admin_data = get_raw_admin_data(email)

    if admin_data != False:
        domains = admin_data["adminAccount"]["Domains"]

        if domains == []:
            domains = None

        return domains
    else:
        return False