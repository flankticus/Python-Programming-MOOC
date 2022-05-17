# Write your solution here
def longest(list_of_strings: list):
    longest = list_of_strings[0]
    for word in list_of_strings:
        if len(word) > len(longest):
            longest = word

    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))