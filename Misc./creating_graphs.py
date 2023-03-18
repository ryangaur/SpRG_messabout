import matplotlib.pyplot as plt


# y xis
y = [1,3,5,9,11,13,17,21]

# create x axis 
x = []
for i in range(len(y)):
    x.append(i)

plt.plot(x, y)
plt.show()