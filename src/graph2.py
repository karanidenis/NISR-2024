import streamlit as st
import pandas as pd
import plotly.express as px

# Graph container
# with st.container():
st.markdown("""
        This dashboard provides insights into Rwanda's labour force dynamics, 
        highlighting the relationship between educational attainment, gender, and age-group with employment statistics.
    """)


# Load the Excel file, skipping rows as necessary
df_total = pd.read_excel('./Data/RW_LFS_Tables_2024Q2.xlsx', sheet_name='LFIndicatorsRw', skiprows=3)
df_total = df_total.dropna(axis=1, how='all')

# Extract rows 0 to 5 and column 23 (the Q2.5 data)
q2_total_df = df_total.iloc[0:5, [22]]  
q2_total_df.columns = ['Q2']
q2_total_df.index = [
    'Working age population(16+ years)',
    'Labour force',
    'Employed',
    'Unemployed',
    'Out of labour force'
]

# Male dataset
df_male = pd.read_excel('./Data/RW_LFS_Tables_2024Q2.xlsx', sheet_name='LFIndicatorsSex', skiprows=3)
q2_male_df = df_male.iloc[0:5, [22]]
q2_male_df.columns = ['Q2']
q2_male_df.index = [
    'Working age population(16+ years)',
    'Labour force',
    'Employed',
    'Unemployed',
    'Out of labour force'
]

# Female dataset
q2_female_df = df_male.iloc[22:27, [22]]
q2_female_df.columns = ['Q2']
q2_female_df.index = [
    'Working age population(16+ years)',
    'Labour force',
    'Employed',
    'Unemployed',
    'Out of labour force'
]

# Combine the three DataFrames
combined_df = pd.concat([q2_total_df, q2_male_df, q2_female_df], axis=1)
combined_df.columns = ['Total', 'Male', 'Female']

    
def show_graph(df):
    # Sidebar for selecting the category
    area = st.sidebar.radio('Select Sex', ['Total', 'Male', 'Female'], key="graph1_sex")

    # Prepare data for visualization
    if area == 'Total':
        filtered_df = combined_df['Total']
    elif area == 'Male':
        filtered_df = combined_df['Male']
    elif area == 'Female':
        filtered_df = combined_df['Female']

    # Reset index for visualization
    filtered_df = filtered_df.reset_index()
    filtered_df.columns = ['Indicators', 'Value']  # Rename columns for clarity

    # Define your color scheme
    colors = ['#006af9', '#008080', '#ff7f50']
    
    # Create pie chart
    fig_pie = px.pie(filtered_df[1:], values='Value', names='Indicators',
                     title=f'Labour Force Distribution - {area}',
                     color_discrete_sequence=colors)
    
    # Display the pie chart
    st.plotly_chart(fig_pie, use_container_width=True)

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


