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

    KENO_ERROR_MSG = """Hello! Please place your wager in the form of a 
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

    AON_DICE_ROLL_NO_BALANCE_ERROR_MSG = """/u/{},

It appears that you have no points with which to wager! Please message the moderators
and they will deposit the starting amount into your bankroll so you can get back on 
your feet.

Thanks, and good luck!"""

    AON_DICE_ROLL_ERROR_MSG = """/u/{},

Please place your bet by posting a comment like this: 

    wager

Thanks, and good luck!"""

    WAR_ERROR_MSG = """/u/{},

Please place your bet by selecting either the 'small' or 'big' bet:

    wager small
    wager mid
    wager big

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

    AON_DICE_ROLL_WIN_MSG = """/u/{},

You've risked your whole balance ({:,}) on this die roll, and the result is...

#__{}__!

Congratulations! Your new balance is {:,}. Good luck!"""

    AON_DICE_ROLL_LOSE_MSG = """/u/{},

You've risked your whole balance ({:,}) on this die roll, and the result is...

#__{}__!

Unfortunately, you've lost your bankroll. You'll have some points automatically deposited in just a minute!
Thanks for playing, and good luck!"""

    CASINO_WAR_REPLY_WRAPPER_TEMPLATE_MSG = """/u/{},

Thank you for your wager of {:,}! Here are your war results:

&nbsp;

{}

Your outcome is : **{}**

&nbsp;

Your __winnings__ are __{:,}__

Your __profit__ is __{:,}__

Your __new balance__ is ***{:,}***

Thanks for playing, and good luck!
"""

    CASINO_WAR_BODY_TEMPLATE = """Your card : 

    {}

Dealer's card: 

    {}"""

    DEPOSIT_AFTER_BANKRUPTCY_MSG = """/u/{},

It looks like you've lost all of your points! Don't worry - we've added some more to 
your balance. Get back out there and have fun!"""

    KENO_REPLY_WRAPPER_TEMPLATE_MSG = """/u/{},

Thank you for your wager of {:,}! Here are your keno results:

&nbsp;

{}

Your outcome is : **{}**

&nbsp;

Your __winnings__ are __{:,}__

Your __profit__ is __{:,}__

Your __new balance__ is ***{:,}***

Thanks for playing, and good luck!"""

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

class PostBodies:
    POKER_POST_TITLE = "Poker Megathread"
    POKER_POST_BODY = """If you want to bet on some poker hands, this is the place to be! In this thread, after your wager is placed, you'll be dealt a 2-card poker hand, and the dealer will put 5 cards on the board (just like Texas Hold'em). This hand will be evaluated, and you will be paid out according to the type of hand you were dealt. 

Make a wager by posting a top-level comment of the form:

`wager {NUMBER}`

where the number is the amount you want to bet (0 < x <= balance).

This game pays out as follows:

Hand | Payout 
---------|----------
No pair OR One pair | __0__
Two pair | __2 : 1__
Three of a Kind | __5 : 1__
Straight | __10 : 1__
Flush | __25 : 1__
Full House | __55 : 1__
Four of a Kind | __600 : 1__
Straight Flush | __4,000 : 1__
Royal Flush | __45,000 : 1__

Good luck everyone!

## __The maximum bet for this game is 50,000__

*Note: In the event that you place multiple bets rapidly, the __most recently placed__ wager will be processed first. In other words, wagers will be processed in the order __opposite__ in which they were placed.*"""


	ROULETTE_POST_TITLE = "Roulette Megathread"
	ROULETTE_POST_BODY = """This is a simplified version of classic roulette! 

In this thread, after your wager is placed, a simulated roulette wheel will be spun, and you will be paid out according to where the ball lands! 

Make a wager by posting a top-level comment of the form:

`wager {NUMBER} {BET_TYPE}`

where the number is the amount you want to bet (0 < x <= balance), and the {BET_TYPE} is one of the types of bets in the table below (and if you're betting singles, it should be a number 0 <= x <= 36).

Some example bets:

    wager 100 red
    wager 100 even
    wager 200 13
    wager 100 0

This game pays out as follows:

Bet| Payout 
---------|----------
Even / Odd | __2 : 1__
Red / Black | __2 : 1__
Singles (0-36) | __37 : 1__

You can include multiple bets in a single spin as well! Just separate them by a single line break when you're typing them - after the comment posts it will look like it's all on one line, but the dealer will be able to read it! **And it must be only one line break!** The comment as you're typing it should look like the example above, even though in the preview and when it's posted it will be all on one line.

Last thing - if you do place multiple bets in the same comment, it behaves like you would place them in a casino - you must have enough in your balance to place all of your bets initially! The total of all of your bets must be less than your bankroll.

Good luck everyone!

## __The maximum bet for this game is 100,000__

*Note: In the event that you place multiple bets rapidly, the __most recently placed__ wager will be processed first. In other words, wagers will be processed in the order __opposite__ in which they were placed.*"""
	
	DICEROLL_POST_TITLE = "3-6-9 Dice Roll Megathread"
	DICEROLL_POST_BODY = """
	Hello! This thread will be the place to play a dice game called 3-6-9. The rules are simple:

* After a wager is made, 2 die rolls will be simulated and their results totaled
* If the total is equal to **3**, **6** or **9**, then you win!

Make a wager by posting a top-level comment of the form:

`wager {NUMBER}`

where the number is the amount you want to bet (0 < x <= balance).

This game pays out __3 : 1__!

Good luck everyone!

## __The maximum bet for this game is 150,000__

*Note: In the event that you place multiple bets rapidly, the __most recently placed__ wager will be processed first. In other words, wagers will be processed in the order __opposite__ in which they were placed.*"""
	
	CASINOWAR_POST_TITLE = "HIGH-LIMIT Casino War Thread"
	CASINOWAR_POST_BODY = """
	Welcome to the High-limit Casino War game! Here's how this game works:

---

You will make a wager by posting a top-level comment of the form:

`wager {SIZE}`

where the *size* is the amount you want to bet (shown at the bottom of the OP)

&nbsp;

After your bet is accepted, one card will be dealt to each the player and the dealer. If the player's card is higher, the player wins. If the dealer's is higher, the player loses.

__In the event of a tie,__ the player and dealer to go war! This means that one card is dealt to each again. Same as before, the higher card wins. If the war is tied, the player will win a bonus higher payout!

---

This game pays out as follows:

Situation| Payout 
---------|----------
Player **wins** during first deal | __2 : 1__
Player **wins** after war | __1.5 : 1__
Player **ties** after war | __3 : 1__

---

Here are the valid bets and their values:

* Small ('wager small') :**1 million**
* Mid ('wager mid') : **20 million**
* Big ('wager big') : **100 million**

&nbsp;

Good luck everyone!

*Note: In the event that you place multiple bets rapidly, the __most recently placed__ wager will be processed first. In other words, wagers will be processed in the order __opposite__ in which they were placed.*"""
	
	KENO_POST_TITLE = "Keno Megathread"
	KENO_POST_BODY = """This is a simplified version of a game called Keno, and it's kind of like a lottery! Here's how it works:

---

Make a wager by posting a top-level comment of the form:

`wager {NUMBER}`

where the number is the amount you want to bet (0 < x <= balance).

&nbsp;

You will be assigned ***8*** random numbers in the range of 1-60. The dealer will then choose ***15*** random numbers on that same range. Both of your lists of numbers will be compared, and if you match enough numbers (this is called a **catch**), you win!

---

This game pays out as follows:

No. of Catches| Payout 
---------|----------
0 or 1| __0__
2 | __2 : 1__
3 | __5 : 1__
4 | __10 : 1__
5 | __20 : 1__
6 | __75 : 1__
7 | __2,000 : 1__
8 | __25,000 : 1__

Good luck everyone!

## __The maximum bet for this game is 100,000__

*Note: In the event that you place multiple bets rapidly, the __most recently placed__ wager will be processed first. In other words, wagers will be processed in the order __opposite__ in which they were placed.*"""