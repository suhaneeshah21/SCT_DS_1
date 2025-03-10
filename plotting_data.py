import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Time-Wasters on Social Media.csv')
plt.hist(df['Age'])
plt.title('Density of different age groups using social media')
plt.xlabel('Ages')
plt.show()
