import random
a = 'y'
while a == 'y':
    no = random.randint(1 , 6)
    if no == 1:
        print("[          ]")
        print("[    o   ]")
        print("[          ]")
    if no == 2:
        print("[o       ]")
        print("[          ]")
        print("[       o]")
    if no == 3:
        print("[          ]")
        print("[o o o]")
        print("[          ]")
    if no == 4:
        print("[o     o]")
        print("[          ]")
        print("[o     o]")
    if no == 5:
        print("[o     o]")
        print("[    o   ]")
        print("[o     o]")
    if no == 6:
        print("[o o o]")
        print("[          ]")
        print("[o o o]")

    a = input("press y to roll again and x to exit:")
    print("\n")

