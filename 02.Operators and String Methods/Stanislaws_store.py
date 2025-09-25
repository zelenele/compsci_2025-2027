def membership_discount(value_of_items):
    membership_discount_value = value_of_items * 0.2
    return membership_discount_value

def discount_check(membership_card):
    if membership_card == True:
        return True
    else:
        return False
    
def shopping_experience(value_of_items, is_a_member):
    if discount_check(is_a_member):
        total_cost = value_of_items - membership_discount(value_of_items)
        return total_cost 
    else:
        return value_of_items
    
print(shopping_experience(170, True))