# WRITE YOUR FUNCTIONS HERE
import pdb

#1 find the name of the pet shop
def get_pet_shop_name(pet_shop_info):
    name = pet_shop_info["name"]
    return name

#2 find the total cash
def get_total_cash(pet_shop_info):
    total_cash = pet_shop_info["admin"]["total_cash"]
    return total_cash

#3 + #4 add or remove cash
def add_or_remove_cash(pet_shop_info, cash_amount):
    pet_shop_info["admin"]["total_cash"] = pet_shop_info["admin"]["total_cash"] + cash_amount

#5 find how many pets have sold
def get_pets_sold(pet_shop_info):
    return pet_shop_info["admin"]["pets_sold"]

#6 increase number of pets sold
def increase_pets_sold(pet_shop_info, pets_sold):
    pet_shop_info["admin"]["pets_sold"] += pets_sold

#7 find the stock count
def get_stock_count(pet_shop_info):
    return len(pet_shop_info["pets"])

#8 + #9 
# find how many there are of a given breed
def get_pets_by_breed(pet_shop_info, breed):
    #pdb.set_trace()
    x = 0
    number_of_breeds = []
    while x < 6:
        if pet_shop_info["pets"][x]["breed"] == breed:
            number_of_breeds.append(pet_shop_info["pets"][x])
        x = x + 1
    return number_of_breeds

#10 + #11
def find_pet_by_name(pet_shop_info, name):
    x = 0
    while x < 6:    
        if pet_shop_info["pets"][x]["name"] == name:
            return pet_shop_info["pets"][x]["name"]
        x = x + 1
    return 0



        

    
    







