#1

def swap_cases(s):
    swapped = ''
    for char in s:
        if char.islower():
            swapped += char.upper()
        elif char.isupper():
            swapped += char.lower()
        else:
            swapped += char
    return swapped

sample_input = "HackerRank.com presents \"Pythonist 2\"."
print(swap_cases(sample_input))

#2

def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)

sample_input = "this is a string"
print(split_and_join(sample_input))

#3
def print_full_name(first, last):
    full_name = first + " " + last
    print("Hello {}! You just delved into python.".format(full_name))

first_name = input().strip()
last_name = input().strip()
print_full_name(first_name, last_name)

#4
def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    modified_string = ''.join(string_list)
    return modified_string

input_string = input().strip()
position, character = input().strip().split()
position = int(position)

result = mutate_string(input_string, position, character)
print(result)

#5

def count_substring(string, sub_string):
    count = string.count(sub_string)
    return count

string = input().strip()
sub_string = input().strip()

result = count_substring(string, sub_string)
print(result)

#6

def validate_string(s):
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

s = input().strip()

validate_string(s)

#7

#Ishlolmadim

#8

import textwrap

def wrap(string, max_width):
    wrapped_lines = textwrap.wrap(string, width=max_width)
    wrapped_string = '\n'.join(wrapped_lines)
    return wrapped_string

string = input().strip()
max_width = int(input().strip())

wrapped_string = wrap(string, max_width)
print(wrapped_string)

#9

#Ishlolmadim


#10


def print_formatted(number):
    width = len(bin(number)[2:])

    print("Decimal Octal Hexadecimal Binary")

    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")


number = int(input().strip())

print_formatted(number)

#11

#Ishlolmadim



#12

def capitalize_name(full_name):
    capitalized_name = full_name.title()
    return capitalized_name

full_name = input().strip()

capitalized_name = capitalize_name(full_name)
print(capitalized_name)







