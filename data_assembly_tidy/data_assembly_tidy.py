import pandas as pd


def main():


    # read the two csv files and replace null values with NaN
    lhr_visit_dom_dataframe = pd.read_csv("lhr_visit_dom.csv", na_values=["NaN"])
    lhr_visit_intl_dataframe = pd.read_csv("lhr_visit_intl.csv", na_values=["NaN"])


    # append two dataframes and reset index
    lhr_visits_dataframe = pd.concat([lhr_visit_dom_dataframe, lhr_visit_intl_dataframe], ignore_index=True)

    # Fill all missing values with zero
    lhr_visits_zero_replace_dataframe = lhr_visits_dataframe.fillna(value=0)

    print(lhr_visits_zero_replace_dataframe.head(10))
    # print(lhr_visit_dom_dataframe.head())

    # print("*****************************")

    # print(lhr_visit_intl_dataframe.head())


if __name__ == "__main__":
    main()