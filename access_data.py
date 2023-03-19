import pandas as pd
import matplotlib.pyplot as plt

trends = pd.read_csv("Raw_Data/search-of-sauce-trends.csv")

df = pd.DataFrame(trends)

time = df['In Search Of Sauce'].tolist()
downloads =df['Unnamed: 1'].tolist()

curated_time = time[2:13]
curated_downloads = downloads[2:13]

plt.plot(curated_time, curated_downloads)


