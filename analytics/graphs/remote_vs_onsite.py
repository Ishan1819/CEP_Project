import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import seaborn as sns

#3. stacked chart for remote vs. on-site jobs
job_data = {
    "Software Engineer": ("Tech", 70, 30),
    "Data Scientist": ("Tech", 65, 35),
    "Cybersecurity Analyst": ("Tech", 60, 40),
    "AI/ML Engineer": ("Tech", 75, 25),
    "Cloud Engineer": ("Tech", 72, 28),
    "Digital Marketer": ("Marketing", 80, 20),
    "UX/UI Designer": ("Design", 78, 22),
    "Content Creator": ("Media", 85, 15),
    "Financial Analyst": ("Finance", 50, 50),
    "Accountant": ("Finance", 55, 45),
    "Healthcare Professional": ("Healthcare", 20, 80),
    "Nurse": ("Healthcare", 10, 90),
    "Doctor": ("Healthcare", 5, 95),
    "Teacher": ("Education", 30, 70),
    "Professor (University)": ("Education", 40, 60),
    "Sales Manager": ("Sales", 50, 50),
    "Retail Manager": ("Retail", 25, 75),
    "Logistics Manager": ("Supply Chain", 30, 70),
    "Civil Engineer": ("Engineering", 15, 85),
    "Mechanical Engineer": ("Engineering", 20, 80),
    "Automotive Engineer": ("Automotive", 25, 75),
    "Construction Manager": ("Construction", 10, 90),
    "Lawyer": ("Legal", 35, 65),
    "Social Worker": ("Non-Profit", 20, 80),
    "Customer Support Rep.": ("Customer Service", 60, 40),
}

def generate_remote_vs_onsite_chart():
    """
    Generates a stacked bar chart for remote vs. on-site job distributions.
    """
    careers = list(job_data.keys())
    remote_percentages = [job_data[career][1] for career in careers]
    onsite_percentages = [job_data[career][2] for career in careers]

    plt.figure(figsize=(12, 6))
    plt.bar(careers, remote_percentages, label="Remote Jobs", color="skyblue")
    plt.bar(careers, onsite_percentages, bottom=remote_percentages, label="On-Site Jobs", color="orange")

    plt.xlabel("Careers", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.title("Remote vs. On-Site Jobs by Career", fontsize=14)
    plt.xticks(rotation=75, fontsize=10)
    plt.legend()

    # Convert to Base64 image
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return image_base64