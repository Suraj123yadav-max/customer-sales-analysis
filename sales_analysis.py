import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 250, 300, 280, 350, 400],
    "Product_A": [80, 90, 100, 110, 130, 150],
    "Product_B": [120, 160, 200, 170, 220, 250]
}

df = pd.DataFrame(data)

print("Total Sales:", df["Sales"].sum())

plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.bar(df["Month"], df["Product_A"], label="Product A")
plt.bar(df["Month"], df["Product_B"], bottom=df["Product_A"], label="Product B")
plt.legend()
plt.title("Product-wise Sales")
plt.show()