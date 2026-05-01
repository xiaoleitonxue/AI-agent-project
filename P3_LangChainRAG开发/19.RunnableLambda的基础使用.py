from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

str_output_parser = StrOutputParser()
my_fuc = RunnableLambda(lambda ai_msg: {"name" : ai_msg})

model = Tongyi(model="qwen-max")

first_prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字, 只告诉我名字"
)

second_prompt = PromptTemplate.from_template(
    "请将这段内容翻译成英文：{name}, 并且解释一下名字含义"
)

chain = first_prompt | model | my_fuc | second_prompt | model | str_output_parser
# chain = first_prompt | model | (lambda ai_msg: {"name" : ai_msg}) | second_prompt | model | str_output_parser

res = chain.stream({"lastname": "王", "gender": "女孩子"})
for chunk in res:
    print(chunk, end="", flush=True)