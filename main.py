import time
import re

from Modules.welcome import *


def main():

    # if haven't been spoken to in a while (say 5 mins) ask if person is new or if they are someone already spoken to
    # if already spoken to, check and see if they know who they are and if they exist in the brain yet

    # pull in retained knowledge of active user
    # welcomeText() #eventually take in basic information about current user such as name

    if(True):
        # get module names from file
        # compare any changes to already loaded modules
        # update changes

        # import available modules
        # print any errors while loading modules
        welcomeText()

        # enable background process (if idle, break!!! go back to welcome message to ask if person is new!)
        agreements = {'accepted': ['yes', 'ya'], 'learning': []}

        thetime = time.time()
        request = raw_input(">>  ")
        if(time.time() - 5 > thetime):
            print("\n~~~~~~~~~~~~~~~~~~~~~~\n" +
                  "Is that still you sir?")
            confirm = raw_input(">>  ")
            for agree in agreements['accepted']:
                if agree in confirm:
                    print("Nice to see you sir!")
                    break
            else:
                for agree in agreements['learning']:
                    if agree in confirm:
                        print("So you're telling me that \""+agree+"\" means yes?")
                        reaffirm = raw_input(">>  ")
                        for agree in agreements['accepted']:
                            if agree in reaffirm:
                                agreements['accepted'].append(agree)
                                agreements['learning'].pop(agree)
                                print("Thank you for helping me learn!")
                                print("Welcome back sir.")
                else:
                    print("Fred: Does that mean yes?")
                    reaffirm = raw_input(">>  ")
                    for agree in agreements['accepted']:
                        if agree in reaffirm:
                            newwords = re.findall(r"[\w']+", confirm)
                            for words in newwords:
                                if words not in agreements['learning'] and words not in agreements['accepted']:
                                    agreements['learning'].append(words)
                                elif words not in agreements['accepted']:
                                    agreements['accepted'].append(agree)
                                    agreements['learning'].pop(agree)
                            print("Thank you for helping me learn!")
                            print("Welcome back sir.")
                if request in agreements:

                    print("Fred: very good sir, what can I do for you?")
        else:
            pass

        print agreements

        if (request is not None or request is None):
            pass
            # disable idle watch process when input has been received!

        # pull from modules
        # regex match based on order of module priority

        # provide appropriate response as return from found module
        # notify user of further information if any processes have started (DEBUG OPTION)

        # scrape information from request and add anything relevant to information about current user

        # create new user if necessary, join/match users if they seem similar


# ====================================================================
# main loop init + check
if __name__ == "__main__":
    while(True):
        try:
            main()
        except KeyboardInterrupt:
            answer = raw_input("\nAre you sure you want to exit? [Y/n]")
            if answer.lower() != "n":
                exit(0)
