import re
import random

agreements = {'accepted': ['yes', 'ya'], 'learning': []}
insults = ['bugger', 'dumb dumb']
users = ['joe', 'jakob']


def welcomeText():
    print("Hello! I am Fred.\n" + "What can I do for you?")


def checkuser():
    print("Could you tell me who this is?")
    name = raw_input(">>  ")
    if name in users:
        loc = users.index(name)
        print("Ahh, hello " + users[loc] + ". What can I do for you?")
        return True
    else:
        users.append(name)
        print("Nice to meet you " + name + ", I'm Fred, what can I do for you?")
        return True


def personunknown():
    print("Is that still you sir?")
    confirm = raw_input(">>  ")
    for agree in agreements['accepted']:
        if agree in confirm:
            print("Nice to see you sir!")
            return True
    else:
        for learn in agreements['learning']:
            if learn in confirm:
                print("So you're telling me that \""+learn+"\" means yes?")
                reaffirm = raw_input(">>  ")
                for agree in agreements['accepted']:
                    if agree in reaffirm:
                        print(agree)
                        agreements['accepted'].append(learn)
                        agreements['learning'].remove(learn)
                        print("Thank you for helping me learn!")
                        print("Welcome back sir.")
                        return True
        else:
            print("Does that mean yes?")
            reaffirm = raw_input(">>  ")
            for agree in agreements['accepted']:
                if agree in reaffirm:
                    newwords = re.findall(r"[\w']+", confirm)
                    for words in newwords:
                        if words not in agreements['learning'] and words not in agreements['accepted']:
                            agreements['learning'].append(words)
                        elif words not in agreements['accepted']:
                            agreements['accepted'].append(agree)
                            agreements['learning'].remove(agree)
                            print("Thank you for helping me learn!")
                    print("Welcome back sir.")
                    return True
            print("You're being unclear you " + random.choice(insults))
            return False
