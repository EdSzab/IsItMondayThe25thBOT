# IsItFridayThe13thBot
# http://www.reddit.com/r/IsItFridayThe13th
# Copyright 2018 Ethan Nguyen, all rights reserved

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Syntax for secret.txt
# Line 1: Reddit Client ID
# Line 2: Reddit Client Secret
# Line 3: Reddit Username
# Line 4: Reddit Password

# Imports
import praw
import datetime
from time import sleep, time;

# Constants
ONE_DAY =           24 * 60 * 60
BOT_FRAME:          str = "Monday 25"
TIME_FRAME:         str = "Monday the 25th"
POST_TITLE:         str = ("Is it", TIME_FRAME + "?")

# Get secret data
secretFile = open("secret.txt").read().split("\n")

# Set secret data
reddit = praw.Reddit(
    user_agent = 'IsItMondayThe23rdBot',
    client_id = secretFile[0],
    client_secret = secretFile[1],
    username = secretFile[2],
    password = secretFile[3])
reddit.validate_on_submit = True
subreddit = reddit.subreddit('IsItMondayThe25th')

# Check Function
def Check():
    # Set day values
    today =         datetime.date.today()
    string =        today.strftime("%A %d")
    todoString =    today.strftime("%A, %B %d, %Y")

    # Find day
    Break = False
    incrementDays = 1
    while (Break == False):
        newDT = today + datetime.timedelta(days=incrementDays)
        stringThing = newDT.strftime("%A %d")
        if stringThing == BOT_FRAME:
            Break = True
        else: incrementDays += 1

    # Print Result
    print("Days left until next %s: %i" % (TIME_FRAME, incrementDays))

    # Execute Result
    if (string == BOT_FRAME):
        post = subreddit.submit(
            title = POST_TITLE,
            selftext = "Yes.\n---\n^(Today is " + todoString + ". The next " + TIME_FRAME + " is " + str(incrementDays) + " day\(s\) away. This message was posted by a bot. [source](https://github.com/etnguyen03/IsItFridayThe13thBot))")
        post.mod.flair(text = "Yes")
    else:
        post = subreddit.submit(
            title = POST_TITLE,
            selftext = "No.\n---\n^(Today is " + todoString + ". The next " + TIME_FRAME + " is " + str(incrementDays) + " day\(s\) away. This message was posted by a bot. This is NOT mine, if you are interested in any of this i reccomend checking out the [source](https://github.com/etnguyen03/IsItFridayThe13thBot))")
        post.mod.flair(text = "No")

# Main Loop
while True:
    Check()
    sleep(ONE_DAY)

