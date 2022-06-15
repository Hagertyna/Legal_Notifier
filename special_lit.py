#special literals
drink = "Available"
food = None

def new_menu(a):
    if a == drink:
        print(drink)
    else:
        print(food)
        
new_menu(drink)
new_menu(food)
