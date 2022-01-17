# WRITE YOUR FUNCTIONS HERE

from ast import Num
from operator import index
from unicodedata import name


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def  add_or_remove_cash(pet_shop, num):
  pet_shop["admin"]["total_cash"] += num
  return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold" ] += num
    return pet_shop["admin"]["pets_sold" ]
 
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, name):
    no_of_breed = []
    for pet in pet_shop["pets"]:
        if pet ["breed"] == name:
            no_of_breed.append(name)
    return no_of_breed

def find_pet_by_name(pet_shop, name):
    found_pet= None
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            found_pet = pet
    return found_pet


def remove_pet_by_name(pet_shop, name):
        for pet in pet_shop["pets"] :
            if pet ["name"] == name:
                 pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    return pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, num):
    customers["cash"] -= num
    return customers["cash"]

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    return customers["pets"].append(new_pet)

def customer_can_afford_pet(customers, new_pet):
    if customers["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customers):
    # import pdb
    # pdb.set_trace()
    if pet==None: 
        return 
    else:
        if customer_can_afford_pet(customers,pet)==False:
            return 
        else:
            add_pet_to_customer(customers, pet)
            remove_pet_by_name(pet_shop, pet)
            remove_customer_cash(customers, pet["price"])
            add_or_remove_cash(pet_shop, pet["price"])
            increase_pets_sold(pet_shop, 1)
            return


