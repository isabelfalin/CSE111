def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("provinces.txt")

    # Print the entire list.
    print(text_list)

def read_list(filename):
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

        text_list.pop(0)
        text_list.pop()
        text_list = ["Alberta" if x == "AB" else x for x in text_list]

        alberta_count = text_list.count("Alberta")
        alberta_count = f"Alberta occurs {alberta_count} times in the modified list."

        print(text_list)
        print()
    # Return the list that contains the lines of text.
    return alberta_count


# Call main to start this program.
if __name__ == "__main__":
    main()
