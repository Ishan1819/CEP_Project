# from fastapi import APIRouter, Query
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import seaborn as sns
# router = APIRouter()

#1. Job market data (static for now, can be updated dynamically later)
def generate_pie_chart():
    """
    Fetches job market demand data and generates a pie chart as a Base64-encoded image.
    """
    
    job_data = {
        "Tech": 15,
        "Healthcare": 10,
        "Finance": 12,
        "Education": 7,
        "Retail": 14,
        "Telecom": 11,
        "Advertising & PR": 6,
        "Logistics & Transportation": 5,
        "Automotive": 3,
        "Energy": 2,
    }
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))
    labels = list(job_data.keys())
    sizes = list(job_data.values())
    colors = plt.cm.Paired(range(len(labels)))
    
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title("Job Market Demand by Industry (2025)", fontsize=14)
    
    # Convert figure to Base64 image
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return image_base64