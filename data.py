# -*- coding: utf-8 -*-
import json
import pandas as pd
import os

DEFAULT_SYSTEM_PROMPT = """从现在开始，你是前端技术面试官，一个面试前端工程师候选人的专家。
以下规则是严格的：
1. 你的主要目的是模仿互联网大厂的真实工作面试
2. 你将问我要面试的公司的职位情况以及需要掌握的技术，你接下来的所有问题都要以职位要求为主进行考核
3. 你会让我先介绍一下自己，等待我的回答
4. 然后根据我的自我介绍问我一个自我介绍中提到的相关问题细节，并等待我的回答。在我给出答案后，你要审查我的答案以及根据岗位信息给出相应的改进建议
5. 你将按照前上一条规则继续问我问题并等待我的回答，如果我回答不知道则进入下个步骤，如果回答了就继续这个步骤直到我至少回答了10个问题
6. 接着随机抽取技术问题并等待我的回答，在我给出答案后你要审查答案并给出相关改进建议，重复这个过程直到我回答不出来后你进入下一个步骤
7. 接着你会询问我的项目经历，并等待我的回答。在我给出答案后，你要审查我的答案以及根据岗位信息给出相应的改进建议
8. 然后根据我的项目经历深挖技术细节相关问题并且等待我的回答，直到我至少回答了10个问题，让我们开始吧!
"""


def list_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            target_file = os.path.join(root, file)
            file_name_with_extension = os.path.basename(target_file)
            file_name, file_extension = os.path.splitext(file_name_with_extension)
            df = pd.read_csv(target_file, encoding='utf-8')
            with open(file_name+".jsonl", "w", encoding='utf-8') as f:
                for _, row in df.iterrows():
                    example_str = json.dumps(create_dataset(row["question"], row["answer"]),ensure_ascii=False)
                    print(example_str)
                    f.write(example_str + "\n")

def create_dataset(question, answer):
    return {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }

if __name__ == "__main__":
    current_path = os.getcwd()
    new_path = os.path.join(current_path, "fine-tuning")
    list_all_files(new_path)
    # df = pd.read_csv("path/to/file.csv", encoding='cp1252')
    # with open("train.jsonl", "w") as f:
    #     for _, row in df.iterrows():
    #         example_str = json.dumps(create_dataset(row["Question"], row["Answer"]))
    #         f.write(example_str + "\n")
