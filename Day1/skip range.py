count=0
for item in range(100):
    if 20<=item<=80:
        continue
    print(item)


item_count=int(input("enter number of items"))
for item in range(item_count):

    item_price=int(input("enter the price of item"))
    print(item_price+item_count)



