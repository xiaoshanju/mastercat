from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    """
    渲染前端页面
    """
    print("llp")
    return render_template('index.html')

"""
这里可以定义各种接口，当我们需要后台操作一些东西的时候，就可以在这里定义，例如：
# 打开create_order页面
@app.route('/create_order')
def create_order_page():
    print("start create_order.html")
    return render_template('create_order.html')

# 访问外部请求数据并返回前端
@app.route('/get_ims_order_list', methods=['GET'])
def get_ims_order_list():
    try:
        response = requests.get("http://waibulianjie/xxx")
        data = response.text
        data = json.loads(data)["data"]
        res = []
        for item in data:
            id_title = item["id_title"]
            res.append(id_title)
        return jsonify(res), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
"""

# 主程序
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
