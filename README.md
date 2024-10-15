# BlocksiCrap
This is a python script to show how bad Blocksi is.\
To be honest there is some more stuff I can find if I look through the logs.\
Fun fact my high school thought it was a good idea to have the log files with, api tokens, api calls, and api json data in the C drive for anyone to see.\
So there goes the use of the 1000$ per year school monitering program.\
Also all you need is the targets email.\
Also yes I am writing this half asleep.

# Features
## User data grabbing
- First and Last name
- User Token
- Company ID
- Google ID
- Org Unit (Still trying to find out how to use this, but it is used by the api)
- Policy Name
- Blocksi Version
- Last Sync ID (No clue what this has)
## Policy Data
- Blocklist
  - URL Blocklist
  - App/Other URLs Blocklist
  - Word Blocklist
- Whitelist
  - URL Whitelist
  - App/Other URLs Whitelist
- You got blocked website grabber

# My half asleep description
So far everything I found was with the Blocksi local logs, I have some stuff being worked on, but I found it with GPT (No clue how but google dorks wouldn't work)\
Every URL is in the domain service.blocksi.net
## Current API Calls
Policy Data (Requires Token):\
https://service.blocksi.net/config/v2/api/policies/users/{email}/settings/true\
This is a GET request, with no params or data\

User Data:\
https://service.blocksi.net/config/v2/api/users/license\
This is a POST request with this being the json template {"email": email}

# Ideas
Using Org Unit with this URL, problem is that it gives a 500 code error. Only tested with POST and json data.\
https://service.blocksi.net/config/v2/api/users