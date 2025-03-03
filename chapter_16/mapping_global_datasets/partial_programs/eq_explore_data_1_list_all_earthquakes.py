from pathlib import Path
import json


# 读取作为字符串的数据并转换为Python对象。
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# 获取数据集中地震列表。
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
