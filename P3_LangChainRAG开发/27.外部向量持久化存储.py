from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma

# vector_store = InMemoryVectorStore(
#     DashScopeEmbeddings()
# )
vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"
)

# loader = CSVLoader(
#     file_path="./data/info.csv",
#     encoding="utf-8",
#     source_column="source",
# )
#
# documents = loader.load()
#
# # print(documents[0])
#
# vector_store.add_documents(
#     documents =  documents,
#     ids = ["id" + str(i) for i in range(1, len(documents)+1)]
# )
#
# vector_store.delete(["id1", "id2"])

result = vector_store.similarity_search(
    query = "如何学习Python",
    k = 2,
    filter = {"source": "黑马程序员"}
)
print(result)