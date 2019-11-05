def test():
    i = 0   
    while True:
        i += 1
        print(i)
        if i == 5:
            return 'over'

print(test())
