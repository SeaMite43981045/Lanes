# What's this?
Lanes is a Python Web Frame, can be used for Python Web development.

# Version updates
### v1.0.3
1. Optimized multiprocess to accept HTTP requests

# How to use it?
### 1. Install
Use the command `pip install Lanes` to install Lanes

###2. Main Function/Class

##### 1. Lanes - Main class
You need to use `app = Lanes()` to instantiate the Lanes class.(You don't have to use "app" as its name, you can change it.)

##### 2. run() - Run your code
Args: Host - host IP address(default: 127.0.0.1)
      Port - Open ports(default: 5550)
      max_listen - Maximum number of connections(default: 50)

Example:

    from Lanes import Lanes

    app = Lanes()

    @app.route("/")
    def index():
        return 'Hello World!'

    if __name__ == "__main__":
        app.run()

##### 3. re_template() render text files such as HTML files.(The following uses HTML as a text file by default.)
Args: file_name - the name of text files
