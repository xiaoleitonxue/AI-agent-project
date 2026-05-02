import os, json
from typing import Sequence
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id
        self.storage_path = storage_path

        self.file_path = os.path.join(self.storage_path, f"{self.session_id}.json")
        os.makedirs(self.storage_path, exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        # new_messages = []
        # for message in all_messages:
        #     new_messages.append(message_to_dict(message))

        new_messages = [message_to_dict(message) for message in all_messages]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property
    def messages(self) -> list[BaseMessage]:
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r", encoding="utf-8") as f:
            messages = json.load(f)
        return messages_from_dict(messages)

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)






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

# store = {}
def get_history(session_id):
    # if session_id not in store:
    #     store[session_id] = InMemoryChatMessageHistory()
    # return store[session_id]
    return FileChatMessageHistory(session_id, "./history")

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