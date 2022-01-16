import plotly.express as px

fig = px.scatter(
    x=[-116.7941667],
    y=[33.4863333],
    labels={"x": "经度", "y": "纬度"},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
)

fig.write_html("global_earthquakes.html")
fig.show()