from agents.data_loading import load_data
from agents.inspector import inspect_data
from agents.cleaner import clean_data

df = load_data()

inspect_data(df)

df = clean_data(df)