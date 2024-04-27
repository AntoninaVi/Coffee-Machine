t_money = 550
t_water = 400
t_milk = 540
t_coffee = 120
t_cup = 9

def statecoffemachine():
    print("The coffee machine has:")
    print(f"{t_water} ml of water")
    print(f"{t_milk} ml of milk")
    print(f"{t_coffee} g of coffee beans")
    print(f"{t_cup} disposable cups")
    print(f"${t_money} of money")

def makeespresso():
    global t_water, t_coffee, t_money, t_cup
    t_water -= 250
    t_coffee -= 16
    t_cup -= 1
    t_money += 4

def makelatte():
    global t_water, t_coffee, t_milk, t_money, t_cup
    t_water -= 350
    t_milk -= 75
    t_coffee -= 20
    t_cup -= 1
    t_money += 7

def makecappuccino():
    global t_water, t_coffee, t_milk, t_money, t_cup
    t_water -= 200
    t_milk -= 100
    t_coffee -= 12
    t_cup -= 1
    t_money += 6

def buycoffee(t):
    if t == 1:
        makeespresso()
    elif t == 2:
        makelatte()
    elif t == 3:
        makecappuccino()

def fillproduct():
    global t_water, t_coffee, t_milk, t_money, t_cup
    print("Write how many ml of water you want to add:")
    w = int(input())
    t_water += w
    print("Write how many ml of milk you want to add:")
    m = int(input())
    t_milk += m
    print("Write how many grams of coffee beans you want to add:")
    cb = int(input())
    t_coffee += cb
    print("Write how many disposable cups you want to add: ")
    cup = int(input())
    t_cup += cup

def takemoney():
    global t_money
    print(f"I gave you ${t_money}")
    t_money = 0

if __name__ == "__main__":
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            n = input()
            if n == "back":
                continue
            n = int(n)
            if n not in [1, 2, 3]:
                continue
            if n == 1 and t_water < 250 or t_coffee < 16:
                print("Sorry, not enough water or coffee beans!")
                continue
            if n == 2 and (t_water < 350 or t_milk < 75 or t_coffee < 20):
                print("Sorry, not enough water, milk, or coffee beans!")
                continue
            if n == 3 and (t_water < 200 or t_milk < 100 or t_coffee < 12):
                print("Sorry, not enough water, milk, or coffee beans!")
                continue
            print("I have enough resources, making you a coffee!")
            buycoffee(n)
        elif action == "take":
            takemoney()
        elif action == "fill":
            fillproduct()
        elif action == "remaining":
            statecoffemachine()
        elif action == "exit":
            break
