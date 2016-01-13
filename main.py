import time

from Modules.welcome import *


def main():

    # if haven't been spoken to in a while (say 5 mins) ask if person is new or if they are someone already spoken to
    # if already spoken to, check and see if they know who they are and if they exist in the brain yet

    # pull in retained knowledge of active user
    # welcomeText() #eventually take in basic information about current user such as name

    welcomeText()

    while(True):
        # get module names from file
        # compare any changes to already loaded modules
        # update changes

        # import available modules
        # print any errors while loading modules

        # enable background process (if idle, break!!! go back to welcome message to ask if person is new!)

        thetime = time.time()
        request = raw_input(">>  ")
        if(time.time() - 2 > thetime):
            affirm = personunknown()

            # Pseudo parse
            # Eventually this will decide what to do with the input
            if affirm is True:
                req = request.split()
                print("Your request is made up of the words:"),
                for word in req:
                    print(" " + word)
            else:
                checkuser()
                print("This is where I am supposed to parse your input :/ but I can't yet")
        else:
            print("This is where I am supposed to parse your input :/ but I can't yet")

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
