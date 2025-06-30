import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/storage/emulated/0/Download/100 Sales Records.csv')
g= df.groupby('Units Sold')['Unit Price'].sum()
g.plot(kind='bar')
plt.title('Total Sales by Product')
plt.ylabel('Sales')
plt.xlabel('Price')
plt.tight_layout()
plt.show()