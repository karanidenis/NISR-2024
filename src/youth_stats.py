import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load the Excel file
df_youth = pd.read_excel('./Data/RW_LFS_Tables_2024Q2.xlsx', sheet_name='LFIndicatorsYouthAdult', skiprows=3)

# Clean and prepare the data
df_youth = df_youth.dropna(axis=1, how='all')

def create_metric_box(label, value):
    st.markdown("""
    <style>
    .metric-box {
        # background-color: #009688;
        # background-color: #1f2c56;
        # background-color: blue;
        background-color: #006af9;
        border-radius: 10px;
        padding: 15px;
        color: white;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 0.2em;
    }
    .metric-label {
        font-size: 1em;
    }
    # .data-container {
    #     margin-top: 20px;
    # }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


def display_metric_box():
    # Layout for metric boxes
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        create_metric_box("Labor force participation rate", "59.38%")
    with col2:
        create_metric_box("Employment rate", "47.208%")
    with col3:
        create_metric_box("Unemployment rate", "40.619%")
    with col4:
        create_metric_box("Youths not education, employment or training", "31.57%")


def radar_chart(df_data):
    # Filter and structure the youth data
    df_youth_chart = df_data.iloc[0:5, [22]]
    df_youth_chart.columns = ['Q2']
    df_youth_chart.index = ['Labour force participation rate', 'Employment rate', 'Unemployment rate', 
                            'Youth not in education, employment, or training (NEET)', 'Youth unemployment rate']
    
    # Extract the relevant rows and data
    dict_df = df_youth_chart
    metrics = dict_df.index.tolist()
    values = dict_df['Q2'].tolist()

    # Add the first value to close the radar chart
    metrics += metrics[:1]
    values += values[:1]

    # Create a radar chart using Plotly
    fig = go.Figure()

    # Add the radar trace
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=metrics,
        fill='toself',
        name='Labor Market Metrics',
        hoverinfo='text',
        text=[f"{metric}: {value:.2f}%" for metric, value in zip(metrics, values)],
        line=dict(color='blue', width=3),  
        marker=dict(color='blue') 
    ))

    # Customize the layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True,
                            color='black',
                            range=[0, max(values) + 5])
        ),
        showlegend=False,
        title="Labor Market Metrics"
    )

    return fig


def graph2():
    # Section 1: Youth Unemployment Analysis
    st.markdown("#### Youth unemployment rates among those aged 15-24 in Rwanda")
    display_metric_box()
    st.plotly_chart(radar_chart(df_youth))
    return 
    
    
