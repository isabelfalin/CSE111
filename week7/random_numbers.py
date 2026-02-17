import random

def main():
    numbers = [16.2, 75.1, 52.3]
    answer = int(input("How many random numbers do you want to add? "))
    print(numbers)
    random_numbers_function(numbers, answer)
    print(numbers)

def random_numbers_function(numbers_list, quantity = 1):
    for i in range(quantity):
        x = random.uniform(0, 100)
        x = round( x, 1 )
        numbers_list.append(x)

#remove main to test using their code
if __name__ == "__main__":
    main()
        
        

    

