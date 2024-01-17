# exceptions are computanionally costly
# a good approach is to return a simple text error or None instead
# also using the pass statement will skip program exceution when condition is accomplish
for number in range(1, 71):
    if number % 7 != 0:
        # the number is not a multiple of 7
        pass
    else:
        print(f'{number} is a multiple of 7')
