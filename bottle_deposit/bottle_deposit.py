"""
    Script: Bottle Deposits

    Description: In many jurisdictions a small deposit is added to drink
                 containers to encourage people to recycle them. In one
                 particular jurisdiction, drink containers holding one liter or
                 less have a $0.10 deposit, and drink containers holding more
                 than one liter have a $0.25 deposit.

                 This program reads the number of containers of each size from
                 the user.
                 The program then continue by computing and displaying the
                 refund that will be received for returning those containers.
                 It formats the output so that it includes a dollar sign and
                 always displays exactly two decimal places.

    Programmer: William Kpabitey Kwabla
    Date: 03/31/20
"""

ONE_LITER_CONSTANT: float = 0.10
MORE_THAN_ONE_LITER_CONSTANT: float = 0.25

def get_number_of_containers_of_each_size_from_user():

    number_of_one_liter_containers =  int(input("Enter the number of one liter containers: "))

    number_of_more_than_one_liter_containers =  int(input("Enter the number_of_more_than_one_liter_containers: "))

    return number_of_one_liter_containers, number_of_more_than_one_liter_containers

def compute_refund_for_each_container_size(number_of_one_liter_containers, number_of_more_than_one_liter_containers):

    total_refund_for_one_liter_containers = number_of_more_than_one_liter_containers * ONE_LITER_CONSTANT

    total_refund_for_more_than_one_liter_containers = number_of_more_than_one_liter_containers * MORE_THAN_ONE_LITER_CONSTANT

    return total_refund_for_one_liter_containers, total_refund_for_more_than_one_liter_containers

def display_refund_for_each_container_size_in_dollars():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
