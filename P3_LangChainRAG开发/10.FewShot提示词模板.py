from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi

example_template = PromptTemplate.from_template(
    "单词：{word}，反义词{antonym}"
)

example_data = [
    {"word": "中国", "antonym": "外国"},
    {"word": "高", "antonym": "低"},
    {"word": "长", "antonym": "短"},
    {"word": "强", "antonym": "弱"},
    {"word": "高", "antonym": "低"},
    {"word": "黑", "antonym": "白"},
    {"word": "大", "antonym": "小"}
]

few_shot_templates = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="告诉我单词的反义词，我提供下面示例",
    suffix="基于前面的例子，告诉我{input_word}的反义词是什么",
    input_variables=['input_word'],
    # example_separator="\n",
    # validate_template=True,
)

# prompt_text = few_shot_templates.invoke(input={"input_word": "左"}).to_string()
# print(prompt_text)
#
# model = Tongyi(model="qwen-max")
# print(model.invoke(prompt_text))

model = Tongyi(model="qwen-max")
text = few_shot_templates | model
print(text.invoke(input={"input_word": "左"}))