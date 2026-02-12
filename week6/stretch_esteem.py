
def get_score(question, answer):
    score = 0
    if question in [1, 4, 5, 6, 7, 8, 9, 12, 16, 17]:
        if answer == "D":
            score = 1
        elif answer == "d":
            score = 2
        elif answer == "N":
            score = 3
        elif answer == "a":
            score = 4
        elif answer == "A":
            score = 5
    elif question in [2, 3, 10, 11, 13, 14, 15, 18,]:
        if answer == "D":
            score = 5
        elif answer == "d":
            score = 4
        elif answer == "N":
            score = 3
        elif answer == "a":
            score = 2
        elif answer == "A":
            score = 1
    return score

def main():
    total_score = 0
    self_score = 0
    perspective_score = 0
    experience_score = 0
    short_score = 0 
    #score = get_score(1, answer)
    #total_score = total_score + score
    #self_score = self_score + score
    
    print("1. I enjoy being outdoors, even in unpleasant weather.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(1, answer)
    experience_score = experience_score + get_score(1, answer)

    print("2.Some species are just meant to die out or become extinct.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(2, answer)
    perspective_score = perspective_score + get_score(2, answer)

    print("3. Humans have the right to use natural resources any way we want.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(3, answer)
    perspective_score = perspective_score + get_score(3, answer)

    print("4. My ideal vacation spot would be a remote, wilderness area.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(4, answer)
    experience_score = experience_score + get_score(4, answer)
    short_score = short_score + get_score(4, answer)

    print("5. I always think about how my actions affect the environment.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(5, answer)
    self_score = self_score + get_score(5, answer)
    short_score = short_score + get_score(5, answer)

    print("6. I enjoy digging in the earth and getting dirt on my hands.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(6, answer)
    experience_score = experience_score + get_score(6, answer)

    print("7. My connection to nature and theenvironment is a part of my spirituality.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(7, answer)
    self_score = self_score + get_score(7, answer)
    short_score = short_score + get_score(7, answer)

    print("8. I am very aware of environmental issues.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(8, answer)
    self_score = self_score + get_score(8, answer)

    print("9. I take notice of wildlife wherever I am.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(9, answer)
    experience_score = experience_score + get_score(9, answer)
    short_score = short_score + get_score(9, answer)

    print("10. I don’t often go out in nature. ")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(10, answer)
    experience_score = experience_score + get_score(10, answer)

    print("11. Nothing I do will change problems in other places on the planet.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(11, answer)
    perspective_score = perspective_score + get_score(11, answer)

    print("12.  I am not separate from nature, but a part of nature. ")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(12, answer)
    self_score = self_score + get_score(12, answer)

    print("13. The thought of being deep in the woods, away from civilization, is frightening.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(13, answer)
    experience_score = experience_score + get_score(13, answer)

    print("14. My feelings about nature do not affect how I live my life.  ")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(14, answer)
    self_score = self_score + get_score(14, answer)

    print("15. Animals, birds and plants should have fewer rights than humans.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(15, answer)
    perspective_score = perspective_score + get_score(15, answer)

    print("16. Even in the middle of the city, I notice nature around me. ")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(16, answer)
    self_score = self_score + get_score(16, answer)

    print("17. My relationship to nature is an important part of who I am.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(17, answer)
    self_score = self_score + get_score(17, answer)
    short_score = short_score + get_score(17, answer)

    print("18. Conservation is unnecessary because nature is strong enough to recover from any human impact.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(18, answer)
    perspective_score = perspective_score + get_score(18, answer)

    print("19.The state of non-human species is an indicator of the future for humans.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(19, answer)
    perspective_score = perspective_score + get_score(19, answer)

    print("20. I think a lot about the suffering of animals.")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(20, answer)
    perspective_score = perspective_score + get_score(20, answer)

    print("21. I feel very connected to all living things and the earth")
    answer = input("Enter D, d, N, a, or A: ")
    total_score = total_score + get_score(21, answer)
    self_score = self_score + get_score(21, answer)
    short_score = short_score + get_score(21, answer)

    average_score = total_score / 10
    average_self = self_score / 8
    average_perspective = perspective_score / 7
    average_experience = experience_score / 6 
    average_short = short_score / 6

    print()
    print(f"Your overall NR_score is {average_score:.2f}")
    print(f"Your NR_self score is: {average_self:.2f}")
    print(f"Your NR_perspetive score is: {average_perspective:.2f}")
    print(f"Your NR_experience score is: {average_experience:.2f}")
    print(f"Your short-form NR is: {average_short:.2f}")
    print()

main()
