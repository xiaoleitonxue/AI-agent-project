from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings()

print(model.embed_query("你好"))
print(model.embed_documents(["你好", "世界"]))