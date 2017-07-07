<<<<<<< HEAD
class ErrorMessages:
    DICE_ROLL_ERROR_MSG = """Hello! Please place your wager in the form of a 
top-level comment:

`wager {NUMBER}`

where 0 < {NUMBER} <= your balance.

Thanks, and good luck!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

    POKER_ERROR_MSG = """Hello! Please place your wager in the form of a 
top-level comment:

`wager {NUMBER}`

where 0 < {NUMBER} <= your balance.

Thanks, and good luck!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

    ROULETTE_WAGER_FORMAT_ERROR_MSG = """Wager could not be made: [*{}*] Reason: __invalid format__.
Please refer to the body of the OP for more info."""

    ROULETTE_WAGER_INSUFFICIENT_BALANCE_ERROR_MSG = """Wager could not be made: [*{}*] Reason:
__Insufficient balance__. Please refer to the body of the OP for more info."""

    ROULETTE_WAGER_OVER_MAX_ERROR_MSG = """Wager could not be made: [*{}*] Reason:
    __Wager was over maximum__. Please refer to the body of the OP for more info."""

    INSUFFICIENT_BALANCE_ERROR_MSG = """Hello! It looks like you're trying to place
a wager for an amount greater than your balance. Please make a more reasonable bet!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

    OVER_MAX_BET_ERROR_MSG = """Hello! It looks like you're trying to place
a wager for an amount greater than the maximum bet for this game (__{:,}__).
Please adjust your wager amount!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

    FLAIR_SHOP_INSUFFICIENT_BALANCE_ERROR_MSG = """/u/{},

It appears that you are attempting to purchase a __Level {}__ flair, which costs {:,}.

Your current balance is {:,}, which is insufficient for this purchase. Please try again when you have the points!"""

    FLAIR_SHOP_ALREADY_MAX_LEVEL = """/u/{},

It appears you are already at the highest flair level! Congratulations!"""

    COIN_FLIP_NO_BALANCE_ERROR_MSG = """/u/{},

It appears that you have no points with which to wager! Please message the moderators
and they will deposit the starting amount into your bankroll so you can get back on 
your feet.

Thanks, and good luck!"""

    COIN_FLIP_ERROR_MSG = """/u/{},

Please place your bet by posting a comment like this: 

    wager

Thanks, and good luck!"""

class ReplyMessages:
    NEW_PLAYER_WELCOME_MESSAGE = """Hello, /u/{}! Welcome to /r/SolutionGambling -
where you can build a meaningless fortune of imaginary points one wager at a time!
It seems that you are a new player with us, so we've gone ahead and made an initial 
deposit of 500 points. Knock yourself out, kid!"""

    DICE_ROLL_SUCCESS_MSG = """/u/{},

Thanks for placing your bet of {:,}! Here are your results:

* Roll 1: {}

* Roll 2: {}

* **Total: {}**

**Your outcome is: {}**

Your winnings are {:,}, and your new balance is {:,}.

Thank you for playing - please come see us again!"""

    POKER_SUCCESS_MSG = """/u/{},

Thanks for placing your bet of {:,}! Here are your results:

Your 2-card poker hand is

{}

&nbsp;

The 5 cards on the board are

{}

&nbsp;

**Your outcome is: {}**

Your winnings are {:,}, and your new balance is {:,}.

Thank you for playing - please come see us again!"""

    PLAYER_LEADERBOARD_TEMPLATE_MSG = """**Here is the overall balance leaderboard:**
    
Rank|Player| Balance 
---------|---------|---------:
1|/u/{} | __{:,}__
2|/u/{} | __{:,}__
3|/u/{} | __{:,}__
4|/u/{} | __{:,}__
5|/u/{} | __{:,}__
6|/u/{} | __{:,}__
7|/u/{} | __{:,}__
8|/u/{} | __{:,}__
9|/u/{} | __{:,}__
10|/u/{} | __{:,}__"""

    WINS_LEADERBOARD_TEMPLATE_MSG = """**Here is the WINS leaderboard:**
    
Rank|Player|Wager Amount|Winnings|Game Type
---------|---------|----------|----------|----------
1|/u/{} | {:,} | __{:,}__ | {}
2|/u/{} | {:,} | __{:,}__ | {}
3|/u/{} | {:,} | __{:,}__ | {}
4|/u/{} | {:,} | __{:,}__ | {}
5|/u/{} | {:,} | __{:,}__ | {}
6|/u/{} | {:,} | __{:,}__ | {}
7|/u/{} | {:,} | __{:,}__ | {}
8|/u/{} | {:,} | __{:,}__ | {}
9|/u/{} | {:,} | __{:,}__ | {}
10|/u/{} | {:,} | __{:,}__ | {}"""

    LOSSES_LEADERBOARD_TEMPLATE_MSG = """**Here is the LOSSES leaderboard:**

    Rank|Player|Amount Lost|Game Type
    ---------|---------|----------|----------
    1|/u/{} | __{:,}__ | {}
    2|/u/{} | __{:,}__ | {}
    3|/u/{} | __{:,}__ | {}
    4|/u/{} | __{:,}__ | {}
    5|/u/{} | __{:,}__ | {}
    6|/u/{} | __{:,}__ | {}
    7|/u/{} | __{:,}__ | {}
    8|/u/{} | __{:,}__ | {}
    9|/u/{} | __{:,}__ | {}
    10|/u/{} | __{:,}__ | {}"""

    LEADERBOARD_FULL_POST_TEMPLATE_MSG = """# Here are the leaderboards for /r/SolutionGambling!

*There are {} players in total.*

{}

&nbsp;

&nbsp;

{}

&nbsp;

&nbsp;

{}

Good luck, all!"""

    ROULETTE_INDIVIDUAL_WAGER_TEMPLATE_MSG = """Wager {}: {:,} on {}

Your outcome is : **{}**

Your winnings for this bet are {:,}

&nbsp;

"""

    ROULETTE_REPLY_WRAPPER_TEMPLATE_MSG = """/u/{},

## The roulette spin results are : ***{} {}***!

Here are your wager results:

&nbsp;

{}

&nbsp;

Your __wagers__ total {:,}

Your __winnings__  total {:,}

Your __overall profit__ is {:,}, and your __new balance__ is {:,}.

Thanks for your wager - good luck!"""

    FLAIR_SHOP_SUCCESS_MSG = """/u/{},

Your purchase of __Level {}__ flair for {:,} was successful! 

Your new balance is __{:,}__.

Enjoy!"""

    COIN_FLIP_WIN_MSG = """/u/{},

You've risked your whole balance ({:,}) on this coin flip, and the result is...

#__{}__!

Congratulations! Your new balance is {:,}. Good luck!"""

    COIN_FLIP_LOSE_MSG = """/u/{},

You've risked your whole balance ({:,}) on this coin flip, and the result is...

#__{}__!

Unfortunately, you've lost. You'll have some points deposited by /u/eganwall whenever he
reads this. Thanks for playing, and better luck next time!"""

class MiscMessages:
    SUBSCRIBER_ANNOUNCEMENT_MSG_TEMPLATE = """Hello, /u/{}!

{}

Thanks for reading and playing - good luck!"""

class MiscConstants:
    FLAIR_TIER_TITLES = {
        "" : "",
        "lvl1" : "Novice: ",
        "lvl2" : "Social Gambler: ",
        "lvl3" : "Addict: ",
        "lvl4" : "Grinder: ",
        "lvl5" : "Professional: ",
        "lvl6" : "High Roller: ",
        "lvl7" : "Whale: ",
    }
=======
class ErrorMessages:
    DICE_ROLL_ERROR_MSG = """Hello! Please place your wager in the form of a 
top-level comment:

`wager {NUMBER}`

where 0 < {NUMBER} <= your balance.

Thanks, and good luck!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

    POKER_ERROR_MSG = """Hello! Please place your wager in the form of a 
top-level comment:

`wager {NUMBER}`

where 0 < {NUMBER} <= your balance.

Thanks, and good luck!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

    ROULETTE_WAGER_FORMAT_ERROR_MSG = """Wager could not be made: [*{}*] Reason: __invalid format__.
Please refer to the body of the OP for more info."""

    ROULETTE_WAGER_INSUFFICIENT_BALANCE_ERROR_MSG = """Wager could not be made: [*{}*] Reason:
__Insufficient balance__. Please refer to the body of the OP for more info."""

    ROULETTE_WAGER_OVER_MAX_ERROR_MSG = """Wager could not be made: [*{}*] Reason:
    __Wager was over maximum__. Please refer to the body of the OP for more info."""

    INSUFFICIENT_BALANCE_ERROR_MSG = """Hello! It looks like you're trying to place
a wager for an amount greater than your balance. Please make a more reasonable bet!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

    OVER_MAX_BET_ERROR_MSG = """Hello! It looks like you're trying to place
a wager for an amount greater than the maximum bet for this game (__{:,}__).
Please adjust your wager amount!

^^If ^^you ^^have ^^any ^^issues, ^^please ^^PM ^^/u/eganwall ^^or ^^post ^^on ^^this ^^sub!*"""

class ReplyMessages:
    NEW_PLAYER_WELCOME_MESSAGE = """Hello, /u/{}! Welcome to /r/SolutionGambling -
where you can build a meaningless fortune of imaginary points one wager at a time!
It seems that you are a new player with us, so we've gone ahead and made an initial 
deposit of 500 points. Knock yourself out, kid!"""

    DICE_ROLL_SUCCESS_MSG = """/u/{},

Thanks for placing your bet of {:,}! Here are your results:

* Roll 1: {}

* Roll 2: {}

* **Total: {}**

**Your outcome is: {}**

Your winnings are {:,}, and your new balance is {:,}.

Thank you for playing - please come see us again!"""

    POKER_SUCCESS_MSG = """/u/{},

Thanks for placing your bet of {:,}! Here are your results:

Your 2-card poker hand is

{}

&nbsp;

The 5 cards on the board are

{}

&nbsp;

**Your outcome is: {}**

Your winnings are {:,}, and your new balance is {:,}.

Thank you for playing - please come see us again!"""

    PLAYER_LEADERBOARD_TEMPLATE_MSG = """**Here is the overall balance leaderboard:**
    
Rank|Player| Balance 
---------|---------|---------:
1|/u/{} | __{:,}__
2|/u/{} | __{:,}__
3|/u/{} | __{:,}__
4|/u/{} | __{:,}__
5|/u/{} | __{:,}__
6|/u/{} | __{:,}__
7|/u/{} | __{:,}__
8|/u/{} | __{:,}__
9|/u/{} | __{:,}__
10|/u/{} | __{:,}__"""

    WINS_LEADERBOARD_TEMPLATE_MSG = """**Here is the WINS leaderboard:**
    
Rank|Player|Wager Amount|Winnings|Game Type
---------|---------|----------|----------|----------
1|/u/{} | {:,} | __{:,}__ | {}
2|/u/{} | {:,} | __{:,}__ | {}
3|/u/{} | {:,} | __{:,}__ | {}
4|/u/{} | {:,} | __{:,}__ | {}
5|/u/{} | {:,} | __{:,}__ | {}
6|/u/{} | {:,} | __{:,}__ | {}
7|/u/{} | {:,} | __{:,}__ | {}
8|/u/{} | {:,} | __{:,}__ | {}
9|/u/{} | {:,} | __{:,}__ | {}
10|/u/{} | {:,} | __{:,}__ | {}"""

    LOSSES_LEADERBOARD_TEMPLATE_MSG = """**Here is the LOSSES leaderboard:**

    Rank|Player|Amount Lost|Game Type
    ---------|---------|----------|----------
    1|/u/{} | __{:,}__ | {}
    2|/u/{} | __{:,}__ | {}
    3|/u/{} | __{:,}__ | {}
    4|/u/{} | __{:,}__ | {}
    5|/u/{} | __{:,}__ | {}
    6|/u/{} | __{:,}__ | {}
    7|/u/{} | __{:,}__ | {}
    8|/u/{} | __{:,}__ | {}
    9|/u/{} | __{:,}__ | {}
    10|/u/{} | __{:,}__ | {}"""

    LEADERBOARD_FULL_POST_TEMPLATE_MSG = """# Here are the leaderboards for /r/SolutionGambling!

*There are {} players in total.*

{}

&nbsp;

&nbsp;

{}

&nbsp;

&nbsp;

{}

Good luck, all!"""

    ROULETTE_INDIVIDUAL_WAGER_TEMPLATE_MSG = """Wager {}: {:,} on {}

Your outcome is : **{}**

Your winnings for this bet are {:,}

&nbsp;

"""

    ROULETTE_REPLY_WRAPPER_TEMPLATE_MSG = """/u/{},

## The roulette spin results are : ***{} {}***!

Here are your wager results:

&nbsp;

{}

&nbsp;

Your __wagers__ total {:,}

Your __winnings__  total {:,}

Your __overall profit__ is {:,}, and your __new balance__ is {:,}.

Thanks for your wager - good luck!"""

class MiscMessages:
    SUBSCRIBER_ANNOUNCEMENT_MSG_TEMPLATE = """Hello, /u/{}!

{}

Thanks for reading and playing - good luck!"""
>>>>>>> ec22b73e27c4152e5c55ba2a5911129c18070c26
