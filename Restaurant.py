print("Welcome to the Everything Restaurant")
print("======================================")

# Prices in USD
heavy_food = 5.00
light_food = 2.50
plain_warm_drink = 0.50
sweet_warm_drink = 1.00
plain_cold_drink = 1.00
sweet_cold_drink = 1.50

total_price = 0.0

while True:
    print("Choose a menu:")
    print("1. Food")
    print("2. Drinks")
    print("3. Finish")
    menu = input("Select the menu you want to buy: ")

    if menu == '3':
        print(f"Total amount you have to pay: ${total_price:.2f}")
        print("Thank you for visiting the Everything Restaurant!")
        print("======================================")
        break

    elif menu == '1':
        print("1. Heavy Food")
        print("2. Light Food")
        food = input("Choose the type of food: ")

        if food == '1':
            food = input("Enter the name of the food: ")
            total_price += len(food) * heavy_food
            print(f"The price of the food you bought is ${len(food) * heavy_food:.2f}")
        elif food == '2':
            food = input("Enter the name of the food: ")
            total_price += len(food) * light_food
            print(f"The price of the food you bought is ${len(food) * light_food:.2f}")

    elif menu == '2':
        print("1. Warm Drink")
        print("2. Cold Drink")
        drink_temp = input("Choose the drink temperature: ")

        if drink_temp == '1':
            print("1. Plain Drink")
            print("2. Sweet Drink")
            drink_flavor_warm = input("Choose the drink flavor: ")

            if drink_flavor_warm == '1':
                drink = input("Enter the name of the drink: ")
                total_price += len(drink) * plain_warm_drink
                print(f"The price of the drink you bought is ${len(drink) * plain_warm_drink:.2f}")
            elif drink_flavor_warm == '2':
                drink = input("Enter the name of the drink: ")
                total_price += len(drink) * sweet_warm_drink
                print(f"The price of the drink you bought is ${len(drink) * sweet_warm_drink:.2f}")

        elif drink_temp == '2':
            print("1. Plain Drink")
            print("2. Sweet Drink")
            drink_flavor_cold = input("Choose the drink flavor: ")

            if drink_flavor_cold == '1':
                drink = input("Enter the name of the drink: ")
                total_price += len(drink) * plain_cold_drink
                print(f"The price of the drink you bought is ${len(drink) * plain_cold_drink:.2f}")
            elif drink_flavor_cold == '2':
                drink = input("Enter the name of the drink: ")
                total_price += len(drink) * sweet_cold_drink
                print(f"The price of the drink you bought is ${len(drink) * sweet_cold_drink:.2f}")

    else:
        print("Invalid choice.")
        print("======================================")
