"""
    Script: Tax and Tip
    Description: This program ask user for cost of a meal ordered at a
                 restaurant.
                 The program then compute the tax and tip for the meal.
                 The program then displays the tip amount, tax amount,
                 and the grand total fo the meal including both the
                 tax and the tip.

    Programmer: William Kpabitey Kwabla.
    Date: 04/03/2020
"""

TIP_CONSTANT: float = 0.18
TAX_CONSTANT: float = 0.17


def ask_user_for_cost_of_meal_in_dollars():

    cost_of_meal = float(input("Enter price for meal: "))

    return cost_of_meal

def calculate_tax(meal_cost:float):

    total_tax = meal_cost * TAX_CONSTANT

    return total_tax

def calculate_tip(meal_cost:float):

    total_tip = meal_cost * TIP_CONSTANT

    return total_tip

def calculate_grand_total_for_meal(tip_total:float, tax_total:float):

    grand_total_for_meal:float = tip_total + tax_total

    return grand_total_for_meal

def display_grant_total_of_meal(grand_total_of_meal):

    print()

    print("The grand total for meal including tax and tip is $: {grand_total_of_meal}")

def main():
    pass

if __name__ == "__main__":
    main()