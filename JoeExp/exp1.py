import random


def main():
    while True:
        greetings = ['hi', 'HI', 'Hi']
        questionsoffeelings = ['How are you?', 'How are you doing?', 'How are you feeling?']
        answersforfeelings = ['Good, yourself?', 'Shitty. :(']

        userInput = input(">>> ")
        if userInput in greetings:
            print("Hello")
        elif userInput in questionsoffeelings:
            print(random.choice(answersforfeelings))
        else:
            print("I do not understand you.")

if __name__ == '__main__':
    main()
