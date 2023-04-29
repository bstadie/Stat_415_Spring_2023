import plotly.express as px 
fig = px.choropleth(KMEAN_df, locations='STATE_ABBR', locationmode='USA-states', color='DRUNK_DRIVING_PERCENTAGE_CLUSTER_MEAN', scope='usa') 
fig.show()

# alternatively, use plotly -- https://datascience.stackexchange.com/questions/9616/how-to-create-us-state-choropleth-map
