from langchain_community.document_loaders import JSONLoader

# loader = JSONLoader(
#     file_path="./data/stu.json",
#     jq_schema=".other.addr",
#     text_content=False
# )
#
# loader = JSONLoader(
#     file_path="./data/stus.json",
#     jq_schema=".[].name",
#     text_content=False
# )

loader = JSONLoader(
    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,
    json_lines= True
)

document = loader.load()
print(document)