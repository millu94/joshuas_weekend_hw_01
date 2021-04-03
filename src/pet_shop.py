# WRITE YOUR FUNCTIONS HERE

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








