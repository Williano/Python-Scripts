import pandas as pd


def main():


    # read the two csv files and replace null values with NaN
    lhr_visit_dom_dataframe = pd.read_csv("lhr_visit_dom.csv", na_values=["NaN"])
    lhr_visit_intl_dataframe = pd.read_csv("lhr_visit_intl.csv", na_values=["NaN"])



    # print(lhr_visit_dom_dataframe.head())

    # print("*****************************")

    # print(lhr_visit_intl_dataframe.head())


if __name__ == "__main__":
    main()