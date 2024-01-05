import json
json_string_1 = '{"name": "A", "age": 35, "company": "Đất Việt"}'
json_obj1 = json.loads(json_string_1)
json_string  = json.dumps(json_obj1,ensure_ascii=False)
print(json_string)