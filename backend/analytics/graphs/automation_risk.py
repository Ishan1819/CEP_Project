import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import seaborn as sns


careers = [
    ("Data Scientist", 50, 10, 1.5),
    ("AI Engineer", 50, 5, 0.8),
    ("Accountant", 20, 69, 1.4),
    ("Retail Cashier", 10, 81, 3.3),
    ("Factory Worker", 8, 78, 12.5),
    ("Medical Doctor", 60, 2, 1.2),
    ("Lawyer", 40, 23, 1.0),
    ("Software Engineer", 50, 4, 1.8),
    ("Graphic Designer", 30, 47, 0.3),
    ("Construction Worker", 45, 88, 7.4),
    ("Administrative Assistant", 15, 96, 2.6),
    ("Financial Analyst", 35, 23, 0.3),
    ("Pharmacist", 40, 3, 0.3),
    ("Teacher", 35, 1, 3.8),
]

# Extract values for plotting
career_names, lifespans, automation_risks, workers = zip(*careers)

# Normalize bubble sizes (for better visualization)
bubble_sizes = [w * 100 for w in workers]

# Plot the Bubble Chart
plt.figure(figsize=(12, 8))
sns.scatterplot(x=lifespans, y=automation_risks, size=bubble_sizes, sizes=(50, 1000), hue=career_names, palette="tab10", alpha=0.7, edgecolor="black")

# Labels and title
plt.xlabel("Career Lifespan (Years)", fontsize=12)
plt.ylabel("Automation Risk (%)", fontsize=12)
plt.title("Career Lifespan vs. Automation Risk", fontsize=14)
plt.legend(loc="upper right", bbox_to_anchor=(1.35, 1), title="Careers")
plt.grid(True, linestyle="--", alpha=0.5)

# Show plot
plt.show()
