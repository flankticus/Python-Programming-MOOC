# Write your solution here
from audioop import add


def length_of_longest(alist: list):
    longest = 0
    for item in alist:
        if len(item) > longest:
            longest = len(item)
    return longest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)