
import transformers
import datasets

from transformers import pipeline

# 加载模型
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# 调用模型, 推理
result = model("I've been waiting for a HuggingFace course my whole life.")

print(result)