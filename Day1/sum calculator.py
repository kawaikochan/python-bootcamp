def greeting():

    print("hello")

greeting()
greeting()

def line_generator():
    for number in range(3):
        print("line",number)


line_generator()

def line_generator(line_count):


    for number in range (line_count):
        print("line", number)

line_generator(20)

def line_generator(line_count,message):


    for number in range (line_count):
        print(message, number)

line_generator(4,"hello world")



