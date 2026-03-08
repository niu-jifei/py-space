import gradio as gr

# 定义情感分析函数
def sentiment_analysis(text):
    text = text.lower()
    if "好" in text or "开心" in text or "喜欢" in text:
        return "积极"
    elif "不好" in text or "难过" in text or "讨厌" in text:
        return "消极"
    else:
        return "中性"

# 创建 Gradio 界面
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(label="请输入文本"),
    outputs=gr.Textbox(label="情感分析结果"),
    title="情感分析示例",
    description="输入一句话，判断它的情感倾向（简单示例）"
)

# 启动应用
demo.launch(share=True)