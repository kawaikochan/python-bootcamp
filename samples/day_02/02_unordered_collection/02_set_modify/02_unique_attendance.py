
#attendee_names = []

#attendee_count = int(input("How many attendees? "))

# Based on the attendee_count, ask the user for that many attendee names
#for attendee in range(attendee_count):
 #   attendee_name = input("attendee name: ")
  #  attendee_names.append(attendee_name)

#print(attendee_names)

#print(attendee_names.count("chiyo"))

attendee_names = set()
attendee_count = int(input("How many attendees? "))
for attendee in range(attendee_count):
   attendee_name = input("attendee name: ")
   attendee_names.add(attendee_name)


# Based on the attendee_count, ask the user for that many attendee names
#   attendee name: Attendee Name 1
#   attendee name: Attendee Name 2
#   attendee name: Attendee Name 3
#   ...

# Append each input in attendee_names and print the unique attendee_names