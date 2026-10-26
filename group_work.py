import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('drinks.csv')

df['(healthiness)/10'].plot(kind='hist', bins=7, color='teal', edgecolor='black')

plt.title('(healthiness)/10')
plt.xlabel('healthiness')
plt.ylabel('/10')
plt.grid(axis='y', linestyle='--', alpha=0.9)

plt.tight_layout()
plt.savefig('(healthiness)/10.png')
# plt.show()
plt.close()
