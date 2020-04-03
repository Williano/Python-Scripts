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

    cost_of_meal = float(input("Enter price for meal $: "))

    return cost_of_meal

def calculate_tax(meal_cost:float):

    total_tax = meal_cost * TAX_CONSTANT

    return total_tax

def calculate_tip(meal_cost:float):

    total_tip = meal_cost * TIP_CONSTANT

    return total_tip

def calculate_grand_total_of_meal(tip_total:float, tax_total:float):

    grand_total_of_meal:float = tip_total + tax_total

    return grand_total_of_meal


def display_tax_total(tax_total:float):

    print()

    print(f"The total tax is $: {tax_total}")

def display_tip_total(tip_total:float):

    print()

    print(f"The total tip is $: {tip_total}")


def display_grand_total_of_meal(grand_total_of_meal:float):

    print()

    print(f"The grand total for meal including tax and tip is $: {grand_total_of_meal}")

def main():

    cost_of_meal:float = ask_user_for_cost_of_meal_in_dollars()

    tax_amount:float = calculate_tax(cost_of_meal)

    tip_amount:float = calculate_tip(cost_of_meal)

    grand_total_for_meal:float = calculate_grand_total_for_meal(tax_amount, tip_amount)

    display_tax_total(tax_amount)

    display_tip_total(tip_amount)

    display_grant_total_of_meal(grand_total_for_meal)


if __name__ == "__main__":
    main()