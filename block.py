import praw
import urllib.request as ul
from bs4 import BeautifulSoup as soup
import re
import unicodedata

# Set this to a multiple of 10 to avoid duplicates, not that they should cause any issues.
up_to = 100  # Enter the Top X Users to Block
karma_type = 1  # Leave as 0 to block top Link Karma, 1 for Total Karma, 2 for Comment Karma

# Go to https://www.reddit.com/prefs/apps/, Scroll to bottom and select 'create another app...'
# Give app a name/description and enter redirect uri as 'http://www.example.com/unused/redirect/uri', this isn't used
# Click 'create app', then update the fields below with the needed information (Enter strings between "")
reddit = praw.Reddit(
    client_id="id",  # Replace id with string under 'personal use script' here
    client_secret="secret",  # Replace secret with string next to 'secret' here
    username="username",  # Replace username with your Reddit Username
    password="password",  # Replace password with your Reddit Password | Do NOT share this file with your password in :)
    user_agent="username_blocker"
)

# BELOW IS THE SCRIPT
# |
# | Step 1: Iterates through karmalb.com (up to the specified # of users) populating messy_usrlist
# | Step 2: Cleans messy_usrlist into a new list containing just the usernames called usrlist
# | Step 3: Uses praw reddit python library to block each user in usrlist
# |
# V

start = 0
if karma_type == 1:
    url = 'https://www.karmalb.com/ajax?key=totalkarma&offset='
if karma_type == 2:
    url = 'https://www.karmalb.com/ajax?key=commentkarma&offset='
else:
    url = 'https://www.karmalb.com/ajax?key=linkkarma&offset='
messy_usrlist = []

i = start
while i < up_to:
    req = ul.Request(url + str(i), headers={'User-Agent': 'Mozilla/5.0'})
    client = ul.urlopen(req)
    htmldata = client.read()
    client.close()
    pagesoup = soup(htmldata, "html.parser")
    itemlocator = pagesoup.findAll('a')

    for each in itemlocator:
        messy = each.text
        if not messy == 'Next':
            if not messy == 'Prev':
                messy_usrlist.append(messy)

    tmp = i
    i = i + 10
    print("Got users", tmp, "to", i)

print("")
print("Username collection completed. Cleaning list.")

usrlist = []

for each in messy_usrlist:
    regex = r'\n[0-9]+.\n'
    one = re.sub(regex, '', each, 0)
    two = unicodedata.normalize("NFKD", one)
    three = two.split(' ')
    usrlist.append(three[0])

print("List cleaned, starting to block users")
print("")

for user in usrlist:
    try:
        reddit.redditor(user).block()
        print(user, "has been Blocked")
    except:
        print("Failed to Block", user, "- User Suspended/Deleted, or Reddit Information Incorrect")

print("")
print("FINISHED, Script Blocked", usrlist.__len__(), "Usernames")
