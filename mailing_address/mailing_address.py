def display_name_and_mailing_address():

    name:str = "William Kpabitey Kwabla"

    street1_address:str = "530 South Donaghey Avenue Apt 600"

    city:str = "Conway"

    state:str = "AR"

    zip_code:str = "72034-7127"

    country:str = "United States"

    print(name)
    print(street1_address)
    print(f"{city}, {state} {zip_code}")
    print(country)


def main():
    display_name_and_mailing_address()

if __name__ == "__main__":
    main()