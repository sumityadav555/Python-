This is module in python which is used to seriealized and deserialized object in python.
The process of convertion python into bytes is known as pickle where as The reverse process is known as unpickling

import pickle

data = {"name": 'sumit', "age" = 25}

# with open ('data.pkl', 'wb') as file:
#     pickle.dump(data, file)

with open ('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

import pickle

data = {"name": "Diana", "age": 28}

# Using Pickler for serialization
with open("data_custom.pkl", "wb") as file:
    pickler = pickle.Pickler(file)
    pickler.dump(data)

