import json

d = {
    "name": "小明",
    "age": 18,
    "sex": "男"
}

s = json.dumps(d, ensure_ascii=False)
print(s)

l = [
    {
        "name": "小明",
        "age": 18,
        "sex": "男"
    },
    {
        "name": "小王",
        "age": 19,
        "sex": "女"
    },
    {
        "name": "小张",
        "age": 20,
        "sex": "男"
    }
]

s = json.dumps(l, ensure_ascii=False)
print(s)

json_str = '{"name": "小明", "age": 18, "sex": "男"}'
jsom_array = '[{"name": "小明", "age": 18, "sex": "男"}, {"name": "小王", "age": 19, "sex": "女"}, {"name": "小张", "age": 20, "sex": "男"}]'
j1 = json.loads(json_str)
j2 = json.loads(jsom_array)
print(j1)
print(j2)