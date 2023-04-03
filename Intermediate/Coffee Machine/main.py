from string import capwords

import machine

resource = machine.resources
money = 0


def coffee_machine():
    global resource
    global money
    user_input = input("What would you like? (espresso/latte/cappuccino):   ")

    if user_input.lower() == 'report':
        for i in resource:
            if i == 'coffee':
                print(f"{capwords(i)} : {resource[i]}g")
            else:
                print(f"{capwords(i)} : {resource[i]}ml")
        print(f"Money : ${money}")

    else:
        temp = machine.MENU[user_input.lower()]
        scarce_resource = 'Null'
        old_resource = resource.copy()
        for i in resource:
            for j in temp["ingredients"]:
                if i == j:
                    if resource[i] >= temp['ingredients'][j]:
                        resource[i] -= temp['ingredients'][j]
                    else:
                        scarce_resource = i
                        break
        if scarce_resource != 'Null':
            print(f"Sorry, There is not enough {scarce_resource}.")
            resource = old_resource.copy()
        else:
            quarter = int(input("Please insert coins.\nHow many quarters?:    "))
            dime = int(input("How many dimes?:  "))
            nickle = int(input("How many nickles?:  "))
            penny = int(input("How many pennies?:   "))
            amount_collected = (0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny)
            if amount_collected < temp['cost']:
                print("Sorry that's not enough money. Money refunded.")
                resource = old_resource.copy()
            else:
                money += temp['cost']
                print(f"Here is ${round(amount_collected - temp['cost'],2)} in change.")
                print(f"Here is your {capwords(user_input)} ☕️. Enjoy!")


while True:
    coffee_machine()
