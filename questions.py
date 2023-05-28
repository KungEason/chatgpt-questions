import json

def get_user_input(question, options):
    print(question)
    for key, value in options.items():
        print(f"{key}. {value}")
    user_input = input("請輸入您的選項: ")
    return user_input

# 讀取 JSON 檔案
with open("your_file.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 喜好和興趣
preferences = data["喜好和興趣"]
preferences_score = 0
for category, details in preferences.items():
    question = f"您喜歡的{category}是？"
    options = details["選項"]
    user_input = get_user_input(question, options)
    score = details["分數"][user_input]
    preferences_score += score
    print(f"您對於{category}的喜好分數是: {score}")

# 行為反應
reactions = data["行為反應"]
reactions_score = 0
for question, details in reactions.items():
    options = details["選項"]
    user_input = get_user_input(question, options)
    score = details["分數"][user_input]
    reactions_score += score
    print(f"對於問題「{question}」的反應分數是: {score}")

# 人際關係
relationships = data["人際關係"]
relationships_score = 0
for question, details in relationships.items():
    options = details["選項"]
    user_input = get_user_input(question, options)
    score = details["分數"][user_input]
    relationships_score += score
    print(f"對於問題「{question}」的回答分數是: {score}")

# 自我認知
self_awareness = data["自我認知"]
self_awareness_score = 0
for question, details in self_awareness.items():
    options = details["選項"]
    user_input = get_user_input(question, options)
    score = details["分數"][user_input]
    self_awareness_score += score
    print(f"對於問題「{question}」的回答分數是: {score}")

# 情緒狀態
emotions = data["情緒狀態"]
emotions_score = 0
for question, details in emotions.items():
    options = details["選項"]
    user_input = get_user_input(question, options)
    score = details["分數"][user_input]
    emotions_score += score
    print(f"對於問題「{question}」的回答分數是: {score}")

# 態度和價值觀
attitudes = data["態度和價值觀"]
attitudes_score = 0
for question, details in attitudes.items():
    options = details["選項"]
    user_input = get_user_input(question, options)
    score = details["分數"][user_input]
    attitudes_score += score
    print(f"對於問題「{question}」的回答分數是: {score}")# 計算各個分數
preferences_score = 1
reactions_score = 1
relationships_score = 1
self_awareness_score = 1
emotions_score = 1
attitudes_score = 1

# 計算總分
total_score = (
    preferences_score + reactions_score + relationships_score +
    self_awareness_score + emotions_score + attitudes_score
)

# 計算分數範圍
personality_type = ""
if 5 <= total_score <= 9:
    personality_type = "外向、開放、充滿創造力的人格"
elif 10 <= total_score <= 14:
    personality_type = "平衡、友善、細心的人格"
elif 15 <= total_score <= 19:
    personality_type = "自信、領導能力、冒險精神的人格"
elif 20 <= total_score <= 24:
    personality_type = "細心、實踐、耐心的人格"
elif 25 <= total_score <= 30:
    personality_type = "自信、創新、追求卓越的人格"

# 計算情緒狀態
emotions_type = ""
if 0 <= emotions_score <= 3:
    emotions_type = "低情緒"
elif 4 <= emotions_score <= 6:
    emotions_type = "中等情緒"
elif 7 <= emotions_score <= 10:
    emotions_type = "高情緒"

# 計算人際關係
relationships_type = ""
if 0 <= relationships_score <= 3:
    relationships_type = "低人際關係"
elif 4 <= relationships_score <= 6:
    relationships_type = "中等人際關係"
elif 7 <= relationships_score <= 10:
    relationships_type = "高人際關係"

# 計算偏好
preferences_type = ""
if 0 <= preferences_score <= 3:
    preferences_type = "低偏好"
elif 4 <= preferences_score <= 6:
    preferences_type = "中等偏好"
elif 7 <= preferences_score <= 10:
    preferences_type = "高偏好"

print("性格特質：", personality_type)
print("情緒狀態：", emotions_type)
print("人際關係：", relationships_type)
print("偏好：", preferences_type)
