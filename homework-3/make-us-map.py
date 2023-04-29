import plotly.express as px 
fig = px.choropleth(KMEAN_df, locations='STATE_ABBR', locationmode='USA-states', color='DRUNK_DRIVING_PERCENTAGE_CLUSTER_MEAN', scope='usa') 
fig.show()
