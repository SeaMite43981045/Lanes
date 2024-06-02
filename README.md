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
    ```
    from Lanes import Lanes

    app = Lanes()

    @app.route("/")
    def index():
        return 'Hello World!'

    if __name__ == "__main__":
        app.run()
    ```
    
