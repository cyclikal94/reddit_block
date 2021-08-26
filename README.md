# reddit_block
Block top reddit users based on Link Karma, Total Karma or Comment Karma using https://www.karmalb.com/

Before running this python script ensure you have met the requirements by using 'pip install -r requirements.txt'

The script defaults to collecting the top 100 usernames for Link Karma from https://www.karmalb.com/. This can be changed by editing the up_to and karma_type variables per the commented lines. You will also need to provide the script with reddit information, see the comments for specifics / instructions.

# Installation
1. Download 'block.py' and 'requirements.txt'
2. Install https://www.python.org/downloads/
3. Open terminal to location of 'block.py' and 'requirements.txt'
4. Run 'pip install -r requirements.txt'
5. Edit 'block.py' to include the amount of top users to block, type of karma and reddit app/user credentials
6. Run 'python block.py'
