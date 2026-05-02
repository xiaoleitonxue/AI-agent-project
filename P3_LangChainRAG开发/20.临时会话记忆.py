from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model="qwen3-max")
# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题，对话历史：{chat_history}，用户提问：{input}，请回答"
# )
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个助手，你需要根据会话历史回答用户问题："),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "请回答如下问题：{input}")
    ]
)

str_parsar = StrOutputParser()

def print_prompt(full_prompt):
    print("="*20, full_prompt.to_string(), "="*20)
    return full_prompt

base_chain = prompt | print_prompt | model | str_parsar

store = {}
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

if __name__ == "__main__":
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    res = conversation_chain.invoke({"input": "小明有2只猫"}, config=session_config)
    print("第一次执行", res)

    res = conversation_chain.invoke({"input": "小明有4只狗"}, config=session_config)
    print("第二次执行", res)
    res = conversation_chain.invoke({"input": "小明一共有几只宠物"}, config=session_config)
    print("第三次执行", res)