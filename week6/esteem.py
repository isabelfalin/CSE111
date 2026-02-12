
def get_score(question, answer):
    score = 0
    if question in [1, 2, 4, 6, 7]:
        if answer == "D":
            score = 0
        elif answer == "d":
            score = 1
        elif answer == "A":
            score = 2
        elif answer == "a":
            score = 3
    elif question in [3, 5, 8, 9, 10]:
        if answer == "D":
            score = 3
        elif answer == "d":
            score = 2
        elif answer == "A":
            score = 1
        elif answer == "a":
            score = 0
    return score

def main():
    total_score = 0
    #self_score = 0
    #score = get_score(1, answer)
    #total_score = total_score + score
    #self_score = self_score + score

    print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")

    print()

    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(2, answer)

    print("2. I feel that I have a number of good qualities")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(2, answer)

    print("3. All in all, I am inclined to feel that I am a failure.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(3, answer)

    print("4. I am able to do things as well as most other people.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(4, answer)

    print("5. I feel I do not have much to be proud of.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(5, answer)

    print("6. I take a positive attitude toward myself.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(6, answer)

    print("7. On the whole, I am satisfied with myself.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(7, answer)

    print("8. I wish I could have more respect for myself.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(8, answer)

    print("9. I certainly feel useless at times.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(9, answer)

    print("10. At times I think I am no good at all.")
    answer = input("Enter D, d, a, or A: ")
    total_score = total_score + get_score(10, answer)

    print(f"Your score is {total_score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

main()
