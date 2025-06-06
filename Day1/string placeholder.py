name_message="your name is{}."
number_message="your favorite number is{}"
color_message="your favorite color is{}"

input_name=input("enter your name")
input_number=input("enter your favorite number")
input_color=input("enter your favorite color")

formatted_name=name_message.format(input_name)
print(formatted_name)

formatted_number=input_number.format(input_number)
print(formatted_number)

formatted_color=input_color.format(input_color)
print(formatted_color)


item_1_price="item price is{}"
item_2_price=" item price is{}"
item_3_price="item price is{}"

item_1_name=input("enter the price 1" )
item_2_name=input("enter the price 2" )
item_3_name=input("enter the price 3" )


total_cost=