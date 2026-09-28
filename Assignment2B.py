# Class: CSE 1321L
# Section: 16B
# Term: Fall 2026
# Instructor: Rubaina Roshan
# Name: Abiegail Raymond
# Assignment: Assignment 2B

# Program Assignment2B.py
print("[Owl Airlines - Checked Bag Kiosk]")
while True:
    member_input = str(input("Are you a Hooty Hoo Preferred Member? (Y/N): "))
    if member_input == "Y":
        print("Welcome, and thank you for being a Hooty Hoo Preferred Member")
        print("As a perk for being awesome, your first 2 checked bags are free")
        print("Additional bags are $35.00 each")

    else:
        print("Checked Bag rates:")
        print("- First Checked bag: $35.00")
        print("- Second Checked bag: $50.00")
        print("- Third+ Checked bag: $150.00 each")

    checking_input = str(input("\nAre you checking any bags? (Y/N): "))
    if checking_input == "Y":
        bags_checked = int(input("How many bags are you checking in?: "))

        bag_fee = 0

        if member_input == "Y":
            print("\nAs a Hooty Hoo Preferred Member your first 2 bags are complimentary.")
            if bags_checked > 2:
                bag_fee = (bags_checked - 2) * 35.00

        else:
            if bags_checked == 1:
                bag_fee = 35.00
            elif bags_checked == 2:
                bag_fee = 35.00 + 35.00
            elif bags_checked >= 3:
                bag_fee = 35.00 + 50.00 + ((bags_checked - 2) * 150.00)
        if bag_fee > 0:
            print(f"\nChecked Bag fees to pay: ${bag_fee:.2f}")
            print()#

    if member_input == "Y":
        print("\nHave a safe flight and thank you for being a Hooty Hoo Preferred Member")
        print()#
