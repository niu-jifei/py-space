# 演示flask框架，获取请求数据

from flask import Flask, jsonify, request, render_template_string

# Create an instance of Flask
app = Flask(__name__)

# 基本路由
@app.route('/')
def hello_world():
    person = {'name': '张三', 'age': 18}
    return jsonify(person)

# 1. 获取URL参数 (查询字符串)
@app.route('/query')
def get_query_params():
    # 获取单个参数
    name = request.args.get('name', '默认名称')
    # 获取多个同名参数
    hobbies = request.args.getlist('hobby')
    # 获取所有参数
    all_params = dict(request.args)
    
    return jsonify({
        'name': name,
        'hobbies': hobbies,
        'all_params': all_params
    })

# 2. 获取路径参数
@app.route('/user/<username>')
def get_path_param(username):
    return jsonify({'username': username})

# 3. 获取路径参数（带类型转换）
@app.route('/post/<int:post_id>')
def get_post(post_id):
    return jsonify({'post_id': post_id, 'type': 'int'})

# 4. 获取表单数据
@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        # 获取表单字段
        username = request.form.get('username')
        password = request.form.get('password')
        # 获取多选框数据
        interests = request.form.getlist('interests')
        
        return jsonify({
            'method': 'POST',
            'username': username,
            'password': password,
            'interests': interests
        })
    else:
        # 返回一个简单的表单页面
        form_html = """
        <form method="post">
            <p>用户名: <input type="text" name="username"></p>
            <p>密码: <input type="password" name="password"></p>
            <p>兴趣:
                <input type="checkbox" name="interests" value="读书"> 读书
                <input type="checkbox" name="interests" value="运动"> 运动
                <input type="checkbox" name="interests" value="音乐"> 音乐
            </p>
            <p><input type="submit" value="提交"></p>
        </form>
        """
        return form_html

# 5. 获取JSON数据
@app.route('/json', methods=['POST'])
def handle_json():
    # 检查请求是否包含JSON数据
    if not request.is_json:
        return jsonify({'error': '请求必须包含JSON数据'}), 400
    
    # 获取JSON数据
    data = request.get_json()
    
    # 处理数据
    if not data:
        return jsonify({'error': '无效的JSON数据'}), 400
    
    # 返回处理后的数据
    response = {
        'received_data': data,
        'message': 'JSON数据接收成功'
    }
    
    return jsonify(response)

# 6. 获取请求头信息
@app.route('/headers')
def get_headers():
    # 获取所有请求头
    headers = dict(request.headers)
    
    # 获取特定的请求头
    user_agent = request.headers.get('User-Agent')
    content_type = request.headers.get('Content-Type')
    
    return jsonify({
        'user_agent': user_agent,
        'content_type': content_type,
        'all_headers': headers
    })

# 7. 获取上传的文件
@app.route('/upload', methods=['GET', 'POST'])
def handle_upload():
    if request.method == 'POST':
        # 检查是否有文件上传
        if 'file' not in request.files:
            return jsonify({'error': '没有文件上传'}), 400
        
        file = request.files['file']
        
        # 检查文件名是否为空
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 获取文件信息
        filename = file.filename
        content_type = file.content_type
        file_size = len(file.read())
        file.seek(0)  # 重置文件指针
        
        return jsonify({
            'filename': filename,
            'content_type': content_type,
            'file_size': file_size,
            'message': '文件上传成功'
        })
    else:
        # 返回一个简单的文件上传表单
        upload_html = """
        <form method="post" enctype="multipart/form-data">
            <p>选择文件: <input type="file" name="file"></p>
            <p><input type="submit" value="上传"></p>
        </form>
        """
        return upload_html

# 8. 获取Cookie数据
@app.route('/cookie')
def get_cookies():
    # 获取所有Cookie
    cookies = dict(request.cookies)
    
    # 获取特定的Cookie
    username = request.cookies.get('username')
    
    # 设置Cookie（在响应中）
    response = jsonify({
        'username': username,
        'all_cookies': cookies
    })
    
    # 设置Cookie
    response.set_cookie('test_cookie', 'test_value')
    
    return response

# 9. 获取请求方法和URL信息
@app.route('/request-info')
def get_request_info():
    info = {
        'method': request.method,
        'url': request.url,
        'base_url': request.base_url,
        'path': request.path,
        'query_string': request.query_string.decode('utf-8'),
        'remote_addr': request.remote_addr,
        'host': request.host,
        'scheme': request.scheme
    }
    
    return jsonify(info)

# 10. 综合示例：处理不同类型的请求
@app.route('/api/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_api_request():
    if request.method == 'GET':
        # 获取查询参数
        data = {
            'method': 'GET',
            'params': dict(request.args)
        }
    elif request.method in ['POST', 'PUT']:
        # 获取请求体数据
        if request.is_json:
            data = {
                'method': request.method,
                'data': request.get_json()
            }
        elif request.form:
            data = {
                'method': request.method,
                'data': dict(request.form)
            }
        else:
            data = {
                'method': request.method,
                'data': '无有效数据'
            }
    elif request.method == 'DELETE':
        # 获取路径参数
        data = {
            'method': 'DELETE',
            'params': dict(request.args)
        }
    
    return jsonify(data)

# 11. 测试页面，包含各种请求方式的示例
@app.route('/test')
def test_page():
    test_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask 请求数据测试</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .section { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; }
            button { margin: 5px; padding: 5px 10px; }
            input { margin: 5px; }
        </style>
    </head>
    <body>
        <h1>Flask 请求数据测试</h1>
        
        <div class="section">
            <h2>1. URL参数测试</h2>
            <button onclick="testQueryParams()">测试URL参数</button>
            <div id="query-result"></div>
        </div>
        
        <div class="section">
            <h2>2. JSON数据测试</h2>
            <button onclick="testJsonData()">测试JSON数据</button>
            <div id="json-result"></div>
        </div>
        
        <div class="section">
            <h2>3. 请求头测试</h2>
            <button onclick="testHeaders()">测试请求头</button>
            <div id="headers-result"></div>
        </div>
        
        <div class="section">
            <h2>4. API测试</h2>
            <button onclick="testApi('GET')">GET请求</button>
            <button onclick="testApi('POST')">POST请求</button>
            <button onclick="testApi('PUT')">PUT请求</button>
            <button onclick="testApi('DELETE')">DELETE请求</button>
            <div id="api-result"></div>
        </div>
        
        <script>
            // 测试URL参数
            function testQueryParams() {
                fetch('/query?name=张三&hobby=读书&hobby=运动')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('query-result').innerHTML = 
                            '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
                    });
            }
            
            // 测试JSON数据
            function testJsonData() {
                fetch('/json', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: '李四',
                        age: 25,
                        hobbies: ['编程', '阅读']
                    })
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('json-result').innerHTML = 
                        '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
                });
            }
            
            // 测试请求头
            function testHeaders() {
                fetch('/headers')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('headers-result').innerHTML = 
                            '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
                    });
            }
            
            // 测试API
            function testApi(method) {
                const options = {
                    method: method
                };
                
                if (method === 'POST' || method === 'PUT') {
                    options.headers = {
                        'Content-Type': 'application/json'
                    };
                    options.body = JSON.stringify({
                        message: '这是一个测试请求',
                        timestamp: new Date().toISOString()
                    });
                }
                
                fetch('/api/data', options)
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('api-result').innerHTML = 
                            '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
                    });
            }
        </script>
    </body>
    </html>
    """
    return test_html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)