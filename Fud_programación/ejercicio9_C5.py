import random
for i in range(21):
    for j in range(21):
        pixel = random.randint(0,1)
        if pixel == 1:
            print("# ", end="")
        else:
            print("  ", end="")
    print("")
