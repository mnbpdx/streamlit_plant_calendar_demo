import streamlit as st
from datetime import datetime
import calendar

# Dummy backend data
dummy_backend = {
    "January": {
        "Seed indoor": ["Tomatoes", "Peppers", "Eggplants"],
        "Seed outdoor": ["Winter Lettuce", "Spinach"],
        "Plant starts": []
    },
    "February": {
        "Seed indoor": ["Cucumbers", "Melons", "Squash"],
        "Seed outdoor": ["Peas", "Radishes"],
        "Plant starts": ["Onions"]
    },
    "March": {
        "Seed indoor": ["Herbs", "Broccoli", "Cauliflower"],
        "Seed outdoor": ["Carrots", "Beets"],
        "Plant starts": ["Potatoes"]
    },
    # Add more months as needed
}

# Dummy plant information
plant_info = {
    "Tomatoes": "Warm-season crop, needs full sun and well-drained soil.",
    "Peppers": "Requires warm soil and full sun. Harvest when fully colored.",
    "Eggplants": "Needs warm temperatures and full sun. Harvest when glossy.",
    "Winter Lettuce": "Cool-season crop, tolerates light frost. Harvest outer leaves.",
    "Spinach": "Fast-growing, cool-season crop. Rich in iron and vitamins.",
    # Add info for other plants
}

# Function to get tasks for a specific month
def get_tasks_for_month(month):
    return dummy_backend.get(month, {
        "Seed indoor": [],
        "Seed outdoor": [],
        "Plant starts": []
    })

# Set page config
st.set_page_config(page_title="Monthly Gardening Task Manager", layout="wide")

# Custom CSS to reduce spacing
st.markdown("""
<style>
    .stCheckbox {
        margin-right: -20px;
    }
    .stButton > button {
        margin-left: -20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for month selection
current_date = datetime.now()
months = list(calendar.month_name)[1:]
selected_month = st.sidebar.selectbox("Select Month", months, index=current_date.month - 1)
selected_year = st.sidebar.number_input("Select Year", min_value=2000, max_value=2100, value=current_date.year)

# Main app
st.header(f"{selected_month} {selected_year}")

# Get tasks for the selected month
monthly_tasks = get_tasks_for_month(selected_month)

# Create a placeholder for the info bubble
info_bubble = st.empty()

# Display tasks for each category
categories = ["Seed indoor", "Seed outdoor", "Plant starts"]
for category in categories:
    st.subheader(category)
    tasks = monthly_tasks[category]
    
    if tasks:
        for task in tasks:
            col1, col2 = st.columns([1, 20])
            with col1:
                st.checkbox("", key=f"{category}_{task}_done")
            with col2:
                if st.button(task, key=f"{category}_{task}"):
                    if task in plant_info:
                        info_bubble.info(plant_info[task])
                    else:
                        info_bubble.error("No information available for this plant.")
    else:
        st.write("No tasks in this category for this month.")
