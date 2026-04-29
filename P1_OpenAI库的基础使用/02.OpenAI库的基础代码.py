from openai import OpenAI

Client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = Client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个python专家，不说废话直接回答具体问题"},
        {"role": "assistant", "content": "好的，我是编程专家，你需要问什么内容？"},
        {"role": "user", "content": "请写一个python程序，实现 1+1 的计算结果"}
    ]
)

print(response.choices[0].message.content)