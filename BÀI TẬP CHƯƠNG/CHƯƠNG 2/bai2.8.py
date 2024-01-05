import json
tu_dien = {1:"một",2:"hai",3:"ba",4:"bốn"}
json_data = json.dumps(tu_dien,ensure_ascii=False,indent=4)
print(json_data)