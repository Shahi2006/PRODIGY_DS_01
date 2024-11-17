import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("India population.csv")
# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(data['Year'], data['Population'], color='skyblue')
plt.title('India\'s Population Over the Years')
plt.xlabel('Year')
plt.ylabel('Population')
plt.tight_layout()
plt.show()
