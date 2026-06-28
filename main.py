from agents.data_loading import load_data
from agents.inspector import inspect_data
from agents.cleaner import clean_data
from agents.transformer import transform_data
from agents.filter import filter_data

df = load_data()

inspect_data(df)

df = clean_data(df)

df = transform_data(df)

print("\nUpdated Dataset")
print(df.head())

topper, failed, attendance, study = filter_data(df)