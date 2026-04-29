from openai import OpenAI

# 1. 获取 client 对象，OpenAI 类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

examples_data = {  # 示例数据
    '新闻报道': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧缩局势的影响。投资者密切关注美联储可能的政策调整，以适应市场的不确定性。',
    '财务报告': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康发展提供了支持。',
    '公司公告': '本公司高兴地宣布成功完成最新一轮并购交易，收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域，提高市场竞争力。',
    '分析师报告': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素。'
}

# 分类列表
examples_types = ['新闻报道', '财务报告', '公司公告', '分析师报告']

# 待提问数据
questions = [
    "今日，央行发布公告宣布降低利率，以刺激经济增长。这一举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
    "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步加强公司的市场地位。",
    "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
    "最新的分析报告指出，可再生能源行业预计在未来几年经历持续增长，投资者应该关注这一领域的投资机会。",
    "小明喜欢小红"
]

# 构造 Prompt（Few-shot 演示）
[
    {"role": "system", "content": f"你是金融专家，将文本分类为 {examples_types}。不清楚的分类为 '不清楚'。"},
    {"role": "user", "content": f"今日，央行发布公告宣布降…… {questions[0]}"},
    {"role": "assistant", "content": "新闻报道"},
    {"role": "user", "content": f"ABC公司今日发布公告称，已成功完成对XYZ公司股…… {questions[1]}"},
    {"role": "assistant", "content": "公司公告"},
    {"role": "user", "content": f"公司资产负债表显示，公司偿债能力强劲，现金流充足…… {questions[2]}"},
    {"role": "assistant", "content": "财务报告"},
    {"role": "user", "content": f"最新的分析报告指出，可再生能源…… {questions[3]}"},
    {"role": "assistant", "content": "分析师报告"},

    {"role": "user", "content": "要提问的问题"} # 此处通常为循环或单次传入 questions 中的内容
]

# 后续通常会调用 client.chat.completions.create(...) 进行模型请求

# 接续之前的逻辑

messages = [
    {"role": "system", "content": f"你是金融专家，将文本分类为 {examples_types}。不清楚的分类为 '不清楚类别'"}
]

# 通过循环动态添加示例 (Few-shot)
for key, value in examples_data.items():
    messages.append({"role": "user", "content": value})
    messages.append({"role": "assistant", "content": key})

# 向模型提问
for q in questions:
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages + [{"role": "user", "content": f"按照示例，回答这段文本的分类类别：{q}"}]
    )

    print(response.choices[0].message.content)
