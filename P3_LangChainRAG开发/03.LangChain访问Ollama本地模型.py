from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="qwen3:4b")

res = model.invoke("请将这段内容翻译成英文：我叫小明，我今年18岁。")
print(res)