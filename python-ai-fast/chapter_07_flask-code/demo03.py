# 演示flask框架，通过页面输入，调用transformers模型的pipeline模式， 实现文本情感分析的功能，简单示例即可

from flask import Flask, render_template_string, request, jsonify
from transformers import pipeline
import os

# 创建Flask应用
app = Flask(__name__)

# 初始化情感分析pipeline
# 使用轻量级模型以减少加载时间
try:
    # 尝试加载中文情感分析模型
    sentiment_pipeline = pipeline("sentiment-analysis", 
                                model="uer/roberta-base-finetuned-chinanews-chinese")
except Exception as e:
    print(f"加载中文模型失败: {e}")
    try:
        # 备选方案：加载英文模型
        sentiment_pipeline = pipeline("sentiment-analysis")
    except Exception as e2:
        print(f"加载英文模型也失败: {e2}")
        # 如果模型加载失败，使用模拟函数
        sentiment_pipeline = None

# 主页路由
@app.route('/')
def home():
    # HTML模板
    html_template = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>文本情感分析</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
            }
            .container {
                background-color: white;
                border-radius: 8px;
                padding: 25px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            textarea {
                width: 100%;
                height: 120px;
                padding: 12px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 16px;
                resize: vertical;
                margin-bottom: 15px;
            }
            button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px 20px;
                font-size: 16px;
                border-radius: 4px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #2980b9;
            }
            button:disabled {
                background-color: #95a5a6;
                cursor: not-allowed;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                border-radius: 4px;
                display: none;
            }
            .positive {
                background-color: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            .negative {
                background-color: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
            .neutral {
                background-color: #e2e3e5;
                color: #383d41;
                border: 1px solid #d6d8db;
            }
            .loading {
                text-align: center;
                margin-top: 20px;
                display: none;
            }
            .spinner {
                border: 4px solid rgba(0, 0, 0, 0.1);
                width: 36px;
                height: 36px;
                border-radius: 50%;
                border-left-color: #09f;
                animation: spin 1s linear infinite;
                margin: 0 auto;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .examples {
                margin-top: 30px;
            }
            .example-item {
                background-color: #f8f9fa;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 4px;
                cursor: pointer;
                transition: background-color 0.2s;
            }
            .example-item:hover {
                background-color: #e9ecef;
            }
            .model-info {
                margin-top: 20px;
                font-size: 14px;
                color: #6c757d;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>文本情感分析</h1>
        <div class="container">
            <div>
                <label for="text-input">请输入要分析的文本：</label>
                <textarea id="text-input" placeholder="在这里输入您想要分析情感的文本..."></textarea>
                <button id="analyze-btn" onclick="analyzeSentiment()">分析情感</button>
            </div>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>正在分析中，请稍候...</p>
            </div>
            
            <div class="result" id="result"></div>
            
            <div class="examples">
                <h3>示例文本（点击使用）：</h3>
                <div class="example-item" onclick="useExample('今天天气真好，心情很愉快！')">
                    今天天气真好，心情很愉快！
                </div>
                <div class="example-item" onclick="useExample('这个产品质量太差了，非常失望。')">
                    这个产品质量太差了，非常失望。
                </div>
                <div class="example-item" onclick="useExample('电影情节一般，演员表演还可以。')">
                    电影情节一般，演员表演还可以。
                </div>
                <div class="example-item" onclick="useExample('我非常喜欢这家餐厅的菜品，服务也很周到。')">
                    我非常喜欢这家餐厅的菜品，服务也很周到。
                </div>
                <div class="example-item" onclick="useExample('等了一个小时还没收到快递，太糟糕了。')">
                    等了一个小时还没收到快递，太糟糕了。
                </div>
            </div>
            
            <div class="model-info">
                <p>本应用使用Transformers库进行情感分析</p>
            </div>
        </div>
        
        <script>
            function useExample(text) {
                document.getElementById('text-input').value = text;
            }
            
            function analyzeSentiment() {
                const text = document.getElementById('text-input').value.trim();
                
                if (!text) {
                    alert('请输入要分析的文本');
                    return;
                }
                
                // 显示加载动画
                document.getElementById('loading').style.display = 'block';
                document.getElementById('result').style.display = 'none';
                document.getElementById('analyze-btn').disabled = true;
                
                // 发送请求到后端
                fetch('/analyze', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: text })
                })
                .then(response => response.json())
                .then(data => {
                    // 隐藏加载动画
                    document.getElementById('loading').style.display = 'none';
                    document.getElementById('analyze-btn').disabled = false;
                    
                    // 显示结果
                    displayResult(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('loading').style.display = 'none';
                    document.getElementById('analyze-btn').disabled = false;
                    alert('分析过程中出现错误，请稍后重试');
                });
            }
            
            function displayResult(data) {
                const resultDiv = document.getElementById('result');
                
                if (data.error) {
                    resultDiv.className = 'result neutral';
                    resultDiv.innerHTML = `<strong>错误：</strong> ${data.error}`;
                } else {
                    const sentiment = data.sentiment;
                    const confidence = (data.confidence * 100).toFixed(2);
                    
                    // 根据情感类型设置样式
                    if (sentiment === '正面' || sentiment === 'POSITIVE') {
                        resultDiv.className = 'result positive';
                    } else if (sentiment === '负面' || sentiment === 'NEGATIVE') {
                        resultDiv.className = 'result negative';
                    } else {
                        resultDiv.className = 'result neutral';
                    }
                    
                    resultDiv.innerHTML = `
                        <h3>分析结果</h3>
                        <p><strong>情感倾向：</strong> ${sentiment}</p>
                        <p><strong>置信度：</strong> ${confidence}%</p>
                        <p><strong>原始文本：</strong> "${data.text}"</p>
                    `;
                }
                
                resultDiv.style.display = 'block';
            }
            
            // 添加回车键提交功能
            document.getElementById('text-input').addEventListener('keypress', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    analyzeSentiment();
                }
            });
        </script>
    </body>
    </html>
    """
    return html_template

# 情感分析API路由
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # 获取请求数据
        data = request.get_json()
        text = data.get('text', '')
        
        if not text.strip():
            return jsonify({'error': '文本不能为空'})
        
        # 使用pipeline进行情感分析
        if sentiment_pipeline:
            result = sentiment_pipeline(text)[0]
            label = result['label']
            score = result['score']
            
            # 根据模型类型调整标签
            if label == 'POSITIVE':
                sentiment = '正面'
            elif label == 'NEGATIVE':
                sentiment = '负面'
            elif label == 'NEUTRAL':
                sentiment = '中性'
            else:
                sentiment = label
        else:
            # 模拟分析结果（当模型加载失败时）
            import random
            sentiments = ['正面', '负面', '中性']
            sentiment = random.choice(sentiments)
            score = random.uniform(0.7, 0.95)
        
        # 返回分析结果
        return jsonify({
            'text': text,
            'sentiment': sentiment,
            'confidence': score
        })
    
    except Exception as e:
        return jsonify({'error': f'分析失败: {str(e)}'}), 500

# 模型信息API
@app.route('/model-info')
def model_info():
    if sentiment_pipeline:
        try:
            model_name = sentiment_pipeline.model.name_or_path
            return jsonify({
                'model': model_name,
                'status': '已加载'
            })
        except:
            return jsonify({
                'model': '未知',
                'status': '已加载'
            })
    else:
        return jsonify({
            'model': '无',
            'status': '未加载（使用模拟结果）'
        })

if __name__ == '__main__':
    print("启动Flask应用...")
    print("情感分析模型状态:", "已加载" if sentiment_pipeline else "未加载（将使用模拟结果）")
    app.run(debug=True, host='0.0.0.0', port=5000)