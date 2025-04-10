import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import seaborn as sns

recession_data = {
    "Tech": [10, 15, 25],
    "Finance": [20, 10, 15],
    "Retail": [15, 30, 10],
    "Construction": [25, 20, 12],
    "Manufacturing": [18, 22, 10],
    "Hospitality": [12, 40, 8],
    "Healthcare": [5, 8, 4],
    "Education": [3, 5, 2],
}

years = ["2008 Recession", "2020 COVID", "2023 Tech Layoffs"]
industries = list(recession_data.keys())
values = np.array(list(recession_data.values()))

def generate_recession_graph():
    """
    Generates a grouped bar chart showing job losses in different industries across recessions.
    """
    bar_width = 0.2
    x = np.arange(len(industries))

    plt.figure(figsize=(12, 6))
    
    for i, year in enumerate(years):
        plt.bar(x + i * bar_width, values[:, i], width=bar_width, label=year)

    plt.xlabel("Industries")
    plt.ylabel("Job Loss Percentage (%)")
    plt.title("Industries Most Affected During Recessions")
    plt.xticks(x + bar_width, industries, rotation=45, ha="right")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Convert plot to Base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return image_base64

