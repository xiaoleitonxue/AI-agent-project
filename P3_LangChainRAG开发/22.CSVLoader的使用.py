from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        "fieldnames": ["name", "age", "sex"],
    },
    encoding="utf-8"
)

documents = loader.load()

# print(documents)
#
# for doc in documents:
#     print(type(documents), doc)

for documents in loader.lazy_load():
    print(type(documents), documents)