import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/allan/OneDrive - SNHU/Classes/CS-350/stepping.csv')
df2 = pd.read_csv('C:/Users/allan/OneDrive - SNHU/Classes/CS-350/stepping2.csv')

plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], marker='', color='orange')
plt.plot(df2['x'], df2['y'], marker='', color='red')
plt.fill_between(df2['x'], df2['y'], 30, where=(df2['y'] > 30), interpolate=True, color='red', alpha=0.05)
plt.title('Duty Cycle Percentage Over TIme')
plt.xlabel('Time in Seconds')
plt.ylabel('Duty Cycle %')
plt.grid(True)
plt.show()


