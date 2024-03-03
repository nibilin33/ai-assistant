# -*- coding: utf-8 -*-
from openai import OpenAI
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

import os

secret_key = os.getenv("SECRET_KEY")

client = OpenAI(
  api_key= secret_key,
  base_url= 'https://api.openai-proxy.com/v1'
)
weekPrompt = """
现在开始你是一名互联网行业周报助手，使用下面的工作内容作为中文周报的基础，生成一份工作周报，突出最重要的内容并以Markdown格式编写，要易于阅读和理解。
特别是要注重提供对决策者有用的见解和分析。你可以根据需要使用任何额外的信息或来源。
周报的内容包括：
1. OKR进展
2. 风险同步
3. 工作总结思考
4. 下周工作计划
以下是你需要完成的任务：
1. 你需要根据我提供的信息帮我完善扩充解释一些技术细节
2. 返回格式为markdown格式, 请确保周报的格式正确,以下是周报的模板
# OKR进展

# 风险同步

# 工作总结思考

# 下周工作计划
一下是我提供的信息：

"""
def chat_weekreports(message):
    prompt = f'{weekPrompt}{message}'
    try:
        response = client.chat.completions.create(
          model="gpt-3.5-turbo-16k",
          messages=[{"role": "user", "content": prompt}],
          temperature=1,
          top_p=1
        )
        report_content = response.choices[0].message.content.strip()
        print(report_content)
        # 打开一个文件用于写入，如果文件不存在，将会创建一个新文件
        with open('weekly_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_content)

    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    print("请输入你的周报内容：")
    # chat_weekreports("")