from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatTongyi(model="qwen3-max")

messages = [
    # SystemMessage(content="你是一个中国诗人，请用唐诗的格式输出"),
    # HumanMessage(content="写一首唐诗"),
    # AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    # HumanMessage(content="安装你上一个回复的格式，再写"),

    ("system", "你是一个中国诗人，请用唐诗的格式输出"),
    ("human", "写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human", "安装你上一个回复的格式，再写")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content, end="", flush=True)