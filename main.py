
from welcome import *


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

        # enable background process (if idle, break!!! go back to welcome message to ask if person is new!)

        request = raw_input(">>  ")

        if (request != None or request == None):
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
