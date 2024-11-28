colors = ['red', 'green', 'blue', 'yellow', 'pink', 'magenta', 'aliceblue', 'aqua', 'purple', 'indigo','violet']
i = 1
for color in colors:
    print(f"{i}. {color}")  # for loop in lists will print all the list items present in the list.
    i += 1
    if color == colors[4] or color == 'green':
        print('this is a special color')
        print()
