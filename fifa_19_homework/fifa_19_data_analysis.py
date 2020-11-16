import pandas as pd


def main():

    # load fifa 19 dataset
    fifa_19_dataset = pd.read_csv("fifa19_ver1.csv")

    fifa_19_dataset.head()



if __name__ == "__main__":
    main()
