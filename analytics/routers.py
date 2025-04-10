from fastapi import APIRouter, Query
from backend.analytics.graphs.job_market import generate_pie_chart
from backend.analytics.graphs.recession_impact import generate_recession_graph
import backend.analytics.graphs.automation_risk as automation_risk
from backend.analytics.graphs.career_trends import generate_career_trend_graph
from backend.analytics.graphs.remote_vs_onsite import generate_remote_vs_onsite_chart
router = APIRouter()


@router.get("/analytics/recession_impact")
async def get_recession_graph():
    """
    Endpoint to return the recession impact graph as a base64 image.
    """
    image_base64 = generate_recession_graph()
    return {"image": f"data:image/png;base64,{image_base64}"}


@router.get("/analytics/job_market_pie_chart")
async def get_job_market_pie_chart():
    """
    Returns the job market demand pie chart as a base64 encoded image.
    """
    image_base64 = generate_pie_chart()
    return {"image": f"data:image/png;base64,{image_base64}"}


@router.get("/analytics/trending_careers")
async def get_trending_careers(year: int = Query(2024, description="Select a year"), chart_type: str = Query("bar", description="Select chart type (bar/line)")):
    """
    Returns a graph (bar/line) for the top 10 trending careers in a selected year.
    """
    image_base64 = generate_career_trend_graph(year, chart_type)

    if not image_base64:
        return {"error": "Data not available for the selected year"}

    return {"image": f"data:image/png;base64,{image_base64}"}


@router.get("/analytics/remote_vs_onsite")
async def get_remote_vs_onsite_chart():
    """
    Returns a stacked bar chart for remote vs. on-site job percentages across different careers.
    """
    image_base64 = generate_remote_vs_onsite_chart()
    return {"image": f"data:image/png;base64,{image_base64}"}


@router.get("/analytics/career_bubble_chart")
async def get_career_bubble_chart():
    """
    Endpoint to return the career bubble chart as a base64 image.
    """
    image_base64 = generate_career_bubble_chart()
    return {"image": f"data:image/png;base64,{image_base64}"}