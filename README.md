# 这是一个什么项目？
Lanes是一个Python web框架，可用于Python web开发

# 版本更新
### V1.0.3
1. 优化了多任务接受http请求

# 使用教程
### 1. 一切从安装开始
使用命令`pip install Lanes`来安装Lanes
### 2. 主要函数/类

##### 1. Lanes: 主类
在你的代码中需要用 app = Lanes() 来实例化(app不一定叫app, 你可以自定义)

##### 2. run() 让你的代码跑起来
传入的参数： Host - 主机ip地址(默认: 127.0.0.1)
            Port - 监听的端口(默认: 5550)
            max_listen - 最大连接数(默认: 50)
示例: 

    from Lanes import Lanes

    app = Lanes()

    @app.route("/")
    def index():
        return 'Hello World!'

    if __name__ == "__main__":
        app.run()

##### 3. re_template() 返回HTML等文本文件的内容(以下默认以HTML为文本文件)
传入的参数: file_name - 文件名，默认寻找 \templates 目录下的file_name
           kwargs - 传入参数，作为HTML模板变量的 key 和 value
示例：

app.py:

    from Lanes import Lanes, re_template

    app = Lanes()

    @app.route("/")
    def index():
        return re_template("index.html")

    if __name__ == "__main__":
        app.run()
    
\templates\index.html:

    <html>...</html>

使用模板：
    这需要在HTML文件中用 "{{" 以及 "}}"将变量括起来

示例：
app.py:

    from Lanes import Lanes, re_template

    app = Lanes()

    @app.route("/")
    def index():
        return re_template("index.html", key="value")

    if __name__ == "__main__":
        app.run()
    
\templates\index.html:

    <html>
        <head>...</head>
        <body>
            <h1> The key is {{ key }}
        </body>
    </html>

渲染后：

<h1>The kay is value</h1>
