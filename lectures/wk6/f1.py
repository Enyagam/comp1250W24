def display_name():
    return "Ben Blanc"


def country_population(country):  # parameters: local variables only available in function body
    if country == "canada":
        return "40 million"
    elif country == "usa":
        return "300 million"
    else:
        return "Unknown"



def order_pizza(toppings="cheese", size="small"):
    return f"Your {size} pizza of {toppings} toppings is ready"


pepperoni_pizza1 = order_pizza("cheese, pepperoni", "medium")
cheese_pizza = order_pizza(size="large", toppings="cheese, double cheese")
# named arguments to pass values to the function
# Woah, woah, woah! What is an argument: a value that you pass to a parameter

pizza = order_pizza()
print(pizza)
print(cheese_pizza)
print(pepperoni_pizza1)
canada_population = country_population("canada")
print(canada_population)
name = display_name()
print(name)