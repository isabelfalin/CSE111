import csv
from datetime import datetime

#Players list
PLAYER_FIRST_NAME = 0
PLAYER_LAST_NAME = 1
UTR_RANKING = 2
GENDER = 3

#tournament list
TOURNAMENT_NAME = 0
TOURNAMENT_MINIMUM_UTR = 1
TOURNAMENT_GENDER = 2
TOURNAMENT_DATE = 3

def main():
    #load the data
    players_list = load_players("players.csv")
    tournamnet_list = load_tournaments("tournaments.csv")

    #show the menu until the user quits
    user_choice = None
    while user_choice != "Q":
        display_menu()
        user_choice = get_menu_choice().upper()

        #handle user choice
        if user_choice == "A":
           average_utr = calculate_UTR(players_list) 
           print(f"The average UTR is: {average_utr:.1f}")

        elif user_choice == "B":
            show_player_stats(players_list)
 
        elif user_choice == "C":
            get_qualified_players_for_tournaments(tournamnet_list, players_list)
            print()
    
    print("Thank you for using The Big T's Tennis Tracker!")

def load_players(file_name):
    player_list = []

    # Open the CSV file for reading.
    with open(file_name, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            player_list.append(row)

    return player_list

def load_tournaments(file_name):
    tournament_list = []

    # Open the CSV file for reading.
    with open(file_name, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            tournament_list.append(row)

    return tournament_list
    

def display_menu():
    print()
    print("Welcome to The Big T's Tennis Tracker! ")
    print()
    print("Please chose an option below:")
    print("A. Average UTR Rank")
    print("B. Player Stats")
    print("C. Tournament Qualifiers")
    print("Q. Quit")
    print()

def get_menu_choice():
    users_choice = input("Enter your selection: ")
    return users_choice

def calculate_UTR(players_list):
    total_utr = 0
    for player in players_list:
        player_utr = float(player[UTR_RANKING])
        total_utr = player_utr + total_utr
    average_utr = total_utr / len(players_list)
    return average_utr

def show_player_stats(players_list):
    for player in players_list:
        player_first_name = player[PLAYER_FIRST_NAME]
        player_last_name = player[PLAYER_LAST_NAME]
        player_utr_ranking = player[UTR_RANKING]
        player_gender = player[GENDER]
        print(f"{player_last_name.capitalize()}, {player_first_name.capitalize()}: {player_gender} - {player_utr_ranking}")

def get_qualified_players_for_tournaments(tournament_list, player_list):
    for tournament in tournament_list:
        tournament_name = tournament[TOURNAMENT_NAME]
        tournament_date = tournament[TOURNAMENT_DATE]
        print(f"\nThe {tournament_name} ({tournament_date}) Qualifying Players:\n")
        for player in player_list:
            player_first_name = player[PLAYER_FIRST_NAME]
            player_last_name = player[PLAYER_LAST_NAME]

            if does_player_qualify_for_tournament(player, tournament):
                print(f"\t{player_first_name.capitalize()} {player_last_name.capitalize()}")
    
def does_player_qualify_for_tournament(player, tournament):
    tournament_minimum_utr = float(tournament[TOURNAMENT_MINIMUM_UTR])
    player_utr_ranking = float(player[UTR_RANKING])
    player_gender = player[GENDER]
    tournament_gender = tournament[TOURNAMENT_GENDER]

    if player_utr_ranking >=  tournament_minimum_utr and player_gender == tournament_gender:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
