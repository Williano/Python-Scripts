"""
    Script: Area of  a Field
    Description: A python program that reads the length and width of a farmer’s
                 field from the user in feet and Display the area of the field
                 in acres.
    Programmer: William Kpabitey Kwabla
    Date: 04/01/20
"""

ONE_ARCE_CONSTANT:int = 43560

def get_length_and_width_of_field_from_user():

    length:float = float(input("Enter the length of the field in meters: "))
    width:float = float(input("Enter the width of the field in meters: "))

    return length, width

def calculate_area_of_field_in_feet(length:float, width:float):

   area_in_feet:float = length * width

   return area_in_feet


def convert_area_from_feet_to_arces(area_in_feet:float):

    pass

def display_area_of_field(area:float):

    print()
    print(f"The area of the field is {area} arces")

def main():

    length, width = get_length_and_width_of_field_from_user()

    area:float = calculate_area_of_field_in_feet(length, width)

    display_area_of_field(area)

if __name__ == "__main__":
    main()
