def ask():
    import random
    roll = int(random.random() * 3) + 1
    if roll == 1:
        print("Yes!\n")
    elif roll == 2:
        print("No.\n")
    else:
        print("Maybe.\n")


def check_input(choice):
    import random
    while True:
        response = raw_input().lower()
        if choice == "again":
            if response == "":
                print("You need to ask an actual question!")
            elif response == "yes":
                return True
            elif response == "no":
                return False
            else:
                print("Error. Invalid input. Enter 'yes' or 'no'.\n")

        elif choice == "question":
            if response == " ":
                print("You need to ask an actual question!")
            elif "?" not in response:
                print("Please include a question mark!!")
            elif spell_check(response) > 0:
                num = int(random.random() * 4) + 1
                if num == 1:
                    print("Where did you learn to spell? Try again:")
                elif num == 2:
                    print("What is this, preschool? Spell properly!!")
                elif num == 3:
                    print("Sorry, some of your words didn't show up in the dictionary. Try avoiding names")
                else:
                    print("Ever heard of a dictionary? Please spell correctly.")
            else:
                return response


def check_repeat(repeat, index):
    if repeat[index] > 1:
        return True
    else:
        return False


def print_repeat(num):
    if num == 1:
        print("Don't you ever get tired of these question types? Okay...")
    elif num == 2:
        print("Obsessed with this question type? Glad you're having fun...")
    elif num == 3:
        print("You know, we have other question types available...")
    else:
        print("Relax and stop worrying...")


# Answers intelligently to the following questions:
# Should I ask my crush out?
# Does anyone like me?
# Are Jim and Pam dating?
# Should I ask them out on a second date?

def rand_love(choice, num, repeat, index):
    import time
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)

    if choice == "a":
        if num == 1:
            print("Hoping to ask your crush out? Well, the Magic 8-Ball says... ")
            time.sleep(1.5)
        elif num == 2:
            print("We're hoping the answer is yes, and the 8-Ball replies...")
            time.sleep(1.5)
        else:
            print("No matter what the 8-Ball says right now, just remember to take care of yourself. Verdict:")
            time.sleep(1.5)
    elif choice == "some":
        if num == 1:
            print("Hoping to find love from that special someone? The 8-Ball declares ...")
            time.sleep(1.5)
        elif num == 2:
            print("Well DOES anyone like you? According to my calculations...")
            time.sleep(1.5)
        else:
            print("We're scanning the database for affection directed towards you. Did we find anything?")
            time.sleep(1.5)
    elif choice == "other":
        if num == 1:
            print("But are they really dating? According to the Almighty 8-Ball ...")
            time.sleep(1.5)
        elif num == 2:
            print("Wow, way to be nosy. Anyways, the ruling is:")
            time.sleep(1.5)
        else:
            print("Ever heard of minding your own business? Well if you really want to know...")
            time.sleep(1.5)
    elif choice == "again":
        if num == 1:
            print("Will things go well at the second date? The 8-Ball gives a resounding...")
            time.sleep(1.5)
        elif num == 2:
            print("Putting your fate in the hands of the 8-Ball? Risky move. The answer is...")
            time.sleep(1.5)
        else:
            print("Hopefully the second time goes better than the first time, right? Final decision:")
            time.sleep(1.5)


def rand_college(choice, num, repeat, index):
    import time
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)

    if choice == "accept":
        if num == 1:
            print("Hoping to get into your dream college? The 8-Ball declares...")
            time.sleep(1.5)
        elif num == 2:
            print("Well, the moment of truth. Here it is:")
            time.sleep(1.5)
        else:
            print("Too nervous to wait for the mailed decision? Here's the prophetic one:")
            time.sleep(1.5)
    elif choice == "major":
        if num == 1:
            print("Will you get your desired major? The data says...")
            time.sleep(1.5)
        elif num == 2:
            print("What you study is always most important. 8-Ball says...")
            time.sleep(1.5)
        else:
            print("The major appears to be a major problem. Terrible jokes aside ....")
            time.sleep(1.5)
    elif choice == "enjoy":
        if num == 1:
            print("Will you enjoy your college experience? According to the 8-Ball...")
            time.sleep(1.5)
        elif num == 2:
            print("Hoping to fit in on campus next year? Chances are ...")
            time.sleep(1.5)
        else:
            print("Judging by your college and your personality, the answer is...")
            time.sleep(1.5)

def rand_football(choice, num, repeat, index):
    import time
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)

    if choice == "superbowl":
        if num == 1:
            print("Will your team have the chance to win the Lombardi Trophy? Odds are...")
            time.sleep(1.5)
        elif num == 2:
            print("But will your favorite team make it to the Super Bowl? 8-Ball says...")
            time.sleep(1.5)
        else:
            print("At this point in the season, you probably already know the answer. 8-Ball confirms...")
            time.sleep(1.5)
    elif choice == "playoff":
        if num == 1:
            print("Perhaps your team CAN clinch a playoff spot...8 Ball declares:")
            time.sleep(1.5)
        elif num == 2:
            print("Will your team make it to the postseason? According to the 8 Ball...")
            time.sleep(1.5)
        else:
            print("You are either about to be excited or extremely disappointed. Verdict:")
            time.sleep(1.5)
    elif choice == "future":
        if num == 1:
            print("Will your team ever truly succeed during your lifetime? Sadly...")
            time.sleep(1.5)
        elif num == 2:
            print("Be careful what you wish for. Disappointment is inevitable. Final decision:")
            time.sleep(1.5)
        else:
            print("Assessing draft picks...calculating leadership positions...output:")
            time.sleep(1.5)

def rand_christmas (choice, num, repeat, index):
    import time
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)

    if choice == "accept":
        if num == 1:
            print("Will your Christmas celebration be a family embarrassment or a treasured memory? 8-Ball says...")
            time.sleep(1.5)
        elif num == 2:
            print("Will your relatives get into an argument about politics, or will you actually enjoy your winter break? According to 8-Ball...")
            time.sleep(1.5)
        else:
            print("What even is this question? Doesn't everybody have fun during winter break?")
            time.sleep(1.5)
    elif choice == "gift":
        if num == 1:
            print("Will it be a new phone, or some dirty coal? The festive 8-Ball says:")
            time.sleep(1.5)
        elif num == 2:
            print("Will your presents this year live up to the hype? Verdict:")
            time.sleep(1.5)
        else:
            print("Instead of asking about presents, maybe you could be grateful for what you have? Anyways:")
            time.sleep(1.5)
    elif choice == "resolution":
        if num == 1:
            print("You shouldn't be leaving your resolutions up to an 8-Ball, but okay:")
            time.sleep(1.5)
        elif num == 2:
            print("Always remember to follow your New Year's resolution:")
            time.sleep(1.5)
        else:
            print("Believe in yourself and you will have the power to accomplish anything:")
            time.sleep(1.5)

def rand_grade (choice, num, repeat, index):
    import time
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)

    if choice == "A":
        if num == 1:
            print("Too bad you left your grades until the end of the semester. Verdict:")
            time.sleep(1.5)
        elif num == 2:
            print("No matter what this 8-Ball tells you, don't worry about it too much")
            time.sleep(1.5)
        else:
            print("Will it be an A or a B? Life or death? Drumroll...")
            time.sleep(1.5)
    elif choice == "final":
        if num == 1:
            print("Will you get utterly wrecked on the final exam? 8-Ball says...")
            time.sleep(1.5)
        elif num == 2:
            print("What are you doing here? Stop worrying and start studying? Anyways...")
            time.sleep(1.5)
        else:
            print("You should have already started studying for finals...")
            time.sleep(1.5)
    elif choice == "next":
        if num == 1:
            print("Will next semester turn out better than this Semester 1 dumpster fire? 8-Ball says...")
            time.sleep(1.5)
        elif num == 2:
            print("Not doing too well in S1? Semester 2 may be difficult, according to the 8-Ball:")
            time.sleep(1.5)
        else:
            print("Accessing grades ... assessing curriculum ... rolling dice ... output:")
            time.sleep(1.5)

def rand_sport(choice, num, repeat, index):
    import time
    repeat[index] += 1
    if check_repeat(repeat, index):
        print_repeat(num)

    if choice == "cif":
        if num == 1:
            print("Hoping to know your team's playoff fortunes ahead of time? Be careful what you wish for...")
            time.sleep(1.5)
        elif num ==2 :
            print("What are you doing here? Stop worrying and practice some more.")
            time.sleep(1.5)
        else:
            print("How good will your team be in the postseason? The 8-Ball calculates:")
            time.sleep(1.5)
    elif choice == "next":
        if num == 1:
            print("Will you team be any good next year? According to the 8-Ball:")
            time.sleep(1.5)
        elif num == 2:
            print("Accessing game footage ... assessing players ... output:")
            time.sleep(1.5)
        else:
            print("Whatever happens, happens. Next year, at least.")
            time.sleep(1.5)
    elif choice == "eval":
        if num == 1:
            print("You could probably just ask your coach. Here's the 8-Ball:")
            time.sleep(1.5)
        elif num == 2:
            print("Success should be something you perceive youself. Anyways...")
            time.sleep(1.5)
        else:
            print("Get ready for reality:")
            time.sleep(1.5)

def get_a(response, num, repeat):
    # 1st topic is love
    if "should" in response and ("i" in response or "I" in response) and "ask" in response and (
            "my crush" in response or "crush" in response) and ("out" in response or "date" in response):
        rand_love("a", num, repeat, 0)
    elif "does" in response and ("like" in response or "have a crush") and "me" in response and (
                "anyone" in response or "someone" in response or "crush" in response):
        rand_love("some", num, repeat, 0)
    elif "are" in response and "dating" in response or ("each other" in response and "dating" in response and "and"):
        rand_love("other", num, repeat, 0)
    elif ("should" in response or "will" in response) and "i" in response and (
            "ask" in response or "date" in response) and (
                "second" in response or "2nd" in response or "again" in response):
        rand_love("again", num, repeat, 0)
    # second topic is college (dream, major, enjoy)
    elif ("will" in response or "do" in response) and "i" in response and ("get into" in response or "accepted" in response):
        rand_college("accept", num, repeat, 1)
    elif "will" in response and "i" in response and ("find" in response or "get" in response) and "major" in response:
        rand_college("major", num, repeat, 1)
    elif ("will" in response or "do" in response) and "i" in response and ("enjoy" in response or "like" in response) and ("life" in response or "college" in response):
        rand_college("enjoy", num, repeat, 1)
    # third topic is NFL season (superbowl, playoffs, future)
    elif ("NFL" in response or "football" in response) and "super bowl" in response and ("get" or "make" in response):
        rand_football("superbowl", num, repeat, 2)
    elif ("playoffs" in response or "playoff" in response) and ("make" in response or "get" in response) and "team" in response:
        rand_football("playoff", num, repeat, 2)
    elif "team" in response and ("future" in response or "year" in response or "years" in response) and "succeed" in response:
        rand_football("future", num, repeat, 2)
    # fourth topic is Christmas (fun, gifts, resolution)
    elif ("will" in response or "do" in response) and "i" in response and ("good time" in response or "fun" in response or "enjoy" in response) and ("holiday" in response or "christmas" in response or "winter break" in response):
        rand_christmas("fun", num, repeat, 3)
    elif ("will" in response or "do" in response) and "i" in response and ("gift" in response or "gifts" in response):
        rand_christmas("gift", num, repeat, 3)
    elif "i" in response and ("resolution" in response or "promises" in response) and ("follow" in response or "keep" in response):
        rand_christmas("resolution", num, repeat, 3)
        # fifth topic is grades (A, final, semester 2)
    elif "will" in response and ("get" in response or "pull" in response) and ("a" in response or "an a" in response):
        rand_grade("A", num, repeat, 4)
    elif ("final" in response or "final exam" in response or "finals" in response) and ("hard" in response or "difficult" in response):
        rand_grade("final", num, repeat, 4)
    elif ("next" in response or "semester 2" in response or "next semester" in response) and ("well" in response or "good" in response):
        rand_grade("next", num, repeat, 4)

        # sixth topic is "your" sport (playoffs, next year, good)
    elif ("cif" in response or "playoffs" in response) and ("well" in response or "good" in response):
        rand_sport("cif", num, repeat, 5)
    elif ("next" in response or "next year" in response or "next season" in response) and ("well" in response or "good" in response):
        rand_sport("next", num, repeat, 5)
    elif "is" in response and "my team" in response and "good" in response:
        rand_sport("eval", num, repeat, 5)


def ai(response, repeat):
    import random
    num = int(random.random() * 3) + 1
    get_a(response, num, repeat)


def spell_check(response):
    from enchant.checker import SpellChecker
    count = 0
    chkr = SpellChecker("en_US")
    chkr.set_text(response)
    for err in chkr:
        if err:
            count += 1
    return count


def main():
    import time
    repeat = [0] * 7
    print("Welcome to the Magic 8-Ball!")
    answer = True
    while answer:
        print("Ask the 8-Ball a yes or no question about love, college, NFL, Christmas, grades, or your school sport")
        time.sleep(1.5)
        print("Remember to leave out proper nouns. Be general.")
        ai(check_input("question"), repeat)
        ask()
        print("Would you like to ask another question?")
        answer = check_input("again")

    print("I hope this was enjoyable!")


main()