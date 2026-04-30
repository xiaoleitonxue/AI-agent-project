from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

"""
PromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
FewShotPromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
ChatPromptTemplate -> BaseChatPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
"""

template = PromptTemplate.from_template("我的邻居是{lastname}，喜欢{hobby}")

res1 = template.format(lastname="王五", hobby="吃")
print(res1,type(res1))

res2 = template.invoke(input={"lastname": "张三", "hobby": "粒子"})
print(res2, type(res2))