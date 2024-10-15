import requests
from libs import pyess

# Raw Data
def raw_policy_data(token:str, email:str):
    headers = {
        "Authorization": token
    }

    res = requests.get(f"https://service.blocksi.net/config/v2/api/policies/users/{email}/settings/true", headers=headers)

    if res.status_code != 200:
        return False
    else:
        return res.json()

# URL Blacklist
def get_blocked_urls(token:str, email:str):
    blocked_urls = []

    user_data = raw_policy_data(token, email)

    if user_data != False:
        blocked_urls_raw = user_data["data"]["bwList"]

        for i in blocked_urls_raw:
            if i["Action"] == "1":
                blocked_urls.append(i["Url"])

        return blocked_urls
    else:
        return False


def get_whitelisted_urls(token: str, email: str):
    whitelisted_urls = []

    user_data = raw_policy_data(token, email)

    if user_data != False:
        whitelisted_urls_raw = user_data["data"]["bwList"]

        for i in whitelisted_urls_raw:
            if i["Action"] == "0":
                whitelisted_urls.append(i["Url"])

        return whitelisted_urls
    else:
        return False

# Word Blocklist
def get_blocked_words(token: str, email: str):
    user_data = raw_policy_data(token, email)

    if user_data != False:
        whitelisted_urls_raw = user_data["data"]["contentFilter"]

        return whitelisted_urls_raw
    else:
        return False

# App Blocklist
def get_blocked_apps(token:str, email:str):
    blocked_apps = []

    user_data = raw_policy_data(token, email)

    if user_data != False:
        blocked_apps_raw = user_data["data"]["appFilter"]

        for i in blocked_apps_raw:
            if i["Action"] == "1":
                blocked_apps.append(i["Url"])

        return blocked_apps
    else:
        return False

def get_whitelisted_apps(token: str, email: str):
    whitelisted_apps = []

    user_data = raw_policy_data(token, email)

    if user_data != False:
        whitelisted_apps_raw = user_data["data"]["appFilter"]

        for i in whitelisted_apps_raw:
            if i["Action"] == "0":
                whitelisted_apps.append(i["Url"])

        return whitelisted_apps
    else:
        return False

def get_denied_page(token: str, email: str):
    user_data = raw_policy_data(token, email)

    if user_data != False:
        return user_data["data"]["accessDeniedPage"]
    else:
        return False