"""Python file for creating the choropleth map of Canada."""
import json
import pandas as pd
import plotly.express as px

provinces = json.load(open('canada_provinces.geojson'))

df = pd.read_csv('heatscale.csv')

cartodb_id_map = {}

for feature in provinces['features']:
    feature['id'] = feature['properties']['cartodb_id']
    cartodb_id_map[feature['properties']['name']] = feature['id']

df['id'] = df['Staffing action taken'][1:14].apply(lambda x: cartodb_id_map[x])

fig = px.choropleth(df,
                    locations='id',
                    geojson=provinces,
                    color='Reduced staff hours or shifts',
                    hover_name='Staffing action taken',
                    color_continuous_scale=px.colors.diverging.RdBu,
                    color_continuous_midpoint=0,
                    scope='north america')
fig.update_geos(fitbounds='locations', visible=False)
fig.update_layout(margin={
    "r": 0,
    "t": 0,
    "l": 0,
    "b": 0
})
fig.show()
