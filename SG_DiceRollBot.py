import praw
import SG_Repository
import SG_Messages
import pprint
import time
import ConfigParser
from random import randint
import SG_Utils

config = ConfigParser.ConfigParser()
config.read("settings.config")
config_header = "DiceRoll"

username = config.get("General", "username")
version = config.get("General", "version")
starting_balance = int(config.get("General", "starting_balance"))
max_bet = int(config.get(config_header, "bet_limit"))
payout_factor = int(config.get(config_header, "payout_factor"))
game_type = '6-9 Dice'

def format_wager_reply(username, wager_amount, roll_1, roll_2, total, outcome,
                       winnings, new_balance):
    return reply_messages.DICE_ROLL_SUCCESS_MSG.format(username,
                                                       wager_amount,
                                                       roll_1,
                                                       roll_2,
                                                       total,
                                                       outcome,
                                                       winnings,
                                                       new_balance)

def roll_die():
    roll = randint(1, 6)
    print("Die roll result: {}".format(roll))
    return roll

def parse_post_for_wager(post_body, player_balance):
    body_tokens = post_body.strip().split(' ')

    if str(body_tokens[0]) == 'wager' and (body_tokens[1].isnumeric() or body_tokens[1] == 'max'):
        if(body_tokens[1] == 'max'):
            return min(player_balance, max_bet)
        else:
            return int(body_tokens[1])

    return 0

def play_6_9(wager_amount):
    roll_1 = roll_die()
    roll_2 = roll_die()

    if (roll_1 + roll_2 == 6) or (roll_1 + roll_2 == 9) or (roll_1 + roll_2 == 3):
        outcome = SG_Repository.WagerOutcome.WIN
        winnings = wager_amount * payout_factor
    else:
        outcome = SG_Repository.WagerOutcome.LOSE
        winnings = 0

    wager_result = {'roll_1' : roll_1, 'roll_2' : roll_2, 'outcome' : outcome,
                    'winnings' : winnings, 'roll_total' : (roll_1 + roll_2)}

    print("6-9 wager result:")
    pprint.pprint(wager_result)

    return wager_result

# create our Reddit instance
c_id = config.get("General", "client_id")
c_secret = config.get("General", "client_secret")
user = config.get("General", "plain_username")
pw = config.get("General", "password")

reddit = praw.Reddit(
    client_id = c_id,
    client_secret = c_secret,
    username = user,
    password = pw,
    user_agent = 'Dealer bot v{} by /u/eganwall'.format(version)
)

# initialize our repository
sg_repo = SG_Repository.Repository()

# get our messaging classes
error_messages = SG_Messages.ErrorMessages
reply_messages = SG_Messages.ReplyMessages
constants = SG_Messages.MiscConstants

# set our subreddit so that we can do mod stuff like edit flairs
subreddit = reddit.subreddit('solutiongambling')
post_title = SG_Messages.PostBodies.DICEROLL_POST_TITLE
post_body = SG_Messages.PostBodies.DICEROLL_POST_BODY

while True:
    # get the Submission object for our dice roll thread
	threadID = config.get(config_header, "thread_id") 
    # get the Submission object for our poker thread
    submission = SG_ThreadManager.GetCurrentThread(threadID)
    if (submission is None):
        submission = SG_ThreadManager.CreateNewThread(subreddit, post_title, post_body)
        submissionID = submission.id
        SG_ThreadManager.HandleOldThread(threadID, submissionID)
        config.set(config_header, "thread_id", submissionID)
        with open('settings.config', 'w+') as configfile:
            config.write(configfile) # change config id

    submission.comment_sort = 'new'
    submission.comments.replace_more(limit = 0)
    for comment in list(submission.comments):
        # if we haven't processed this comment yet, make a new record for it and
        # process it
        if sg_repo.GET_COMMENT_BY_ID(comment.id) is None:
            sg_repo.INSERT_COMMENT_ID(comment.id)

            # if this player hasn't commented on the sub yet, make sure we
            # create a record of them, update their flair, and send them the
            # welcome PM
            if sg_repo.GET_PLAYER_BY_USERNAME(comment.author.name) is None:
                sg_repo.INSERT_PLAYER(comment.author.name, starting_balance)
                SG_Utils.update_player_flair(comment.author.name, starting_balance, '')
                reddit.redditor(comment.author.name).message('Welcome!',
                                                             reply_messages.NEW_PLAYER_WELCOME_MESSAGE.format(comment.author.name),
                                                             from_subreddit='/r/SolutionGambling')

            # get the player from the DB so we can validate their wager
            # and update their balance
            player = sg_repo.GET_PLAYER_BY_USERNAME(comment.author.name)

            # now process the comment - first we convert it to lower
            post_body_lower = comment.body.lower()
            print("Processing post body: ".format(post_body_lower))

            wager_amount = parse_post_for_wager(post_body_lower, player['balance'])
            print("Wager amount from post: {}".format(wager_amount))

            if wager_amount <= 0:
                print("Wager amount not valid")
                comment.reply(error_messages.DICE_ROLL_ERROR_MSG)
                continue

            if wager_amount > player['balance']:
                print("Player wagered more than their balance")
                comment.reply(error_messages.INSUFFICIENT_BALANCE_ERROR_MSG)
                continue

            if wager_amount > max_bet:
                print("Player wagered more than this game's max bet")
                comment.reply(error_messages.OVER_MAX_BET_ERROR_MSG.format(max_bet))
                continue

            wager_result = play_6_9(wager_amount)
            new_player_balance = player['balance'] - wager_amount + wager_result['winnings']

            sg_repo.INSERT_WAGER(player['username'], wager_result['outcome'],
                                 wager_amount, wager_result['winnings'], new_player_balance, game_type)
            SG_Utils.update_player_after_wager(player['username'], new_player_balance, player['flair_css_class'])

            reply = format_wager_reply(player['username'], wager_amount, wager_result['roll_1'],
                                       wager_result['roll_2'], wager_result['roll_total'],
                                       wager_result['outcome'], wager_result['winnings'],
                                       new_player_balance)

            print("Reply formatted:\n{}".format(reply))
            comment.reply(reply)

    print("---------------------- Processing finished - sleeping for 10 seconds...")
    time.sleep(10)

# players = sg_repo.GET_ALL_PLAYERS()
# for player in players:
#     pprint.pprint(player)
#     sg_repo.DELETE_PLAYER_BY_USERNAME(player['username'])