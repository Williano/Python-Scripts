import pandas as pd


def main():


    # read the two csv files and replace null values with NaN
    lhr_visit_dom_dataframe = pd.read_csv("lhr_visit_dom.csv", na_values=["NaN"])
    lhr_visit_intl_dataframe = pd.read_csv("lhr_visit_intl.csv", na_values=["NaN"])


    # append two dataframes and reset index
    lhr_visits_dataframe = pd.concat([lhr_visit_dom_dataframe, lhr_visit_intl_dataframe], ignore_index=True)

    # Fill all missing values with zero
    lhr_visits_zero_replace_dataframe = lhr_visits_dataframe.fillna(value=0)

    # Save merged data to csv with no index
    lhr_visits_zero_replace_dataframe.to_csv("lhr_visits.csv", index=False)

    # Load saved file into visits dataframe
    visits_dataframe = pd.read_csv("lhr_visits.csv")

    # Melt the data columns into visit length and count
    visits_melted_dataframe = visits_dataframe.melt(
        id_vars=["type"],
        value_vars=[
        "Up to 12 hrs", "Over 12 hrs to 1 day",
        "Over 1 day to 2 days" , "Over 2 days to 3 days",
        "Over 3 days to 4 days", "Over 4 days to 5 days",
        "Over 5 days to 6 days", "Over 6 days to 1 week",
        "Over 1 week to 2 weeks", "Over 2 weeks to 3 weeks",
        "Over 3 weeks to 4 weeks", "Over 4 weeks"],
        var_name="visit_length", value_name="count")

    print(visits_melted_dataframe.head(100))
    # print(lhr_visit_dom_dataframe.head())

    # print("*****************************")

    # print(lhr_visit_intl_dataframe.head())


if __name__ == "__main__":
    main()