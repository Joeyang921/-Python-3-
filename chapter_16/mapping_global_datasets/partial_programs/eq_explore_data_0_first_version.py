from pathlib import Path
import json


# 读取作为字符串的数据并转换为Python对象。
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# 创建一个更可读的数据文件版本。
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)