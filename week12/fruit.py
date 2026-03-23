def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    print()

    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")
    print()

    fruit_list.append("orange")
    print(f"Appended: {fruit_list}")
    print()

    i = fruit_list.index("apple")
    fruit_list.insert(i, "cherry")
    print(f"Insert and Index: {fruit_list}")
    print()

    fruit_list.remove("banana")
    print(f"Removed banana: {fruit_list}")
    print()

    fruit_list.pop()
    print(f"Pop List: {fruit_list}")
    print()

    fruit_list.sort()
    print(f"Sorted: {fruit_list}")
    print()

    fruit_list.clear()
    print(f"Cleared List: {fruit_list}")


if __name__ == "__main__":
    main()