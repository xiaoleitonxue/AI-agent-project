from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

str_output_parser = StrOutputParser()
json_output_parser = JsonOutputParser()

model = Tongyi(model="qwen-max")

first_prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字, 简单回答"
    ", 并封装为JSON格式返回给我。要求key是name，value就是你起的名字，请严格遵守格式要求。"
)

second_prompt = PromptTemplate.from_template(
    "请将这段内容翻译成英文：{name}, 并且解释一下名字含义"
)

chain = first_prompt | model | json_output_parser | second_prompt | model | str_output_parser

# res = chain.invoke({"lastname": "王", "gender": "女孩子"})
#
# print(res)
# print(type(res))

res = chain.stream({"lastname": "王", "gender": "女孩子"})
for chunk in res:
    print(chunk, end="", flush=True)