# Class: CSE 1321L
# Section: 16B
# Term: Fall 2026
# Instructor: Rubaina Roshan
# Name: Abiegail Raymond
# Assignment: Assignment 2A

# Program Assignment2A.py

loudness = float(input("Enter input loudness (dB): "))
threshold = float(input("Enter threshold (dB): "))

print("Select a ratio: ")
print("1 - 3:1")
print("2 - 4:1")
print("3 - 10:1")

choice = int(input("> "))

match choice:
    case 1:
        ratio = 3
    case 2:
        ratio = 4
    case 3:
        ratio = 10
    case _:
        ratio = 2

print(f"You have selected the {ratio}:1 ratio")

if loudness > threshold:
    leftover_amount = loudness - threshold
    compressed_amount = leftover_amount / ratio
    output = threshold + compressed_amount

else:
    output = loudness

print(f"Output Level: {output} dB")


