import pandas as pd
import matplotlib.pyplot as plt

# EXAMPLE 1
# y xis
y = [1,3,5,9,11,13,17,21]

# create x axis 
x = []
for i in range(len(y)):
    x.append(i)
# plot
fig1 = plt.figure()
plt.plot(x, y)



# EXAMPLE 2
# Data in a dictionary of lists
data = {
    'Name':['Ryan', 'Ryans brother', 'Ryans Sister', 'Ryans mum', 'Ryans dad'],
    'Coolness Level':[0,7,7,10,10],
    'Number of Friends':[1,23,18,103,23]
}

df = pd.DataFrame(data)

# put each column in it's own list
name = df['Name'].tolist()
coolness = df['Coolness Level'].values
friends = df['Number of Friends'].values

# plot
fig2 = plt.figure()
plt.plot(name, coolness)
plt.plot(name, friends)
plt.show()
