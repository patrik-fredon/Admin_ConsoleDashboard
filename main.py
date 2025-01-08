# main.py
from datetime import datetime

import pandas as pd
import streamlit as st


# Load the data
t = "./data/data.csv"
data = pd.read_csv(t)

st.title("Dashboard Fredon")
st.subheader("Useful, fast and simple dash for Fredons sites")

# Display the current date
current_date = datetime.today().strftime("%Y-%m-%d")
st.write(f"Current date: {current_date}")

# Display the first few rows of the data
st.subheader("Data Preview")
st.write(data.head())

page = st.sidebar.selectbox("Choose a page", ["Dashboard", "Blog", "Products", "Monitoring"])

if page == "Dashboard":
    st.sidebar("Dashboard")
elif page == "Blog":
    st.sidebar("Blog Posts")
    # Add your blog posts here
elif page == "Products":
    st.sidebar("Products")
    # Add your products here
elif page == "Monitoring":
    st.sidebar("Monitoring")
    # Add your monitoring here


# Check if "date" column exists in the DataFrame
if "date" in data.columns:
    # Convert "date" column to datetime

    try:
        data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
        st.success("Date column successfully converted to datetime.")
    except ValueError as e:
        st.error(f'Error converting "date" column: {e}')
else:
    st.warning('No "date" column found in the data.')



# Display data info
st.subheader("Data Info")
st.write(data.info())

# You can add more visualizations or analysis here

# Remove the graph and Flask parts for now as they"re not properly implemented