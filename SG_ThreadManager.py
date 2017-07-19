import praw
from datetime import datetime
import pytz
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("settings.config")

date = config.get("General", "date")

# create our Reddit instance
c_id = config.get("General", "client_id")
c_secret = config.get("General", "client_secret")
user = config.get("General", "plain_username")
pw = config.get("General", "password")
version = config.get("General", "version")

reddit = praw.Reddit(
        client_id = c_id,
        client_secret = c_secret,
        username = user,
        password = pw,
        user_agent = 'Dealer bot v{} by /u/eganwall'.format(version)
        )

def GetCurrentThread(threadID):
    # Check threadID date against current date
    # if same, return ID
    # else, return None
    today = GetTodayFormatted()
    thread = reddit.submission(id=threadID)
    threadTitle = thread.title
    if (GetDateFromTitle(threadTitle) == today):
        return thread
    else:
        return None
    
def CreateNewThread(subreddit, postTitle, postBody):
    today = GetTodayFormatted()
    postTitle = today + ' ' + postTitle
    newThread = subreddit.submit(postTitle, selftext=postBody)
    return newThread

def HandleOldThread(oldThreadID, newThreadID):
    oldThread = reddit.submission(id=oldThreadID)
    newPostBody = 'This thread is closed. Please visit https://redd.it/'+newThreadID+' to continue playing'
    if (oldThread != None):
        oldThread.edit(newPostBody)
        oldThread.mod.lock()

def GetDateFromTitle(title):
    return title.split(' ')[0]

def GetTodayFormatted():
    return datetime.now(pytz.timezone('US/Pacific')).strftime('%m.%d')
