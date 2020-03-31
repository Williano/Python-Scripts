"""
    Script: Area of  a Room
    Description: A python program that ask user for lenght and width of a room
                 and compute the area of the room with the user inputs.
    Programmer: William Kpabitey Kwabla
    Date: 03/31/20
"""


def get_length_and_width_of_room_from_user():

    length:float = float(input("Enter the length of the room in meters: "))
    width:float = float(input("Enter the width of the room in meters: "))

    return length, width

def calculate_area_of_room(length:float, width:float):

   area:float = length * width

   return area

def display_area_of_room(area:float):

    print()
    print(f"The area of the room is {area} meters")

def main():

    length, width = get_length_and_width_of_room_from_user()

    area:float = calculate_area_of_room(length, width)

    display_area_of_room(area)

if __name__ == "__main__":
    main()
