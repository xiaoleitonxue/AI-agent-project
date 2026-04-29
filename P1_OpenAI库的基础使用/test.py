from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
)

try:
    completion = client.chat.completions.create(
        model="deepseek-r1:8b",
        messages=[{"role": "user", "content": "你好"}],
        stream=False,  # 先测试非流式
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"错误: {e}")
