import pandas as pd
from bokeh.io import output_file, save
from bokeh.models import ColumnDataSource, HoverTool, Select, Slider, CustomJS
from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models.callbacks import CustomJS

# Load data
data = pd.read_csv("data/merged_data_TA.csv")

# Clean and filter data
data = data[(data['Longitude'] > -125) & (data['Longitude'] < -120)]
data = data[(data['Latitude'] > 37) & (data['Latitude'] < 38)]

#use only 2 years
data = data[(data['Year'] == 2018) | (data['Year'] == 2019)]

# Convert coordinates to Web Mercator for Bokeh map
def wgs84_to_web_mercator(lon, lat):
    import numpy as np
    k = 6378137
    x = lon * (k * np.pi / 180.0)
    y = np.log(np.tan((90 + lat) * np.pi / 360.0)) * k
    return x, y

data["x"], data["y"] = wgs84_to_web_mercator(data["Longitude"], data["Latitude"])

# Prepare data source
source = ColumnDataSource(data)

# Create base plot
tile_provider = get_provider(Vendors.CARTODBPOSITRON)
p = figure(x_axis_type="mercator", y_axis_type="mercator", height=600, width=800,
           title="Crime Incidents by Traffic Category and Hour")
p.add_tile(tile_provider)

hover = HoverTool(tooltips=[
    ("Category", "@Category"),
    ("Hour", "@TimeOfDay"),
    ("District", "@PdDistrict"),
])
p.add_tools(hover)

points = p.circle(x="x", y="y", size=8, source=source, fill_alpha=0.6)

# Interactive widgets
category_select = Select(title="Category", value="ASSAULT", options=sorted(data["Category"].unique()))
hour_slider = Slider(start=0, end=23, value=17, step=1, title="Hour of Day")

# JavaScript callback to filter data
callback = CustomJS(args=dict(source=source, original=ColumnDataSource(data),
                              category=category_select, hour=hour_slider),
                    code="""
    const data = source.data;
    const original_data = original.data;
    const selected_category = category.value;
    const selected_hour = hour.value;

    const new_data = {x: [], y: [], Category: [], TimeOfDay: [], PdDistrict: []};

    for (let i = 0; i < original_data['Category'].length; i++) {
        if (original_data['Category'][i] === selected_category &&
            original_data['TimeOfDay'][i] === selected_hour) {
            new_data['x'].push(original_data['x'][i]);
            new_data['y'].push(original_data['y'][i]);
            new_data['Category'].push(original_data['Category'][i]);
            new_data['TimeOfDay'].push(original_data['TimeOfDay'][i]);
            new_data['PdDistrict'].push(original_data['PdDistrict'][i]);
        }
    }
    source.data = new_data;
""")

category_select.js_on_change('value', callback)
hour_slider.js_on_change('value', callback)

layout = column(p, row(category_select, hour_slider))
output_path = "images/interactive_map_filtered.html"
output_file(output_path)
save(layout)

output_path
