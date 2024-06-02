import socket
import re
import multiprocessing
from functools import wraps

from .logger import Logger
from .config import config
from .error import *
from .temp import Template

URL_PATH = []
URL_FUNC = {}
REDIRECT = [False, ""]


class Request:
    def args():
        d_dict = {}
        data = recv_data.split()[1].split("?")[-1].split("&")
        if len(recv_data.split()[1].split("?")) > 1:
            for d in data:
                d_dict[d.split("=")[0]] = d.split("=")[1]
            return d_dict
        else:
            return ""


class Lanes():
    config = config

    def __init__(self) -> None:
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def route(f, url: str, method: str='GET'):
        def wrapper(f):
            URL_PATH.append(url)
            URL_FUNC[url] = [f, method]
        return wrapper

    def func_response(self, code: str, target: str = None):
        if code == "200":
            response = "HTTP/1.1 200 OK\r\n"
            response += "Server:pwb\r\n\
                Access-Control-Allow_credentials:true\r\n\
                Access-Control-Allow-Origin:*\r\n\
                Access-Control-Allow-Method:GET, POST, PUT\r\n\
                Access-Control-Allow-Headers:X-Custom-Header\r\n\r\n"
            return response
        elif code == "404":
            response = "HTTP/1.1 404\r\n"
            response += "Server:pwb\r\n\
                Access-Control-Allow_credentials:true\r\n\
                Access-Control-Allow-Origin:*\r\n\
                Access-Control-Allow-Method:GET, POST, PUT\r\n\
                Access-Control-Allow-Headers:X-Custom-Header\r\n\r\n"
            response += "<h1>Page no found</h1>\n<hr/>\n<p>Please check the url.<p>"
            return response
        elif code == "301":
            response = "HTTP/1.1 301\r\n"
            response += "Location: {}\r\n".format(target)
            return response
        else:
            raise HTTPCodeError("Please enter the correct HTTP code!")

    def run(self, host = "127.0.0.1", port = 5550, max_listen = 50):
        self.serverSocket.bind((host, port))
        self.serverSocket.listen(max_listen)
        Logger.logger(Logger, 0, "===================================================================================================================================")
        Logger.logger(Logger, 0, "The server is running successfully", force=True)
        Logger.logger(Logger, 0, f"Bind: http://{host}:{port}", force=True)
        print("------------------------------------------------------")

        while True:
            client, ip_port = self.serverSocket.accept()
            global recv_data
            global lines
            recv_data = client.recv(1024).decode('utf-8')
            lines = recv_data.splitlines()
            try:
                __request_file_path = re.match(r"[^/]+(/[^ ]*)", lines[0]).group(1)
            except Exception as e:
                Logger.logger(Logger, 3, str(e))
            multiprocessing.Process(target=self.handle_request, args=(client, recv_data, ip_port, __request_file_path,)).start()
            client.close()
        self.serverSocket.close()

    def handle_request(self, client, recv_data, ip_port, request_file_path):
        if REDIRECT[0]:
            response = self.func_response("301", target=REDIRECT[1])
            try:
                Logger.logger(Logger, 1, f"{recv_data.split()[0]} {recv_data.split()[1]} {ip_port[0]}:{str(ip_port[1])} 301")
                Logger.logger(Logger, 1, recv_data.split()[0] + " " + recv_data.split()[1] + " " + recv_data.split()[2] + " " + recv_data.split()[3] + recv_data.split()[4])
            except Exception as e:
                Logger.logger(Logger, 0, str(e))
            REDIRECT[0] = False
            REDIRECT[1] = ""
        else:
            try:
                if request_file_path.split("?")[0] in URL_PATH:
                        response = self.func_response("200")
                        response += URL_FUNC[request_file_path.split("?")[0]][0]()
                        try:
                            Logger.logger(Logger, 1, f"{recv_data.split()[0]} {recv_data.split()[1]} {ip_port[0]}:{str(ip_port[1])} 200")
                            Logger.logger(Logger, 1, recv_data.split()[0] + " " + recv_data.split()[1] + " " + recv_data.split()[2] + " " + recv_data.split()[3] + recv_data.split()[4])
                        except Exception as e:
                            Logger.logger(Logger, 0, str(e))
                else:
                    response = self.func_response("404")
                    try:
                        Logger.logger(Logger, 2, f"{recv_data.split()[0]} {recv_data.split()[1]} {ip_port[0]}:{str(ip_port[1])} 404")
                        Logger.logger(Logger, 2, recv_data.split()[0] + " " + recv_data.split()[1] + " " + recv_data.split()[2] + " " + recv_data.split()[3] + recv_data.split()[4])
                    except Exception as e:
                        Logger.logger(Logger, 0, str(e))
            except:
                pass

        
        response += "\r\n"

        client.send(response.encode('utf-8'))

        client.close()


def re_template(file_name: str, **kwargs):
    try:
        f = open(config["templates_folder"] + file_name, 'r')
        text = f.read()
        f.close()

        return Template.template_detect(Template, text, **kwargs)
    except IOError as e:
        Logger.logger(Logger, 2, str(e))
        raise HTTPCodeError("Check the file path or whether the file exists")

def redirect(target: str):
    try:
        REDIRECT[0] = True
        REDIRECT[1] = target
        print(REDIRECT)
    except Exception as e:
        Logger.logger(Logger, 3, str(e))
        raise HTTPRouteError("Please Check whether the route is correct")
