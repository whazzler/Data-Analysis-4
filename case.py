import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')

race_counts = df['Country'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(20, 15))
race_counts.plot(kind='pie', color='skyblue', ax=ax)

ax.set_title('Number of People by Country', fontsize=14, fontweight='bold')
ax.set_xlabel('Race/Ethnicity Group', fontsize=12)
ax.set_ylabel('Student Count', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('Countries.png')
plt.close()

plt.figure(figsize=(8, 5))
