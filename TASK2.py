"""Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name."""

First_Name = input("Enter your First name : ")
Last_Name = input("Enter your Last name : ")

Full_Name = First_Name + " " + Last_Name
print(f"Hello, {Full_Name}!, Welcome to the Python Program")