from questions import questions


def display_question(question_number, question_data):
    print()
    print("Question", question_number)
    print(question_data["question"])

    options = question_data["options"]

    for i in range(len(options)):
        print(str(i + 1) + ".", options[i])


def run_game():
    print("=" * 45)
    print("        NEXUS - CODE AWAKENING")
    print("        Coding Challenge Game")
    print("=" * 45)

    name = input("Enter your name: ")

    score = 0

    for i in range(len(questions)):
        display_question(i + 1, questions[i])

        choice = input("Enter your answer (1-4): ")

        if choice.isdigit():
            choice = int(choice)

            if choice == questions[i]["answer"]:
                print("Correct!")
                score = score + 1
            else:
                print("Wrong answer.")
        else:
            print("Invalid input.")

    print()
    print("=" * 45)
    print("Game completed!")
    print("Player:", name)
    print("Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good effort! Keep practicing.")
    else:
        print("Keep practicing and try again!")

    print("=" * 45)


def main():
    run_game()


if __name__ == "__main__":
    main()