import csv

data = [
    ['王梓涵', 25, '男'],
    ['刘若曦', 22, '女'],
    ['陈俊宇', 20, '男'],
    ['赵思瑶', 28, '女'],
    ['黄浩然', 15, '男'],
    ['林雨桐', 20, '女'],
    ['周博文', 20, '男'],
    ['吴诗琪', 24, '女'],
    ['马子轩', 22, '男'],
    ['孙悦然', 27, '女']
]

with open(r'D:\lesson\lesson-practice\ai_agent_project\P3_LangChainRAG开发\data\stu.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'gender'])
    writer.writerows(data)
