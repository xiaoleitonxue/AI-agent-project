from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}。"),
        ("user", "用户提问: {input}")
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

vector_store.add_texts(texts=["减肥就是要少吃多练", "在减脂期间吃东西很重要,清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动哦"])

input_text = "如何减肥"

result = vector_store.similarity_search(input_text, k=2)
# print(result)
reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

def prompt_print(full_prompt):
    print("="*20, full_prompt.to_string(), "="*20)
    return full_prompt

chain = prompt | prompt_print | model | StrOutputParser()

res = chain.invoke({"input": input_text, "context": reference_text})
print(res)