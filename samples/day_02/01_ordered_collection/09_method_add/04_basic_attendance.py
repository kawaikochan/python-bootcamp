from tkinter.scrolledtext import example

attendee_names = ["attendee name:"]

attendee_count = int(input("How many attendees? "))
for item in range (attendee_count):
    input("please write your name")


# Based on the attendee_count, ask the user for that many attendee names
#   attendee name: user input 1
#   attendee name: user input 2
#   attendee name: user input 3
#   ...

# Append each input in attendee_names and print attendee_names
