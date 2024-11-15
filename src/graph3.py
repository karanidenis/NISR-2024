# df_educ = pd.read_excel('./Data/RW_LFS_Tables_2024Q2.xlsx', sheet_name='LFIndicatorsEduc', skiprows=3)
# df_status = pd.read_excel('./Data/RW_LFS_Tables_2024Q2.xlsx', sheet_name='StatusInEmploymentUrRur', skiprows=3)

# df_educ = df_educ.dropna(axis=1, how='all')
# df_status = df_status.dropna(axis=1, how='all')

# # Highlight unemployment and employment rates directly
# employment_rate = df_youth_chart.loc['Employment rate', 'Q2']
# unemployment_rate = df_youth_chart.loc['Unemployment rate', 'Q2']

# # Pie chart for youth unemployment indicators
# fig_youth = px.pie(df_youth_chart, values='Q2', names=df_youth_chart.index, title="Youth Unemployment Indicators",
#                    color_discrete_sequence=px.colors.sequential.RdBu)
# fig_youth.update_traces(textinfo='percent+label')
# st.plotly_chart(fig_youth, use_container_width=True)

# # Additional comment on high youth unemployment
# st.markdown(f"The youth unemployment rate is **{unemployment_rate:.1f}%**, compared to an employment rate of **{employment_rate:.1f}%**. This indicates significant challenges for young people entering the workforce in Rwanda, with many not in education, employment, or training (NEET).")

# # Section 2: Education and Unemployment
# st.header("Impact of Education on Employment vs. Unemployment")
# st.markdown("#### How educational attainment affects employment and unemployment rates")

# # Prepare data for education level and employment comparison
# df_educ_chart = df_educ.iloc[0:5, [22]]
# df_educ_chart.columns = ['Q2']
# df_educ_chart.index = ['No education', 'Primary education', 'Secondary education', 'Post-secondary education', 'Tertiary education']
# df_educ_chart['Q2'] = df_educ_chart['Q2'] * 100

# # Plot for employment rates by education level
# fig_educ = px.bar(df_educ_chart, x=df_educ_chart.index, y='Q2', title="Education and Labour Force Participation",
#                   color='Q2', color_continuous_scale=px.colors.sequential.Viridis)
# fig_educ.update_layout(yaxis_title="Percentage (%)", xaxis_title="Level of Education", title_x=0.5)
# st.plotly_chart(fig_educ, use_container_width=True)

# # Additional note on education's impact on employment
# st.markdown("""
#     Higher education levels correlate with improved employment rates, suggesting that lack of education is a barrier to employment. However, even among those with secondary education, unemployment is still an issue.
# """)

# # Section 3: Employment Status by Urban/Rural Areas
# st.header("Urban vs. Rural Employment Status")
# st.markdown("#### Comparing employment status and underemployment between urban and rural areas")

# # Select relevant rows for urban/rural employment status and convert to percentages
# df_status_chart = df_status.iloc[0:5, [22]]
# df_status_chart.columns = ['Q2']
# df_status_chart.index = ['Employed', 'Unemployed', 'Not in labour force', 'Underemployed', 'Overemployed']
# df_status_chart['Q2'] = df_status_chart['Q2'] * 100  
# # Employment vs. Unemployment bar chart
# fig_status = go.Figure()
# fig_status.add_trace(go.Bar(
#     x=df_status_chart.index, y=df_status_chart['Q2'], 
#     marker_color=px.colors.sequential.Turbo, 
#     text=[f"{val:.1f}%" for val in df_status_chart['Q2']],
#     textposition='auto'
# ))
# fig_status.update_layout(title="Employment Status by Urban/Rural Residence", 
#                          xaxis_title="Employment Status", yaxis_title="Percentage (%)",
#                          title_x=0.5)
# st.plotly_chart(fig_status, use_container_width=True)

# # Analysis on urban/rural differences in unemployment and underemployment
# st.markdown("""
#     Employment status varies significantly between urban and rural areas, with underemployment particularly high in rural areas. This suggests a need for more meaningful employment opportunities outside urban centers. 
# """)

# # Conclusion section
# st.header("Key Takeaways")
# st.markdown(f"""
#     Rwanda's data reveals significant unemployment challenges, particularly among youth and in rural regions. Educational attainment appears to improve employment prospects, but underemployment and high unemployment persist, 
#     indicating that available jobs may not match the skills or needs of the population. **Addressing these challenges will require policies targeting youth employment, skills development, and rural job creation**.
# """)
