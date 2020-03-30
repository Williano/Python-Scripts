
def enter_user_name():

    try:
        user_name = str(input("Please enter your name: "))
    except Exception as e:
        print(e)

    return user_name


def display_hello_with_user_name(user_name:str):

    print(f"Hello, {user_name} !")

def main():

    user_name = enter_user_name()

    display_hello_with_user_name(user_name)


if __name__ == "__main__":
    main()