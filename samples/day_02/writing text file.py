with open("test.txt","w")as file:
    file.write("new line")

with open("text.txt","a")as file:
    file.write("new line")

with open("text.txt","a")as file:
    messsage=["a","b","c"]
    #messsage=+"\n",
names=["mia\n","ethan\n","liam\n"]

with open("friends","w")as file:
    file.writelines(names)
