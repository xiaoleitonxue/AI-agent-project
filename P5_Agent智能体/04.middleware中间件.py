from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langgraph.runtime import Runtime

@tool(description="查询天气,传入城市")
def get_weather(city: str) -> str:
    return "明天{city}天气晴转多云，最低气温 18℃，最高气温 26℃。"

@before_agent
def log_before_agent(state: AgentState, runtime: Runtime) -> None:
    # agent执行前会调用这个函数并传入state和runtime两个对象
    print(f"[before agent]agent启动，并附带{len(state['messages'])}消息")

@after_agent
def log_after_agent(state: AgentState, runtime: Runtime) -> None:
    # agent执行完成后会调用这个函数并传入state和runtime两个对象
    print(f"[after agent]agent执行完成，并附带{len(state['messages'])}消息")

@before_model
def log_before_model(state: AgentState, runtime: Runtime) -> None:
    # model执行前会调用这个函数并传入state和runtime两个对象
    print(f"[before model]model启动，并附带{len(state['messages'])}消息")

@after_model
def log_after_model(state: AgentState, runtime: Runtime) -> None:
    # model执行完成后会调用这个函数并传入state和runtime两个对象
    print(f"[after model]model执行完成，并附带{len(state['messages'])}消息")

@wrap_model_call
def model_call_hook(request, handler):
    print("模型调用了")
    return handler(request)

@wrap_tool_call
def tool_call_hook(request, handler):
    print("工具被调用了")
    print(f"工具执行: {request.tool_call['name']}")
    print(f"工具执行传入参数: {request.tool_call['args']}")
    return handler(request)

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],
    middleware=[log_before_agent, log_after_agent, log_before_model, log_after_model, model_call_hook, tool_call_hook]
)

res = agent.invoke({"messages": [{"role": "user", "content": "上海今天天气如何呀，如何穿衣"}]})
print("**********\n", res)