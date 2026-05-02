from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader(
#     file_path = "./data/pdf1.pdf",
#     mode = "single",
# )

loader = PyPDFLoader(
    file_path = "./data/pdf2.pdf",
    mode = "page",
    password="itheima"
)

i = 0
for doc in loader.load():
    i += 1
    print(doc)
    print("="*20, i, "="*20)