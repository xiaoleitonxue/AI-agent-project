from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

res = model.invoke("请将这段内容翻译成英文：我叫小明，我今年18岁。")
print(res)