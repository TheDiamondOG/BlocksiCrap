import json
import os

from rich.console import Console
from libs import pyess, config
from libs.blocksi import user_data, policy_data

console = Console()

config_stuff = config.CoolConfig("config.json", {"email": "", "token": ""})

config_current = config_stuff.read()

email = config_current["email"]
token = config_current["token"]

def mm():
    pyess.clear()
    console.print("========================", style="blue")
    console.print("===== Blocksi Crap =====", style="blue")
    console.print("=== Proof of concept ===", style="blue")
    console.print("=== By TheDiamondOG. ===", style="blue")
    console.print("========================\n", style="blue")

    console.print("0. Exit", style="blue")
    console.print("1. Settings", style="blue")
    console.print("2. Policy Data", style="blue")
    console.print("3. User Data", style="blue")
    console.print("========================\n", style="blue")

    option = input("Option: ")

    option_hand(option, "mm")

def option_hand(option:str, page:str):
    pyess.clear()
    try:
        option = int(option)
    except Exception:
        console.print("Invalid Option", style="red")
        pyess.pause()

    if page == "mm":
        if option == 0:
            exit()
        elif option == 1:
            settings()
        elif option == 2:
            policy_data_menu()
        elif option == 3:
            user_data_menu()
        else:
            console.print("Invalid Option", style="red")
            pyess.pause()

def settings():
    while True:
        pyess.clear()
        global email, token
        console.print("0. Back", style="blue")
        console.print("1. Set Email", style="blue")
        console.print("2. Set Token", style="blue")
        console.print("3. User Dump", style="blue")
        option = input("Option: ")

        try:
            option = int(option)
        except Exception:
            console.print("Invalid Option", style="red")
            pyess.pause()

        pyess.clear()

        if option == 0:
            break
        elif option == 1:
            email = input("Email: ")
            config_current["email"] = email
            config_stuff.write(config_current)
        elif option == 2:
            console.print("Insert your token, or press enter to use the email to get your token.", style="blue")
            tokener = input("Token: ")
            if tokener.replace(" ", "") == "":
                if email != "":
                    token = user_data.get_token(email)
                else:
                    console.print("You need to set an email to automatically set a token", style="red")
            else:
                token = tokener
            config_current["token"] = token
            config_stuff.write(config_current)
        elif option == 3:
            console.print("Grabbing policy data", style="blue")
            policy_data_dump = policy_data.raw_policy_data(token, email)
            if policy_data_dump == False:
                console.print("Failed to grab policy data", style="red")
                pyess.pause()
                break
            console.print("Grabbed policy data", style="blue")

            console.print("Grabbing user data", style="blue")
            user_data_dump = user_data.get_raw_user_data(email)
            if user_data_dump == False:
                console.print("Failed to grab user data", style="red")
                pyess.pause()
                break
            console.print("Grabbed user data", style="blue")

            console.print(f"Checking if {os.getcwd()}/BlocksiDump/ exists", style="blue")
            if not os.path.exists("BlocksiDump"):
                console.print(f"Creating {os.getcwd()}/BlocksiDump/", style="blue")
                os.mkdir("BlocksiDump")

            console.print(f"Checking if {os.getcwd()}/BlocksiDump/{email} exists", style="blue")
            if not os.path.exists(f"BlocksiDump/{email}"):
                console.print(f"Creating {os.getcwd()}/BlocksiDump/{email}", style="blue")
                os.mkdir(f"BlocksiDump/{email}")

            console.print(f"Saving policy data", style="blue")
            with open(f"BlocksiDump/{email}/policy_data.json", "w+") as f:
                json.dump(policy_data_dump, f)
                console.print(f"Saved policy data", style="blue")

            console.print(f"Saving user data", style="blue")
            with open(f"BlocksiDump/{email}/user_data.json", "w+") as f:
                json.dump(user_data_dump, f)
                console.print(f"Saved user data", style="blue")
        else:
            console.print("Invalid Option", style="red")
            pyess.pause()

def policy_data_menu():
    while True:
        pyess.clear()
        console.print("===============================", style="blue")
        console.print("===== Blocksi Policy Data =====", style="blue")
        console.print("===============================\n", style="blue")
        console.print("0. Back", style="blue")
        console.print("1. Blacklists", style="blue")
        console.print("2. Whitelists", style="blue")
        console.print("3. Get Block Website", style="blue")
        console.print("===============================\n", style="blue")

        option = input("Option: ")
        pyess.clear()

        if option == "0":
            break
        if option == "1":
            console.print("==============================", style="blue")
            console.print("===== Blocksi Blacklists =====", style="blue")
            console.print("==============================\n", style="blue")
            console.print("0. Back", style="blue")
            console.print("1. URLs", style="blue")
            console.print("2. Words", style="blue")
            console.print("3. Apps", style="blue")
            console.print("==============================\n", style="blue")

            option = input("Option: ")
            pyess.clear()
            if option == "1":
                console.print("Blocked URLS:", style="blue")
                blocked_url = policy_data.get_blocked_urls(token, email)
                if blocked_url != False:
                    for i in blocked_url:
                        console.print(i, style="blue")
                else:
                    console.print("Failed lol", style="red")

            if option == "2":
                console.print("Blocked Words:", style="blue")
                blocked_words = policy_data.get_blocked_words(token, email)
                if blocked_words != False:
                    for i in blocked_words:
                        console.print(i, style="blue")
                else:
                    console.print("Failed lol", style="red")

            if option == "3":
                console.print("Blocked Apps/URLs:", style="blue")
                blocked_apps = policy_data.get_blocked_apps(token, email)
                if blocked_apps != False:
                    for i in blocked_apps:
                        console.print(i, style="blue")
                else:
                    console.print("Failed lol", style="red")
            pyess.pause()

        elif option == "2":
            console.print("==============================", style="blue")
            console.print("===== Blocksi Whitelists =====", style="blue")
            console.print("==============================\n", style="blue")
            console.print("0. Back", style="blue")
            console.print("1. URLs", style="blue")
            console.print("2. Apps", style="blue")
            console.print("==============================\n", style="blue")

            option = input("Option: ")
            pyess.clear()
            if option == "1":
                console.print("Allowed URLS:", style="blue")
                whitelisted_url = policy_data.get_whitelisted_urls(token, email)
                if whitelisted_url != False:
                    for i in whitelisted_url:
                        console.print(i, style="blue")
                else:
                    console.print("Failed lol", style="red")

            if option == "2":
                console.print("Allowed Apps/URLs:", style="blue")
                whitelisted_apps = policy_data.get_whitelisted_apps(token, email)
                if whitelisted_apps != False:
                    for i in whitelisted_apps:
                        console.print(i, style="blue")
                else:
                    console.print("Failed lol", style="red")
            pyess.pause()
        elif option == "3":
            console.print(f"Block Website URL: {policy_data.get_denied_page(token, email)}", style="blue")
            pyess.pause()



def user_data_menu():
    while True:
        pyess.clear()
        console.print("=============================", style="blue")
        console.print("===== Blocksi User Data =====", style="blue")
        console.print("=============================\n", style="blue")
        console.print("0. Back", style="blue")
        console.print("1. Get Token", style="blue")
        console.print("2. Get Name", style="blue")
        console.print("3. Get Company ID", style="blue")
        console.print("4. Get Google ID", style="blue")
        console.print("5. Get Organization Unit (Debugish)", style="blue")
        console.print("6. Get Policy", style="blue")
        console.print("7. Get Version", style="blue")
        console.print("8. Get Last Sync ID", style="blue")
        console.print("=============================\n", style="blue")

        option = input("Option: ")
        pyess.clear()
        try:
            option = int(option)
        except Exception:
            console.print("Invalid Option", style="red")
            pyess.pause()

        if option == 0:
            break
        elif option == 1:
            console.print(f"User Token: {user_data.get_token(email)}", style="blue")
            pyess.pause()
        elif option == 2:
            console.print(f"Name: {user_data.get_name(email)}", style="blue")
            pyess.pause()
        elif option == 3:
            console.print(f"Company ID: {user_data.get_company_id(email)}", style="blue")
            pyess.pause()
        elif option == 4:
            console.print(f"Google ID: {user_data.get_google_id(email)}", style="blue")
            pyess.pause()
        elif option == 5:
            console.print(f"Org Unit: {user_data.get_orgUnit(email)}", style="blue")
            pyess.pause()
        elif option == 6:
            console.print(f"Policy: {user_data.get_policy(email)}", style="blue")
            pyess.pause()
        elif option == 7:
            console.print(f"Version: {user_data.get_version(email)}", style="blue")
            pyess.pause()
        elif option == 8:
            console.print(f"Last Sync ID: {user_data.get_last_sync_id(email)}", style="blue")
            pyess.pause()
        else:
            console.print("Invalid Option", style="red")
            pyess.pause()

while True:
    mm()