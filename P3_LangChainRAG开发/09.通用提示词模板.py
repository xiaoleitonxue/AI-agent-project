from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字, 简单回答"
)

# prompt_text = prompt_template.format(lastname="王", gender="男孩子")

# print(prompt_template)
# print(prompt_text)

# model = Tongyi(model="qwen-max")
# res = model.invoke(prompt_text)
# print(res)

model = Tongyi(model="qwen-max")
chain = prompt_template | model
res = chain.invoke({"lastname": "王", "gender": "女孩子"})
print(res)