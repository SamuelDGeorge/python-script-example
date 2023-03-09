import pandas as pd

my_data = pd.read_excel("Fruit_Dataset.xlsx")

my_raw_data = [
    {
    "a":1,
    "b":1
    }
]

empty_data = pd.DataFrame.from_records(my_raw_data)

print(empty_data)