import streamlit as st
import pandas as pd
from general_gender_stats import graph1
from youth_stats import graph2

# Graph container
with st.container():
    st.title("Rwanda Labour Force Survey Dashboard 2024:Q2")
    st.markdown("""
        This dashboard provides insights into Rwanda's labour force dynamics, 
        highlighting the relationship between educational attainment, gender, and age-group with employment statistics.
    """)

    # Define a list of graph functions
    graph_functions = [graph1, graph2]

    # Initialize session state for the index of the current graph
    if 'current_graph_index' not in st.session_state:
        st.session_state.current_graph_index = 0

    # Display the current graph
    current_graph_index = st.session_state.current_graph_index

    # Call the current graph function with appropriate parameters
    graph_functions[current_graph_index]()

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('Previous'):
        if st.session_state.current_graph_index > 0:
            st.session_state.current_graph_index -= 1  # Update session state
            # Trigger page refresh by changing session state

with col2:
    if st.button('Next'):
        if st.session_state.current_graph_index < len(graph_functions) - 1:
            st.session_state.current_graph_index += 1  # Update session state
            # Trigger page refresh by changing session state

