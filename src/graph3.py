import streamlit as st
import pandas as pd
import plotly.express as px

# Graph container
# with st.container():
st.markdown("""
        This dashboard provides insights into Rwanda's labour force dynamics, 
        highlighting the relationship between educational attainment, gender, and age-group with employment statistics.
    """)

    
def show_graph(df):

    # Summary
    st.markdown(f"""
    The chart illustrates the breakdown of the total population aged 16 and over by employment status:
    - Employed
    - Unemployed
    - Out of labour force
    """)

# Call the function to show the graph
# show_graph(combined_df)

def graph1(df):
    # Add a radio button in the sidebar to toggle between the plot and the raw data
    view_mode = st.sidebar.selectbox(
        "Select View Mode", ["Plot", "Raw Data"], key="graph1_select_view_mode")

    # Based on the selection, either display the plot or the raw data
    if view_mode == "Plot":
        # display_metric_box()
        show_graph(combined_df)
    elif view_mode == "Raw Data":
        # Wrap the data table in a container with margin
        st.markdown('<div class="data-container">', unsafe_allow_html=True)
        df = df.dropna(axis=1, how='all')  # Drop empty columns
        st.dataframe(df)  # This will display the dataframe as a table
        st.markdown('</div>', unsafe_allow_html=True)

graph1(combined_df)



