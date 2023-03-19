import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name':['Ryan', 'Ryans brother', 'Ryans Sister', 'Ryans mum', 'Ryans dad'],
    'Coolness Level':[0,7,7,10,10],
    'Number of Friends':[1,23,18,103,23]
}

df = pd.DataFrame(data)

print(df)