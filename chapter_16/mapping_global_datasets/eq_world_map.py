from pathlib import Path
import json

import plotly.express as px
import pandas as pd

# 读取作为字符串的数据并转换为Python对象。
path = Path('eq_data/eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# 获取数据集中地震列表。
all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
 )
fig.write_html('eq_data/global_earthquakes.html')
fig.show()
