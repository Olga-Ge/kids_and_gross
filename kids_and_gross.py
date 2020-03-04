while True:
    try:
        gross = input("How much are you making?")
        gross = int(gross)
        # if I am here, i have a proper number!
        if gross > 1000000 or gross < 0:
            print("you liar!")
            continue

        # tax = 0
        if gross < 1000:
            tax = 0.1
        elif gross < 2000:
            tax = 0.11
        elif gross < 4000:
            tax = 0.12
        else:
            tax = 0.14
        break
    except:
        print("that was not a good gross")

while True:
    try: # this one is to catch bad kids
        kids = input("how many kids do you know to have?")
        kids = int(kids)
        if gross < 2000:
            tax = tax - kids*0.01
        else:
            tax = tax - kids*0.005
        if tax < 0:
            print("hey there, bunny, need to put a stop")
            tax = 1

        net = gross*(1-tax)
        print("you take home", net, "euros/pesos/ruble/CHF/balboa")
        break
    except:
        print("that was not a real number for kids!")
