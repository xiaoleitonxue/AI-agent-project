from openai import OpenAI

Client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = Client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个Ai助手，回答很简洁"},
        {"role": "assistant", "content": "好的，我是ai助手，你需要问什么内容？"},
        {"role": "user", "content": "小明有3条狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小明有32只猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小明有几只宠物"},
    ],
    stream = True
)

#print(response.choices[0].message.content)
for chunk in response:
    print(chunk.choices[0].delta.content,
          end="",
          flush=True
          )