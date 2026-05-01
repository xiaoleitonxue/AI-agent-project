from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")
prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字, 简单回答"
)

parser = StrOutputParser()

chain = prompt | model | parser | model | parser
res = chain.invoke({"lastname": "王", "gender": "女孩子"})
print(res)
print(type(res))