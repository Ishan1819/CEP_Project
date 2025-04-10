import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import seaborn as sns
#2. Different top 10 trending careers for each year (2015 - 2024)
job_trends = {
    2015: {"Software Engineer": 50000, "Teacher": 45000, "Civil Engineer": 30000, "Retail Manager": 35000, "Pharmacist": 32000,
           "HR Specialist": 29000, "Graphic Designer": 27000, "Construction Manager": 25000, "Accountant": 23000, "Sales Executive": 22000},

    2016: {"Software Engineer": 52000, "Nurse": 48000, "Financial Analyst": 31000, "Marketing Executive": 33000, "Cybersecurity Analyst": 28000,
           "HR Specialist": 27000, "Graphic Designer": 26000, "Construction Manager": 24000, "Data Entry Operator": 22000, "Mechanical Engineer": 21000},

    2017: {"Data Scientist": 55000, "Nurse": 49000, "Digital Marketer": 35000, "Cybersecurity Analyst": 30000, "AI Engineer": 27000,
           "Software Engineer": 26000, "Accountant": 25000, "Teacher": 24000, "HR Manager": 23000, "Architect": 22000},

    2018: {"AI Engineer": 60000, "Data Scientist": 57000, "Software Developer": 45000, "Doctor": 42000, "Content Creator": 32000,
           "Social Media Manager": 31000, "Blockchain Developer": 29000, "Pharmacist": 27000, "Teacher": 25000, "Automotive Engineer": 23000},

    2019: {"Cybersecurity Analyst": 65000, "AI Engineer": 60000, "Digital Marketer": 48000, "Software Engineer": 45000, "Doctor": 40000,
           "Nurse": 39000, "Data Analyst": 37000, "HR Manager": 35000, "Web Developer": 33000, "Retail Manager": 31000},

    2020: {"Cloud Engineer": 70000, "AI Engineer": 65000, "Cybersecurity Analyst": 60000, "Software Developer": 55000, "Nurse": 50000,
           "Doctor": 48000, "Content Creator": 45000, "Pharmacist": 40000, "Digital Marketer": 35000, "Social Worker": 30000},

    2021: {"AI Engineer": 80000, "Data Scientist": 75000, "Software Engineer": 70000, "Machine Learning Engineer": 67000, "Cybersecurity Expert": 64000,
           "Doctor": 60000, "Nurse": 57000, "Cloud Engineer": 55000, "Marketing Manager": 50000, "E-commerce Specialist": 48000},

    2022: {"Blockchain Developer": 85000, "AI Engineer": 80000, "Cybersecurity Expert": 75000, "Software Engineer": 70000, "Data Scientist": 67000,
           "Doctor": 65000, "Machine Learning Engineer": 63000, "Nurse": 60000, "Cloud Engineer": 58000, "FinTech Specialist": 56000},

    2023: {"AI Engineer": 90000, "Cybersecurity Expert": 85000, "Blockchain Developer": 80000, "Machine Learning Engineer": 75000, "Data Analyst": 70000,
           "Software Engineer": 67000, "Doctor": 65000, "E-commerce Specialist": 60000, "UX/UI Designer": 57000, "Cloud Security Engineer": 55000},

    2024: {"Quantum Computing Engineer": 95000, "AI Engineer": 90000, "Blockchain Developer": 85000, "Cybersecurity Expert": 80000, "Machine Learning Engineer": 78000,
           "Software Engineer": 75000, "Data Scientist": 70000, "Bioinformatics Specialist": 67000, "Cloud Engineer": 65000, "Doctor": 60000},
}

def generate_career_trend_graph(year: int, chart_type: str):
    """
    Generates a bar or line chart showing the top 10 trending careers in a given year.
    """
    if year not in job_trends:
        return None  # Year not available

    careers = list(job_trends[year].keys())
    opportunities = list(job_trends[year].values())

    # Plot the graph
    plt.figure(figsize=(10, 6))

    if chart_type == "bar":
        plt.bar(careers, opportunities, color="skyblue")
    else:
        plt.plot(careers, opportunities, marker="o", linestyle="-", color="blue")

    plt.xlabel("Careers")
    plt.ylabel("Job Opportunities")
    plt.title(f"Top 10 Trending Careers in {year}")
    plt.xticks(rotation=45)

    # Convert to Base64 image
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return image_base64