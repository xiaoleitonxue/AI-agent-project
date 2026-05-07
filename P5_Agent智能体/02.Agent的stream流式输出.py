from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool

@tool(description="查询股票价格")
def get_price(name:str) -> str:
    return f"股票{name}的价格是100元"

@tool(description="查询股票信息")
def get_info(name:str) -> str:
    return f"股票{name}的信息是：股票名称：{name}，股票价格：100元，股票涨跌幅：0.1%"

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_info, get_price],
    system_prompt="你是一个聊天助手，可以回答股票相关问题，并且需要告诉我思考过程"
)

for chunk in agent.stream(
    {"messages":[{"role": "user", "content": "aa教育的股价是多少，并且给我介绍一下？"}]},
    stream_mode="values"
):
    # print(chunk)
    latest_messages = chunk['messages'][-1]
    # print(latest_messages)
    if latest_messages.content:
        print(type(latest_messages).__name__, latest_messages.content)

    try:
        if latest_messages.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_messages.tool_calls]}")
    except AttributeError as e:
        pass