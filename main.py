import sys

name = input("Enter your name: ")
print('\n\n')
print('Hello', name, "Welcome to KBC", end="\n\n")
print("BEST OF LUCK\n\n")

# Questions
questions = [
    "1. Which animal is known as the Ship of the Desert?",
    "2. How many days are there in a week?",
    "3. How many days are there in a month?",
    "4. A rainbow consists of how many colours?",
    "5. How many minutes are there in an hour?"
]

# Answers list
answers = ["B", "D", "C", "A", "C"]

# Option function
def option(correct_answer, current_amount):
    ans = input("Enter the correct option:  ").upper()
    if ans == correct_answer:
        current_amount += 1000
        print("      CORRECT ANSWER ")
        print("CONGRATULATIONS! YOU HAVE WON: ", current_amount, end="\n\n\n")
        return current_amount, True
    else:
        print("Wrong answer")
        print("Nice playing with you. You are taking Rs.", current_amount, "INR with you\n\n")
        sys.exit()  # Exit the program

# Main Game Loop
def main():
    current_amount = 0
    for i in range(len(questions)):
        print(questions[i])
        print("(choose the correct answer: A/B/C/D)\n")
        print(options[i])
        current_amount, correct = option(answers[i], current_amount)
        if not correct:
            break

    print("Congratulations! You have completed the game with a total amount of ", current_amount, "INR")

# Options for each question
options = [
    "A. OSTRICH    B. CAMEL      C. LION      D. CAT",
    "A. 4     B. 5      C. 10     D. 7",
    "A. 365     B. 29     C. 30      D. 45",
    "A. 7      B. 4     C. 3      D. 10",
    "A. 30     B. 78     C. 60     D. 24"
]

# Run the game
if __name__ == "__main__":
    main()
