from openai import OpenAI

Client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = Client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个python专家，并且话非常多"},
        {"role": "assistant", "content": "好的，我是编程专家，你需要问什么内容？"},
        {"role": "user", "content": "请写一个python程序，实现 1+1 的计算结果"}
    ],
    stream = True
)

#print(response.choices[0].message.content)
for chunk in response:
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end="", flush=True
          )