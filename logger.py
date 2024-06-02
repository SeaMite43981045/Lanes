import time
import os
from .config import config

class Logger:
    log = {
        0:"\033[37m[DEBUG]\033[0m",
        1:"[INFO]\033[0m",
        2:"\033[93m[WARNING]\033[0m",
        3:"\033[91m[ERROR]\033[0m",
        4:"\033[95m[CRITICAL]\033[0m",
    }

    log_out = {
        0:"[DEBUG]",
        1:"[INFO]",
        2:"[WARNING]",
        3:"[ERROR]",
        4:"[CRITICAL]",
    }

    def logger(self, level: int, content: str, force:bool = False):
        if force == False:
            if config["lowest_level"] == 0:
                print(self.log[level] + " \033[32m" + time.strftime('[%Y-%m.%d-%H:%M:%S]') + "\033[0m " + content)
            elif config["lowest_level"] == 1:
                if level > 0:
                    print(self.log[level] + " \033[32m" + time.strftime('[%Y-%m.%d-%H:%M:%S]') + "\033[0m " + content)
            elif config["lowest_level"] == 2:
                if level > 1:
                    print(self.log[level] + " \033[32m" + time.strftime('[%Y-%m.%d-%H:%M:%S]') + "\033[0m " + content)
            elif config["lowest_level"] == 3:
                if level > 2:
                    print(self.log[level] + " \033[32m" + time.strftime('[%Y-%m.%d-%H:%M:%S]') + "\033[0m " + content)
            elif config["lowest_level"] == 4:
                if level > 3:
                    print(self.log[level] + " \033[32m" + time.strftime('[%Y-%m.%d-%H:%M:%S]') + "\033[0m " + content)
        else:
            print(self.log[level] + " \033[32m" + time.strftime('[%Y-%m.%d-%H:%M:%S]') + "\033[0m " + content)

        if config["log_output"] == True:
            if os.path.exists("log_out"):
                if os.path.exists("log_out/lanes." + time.strftime('%Y-%m.%d..%H') + ".log"):
                    f = open("log_out/lanes." + time.strftime('%Y-%m.%d..%H') + ".log",'a')
                    f.write(self.log_out[level] + " " + time.strftime('[%Y-%m.%d-%H:%M:%S]') + " " + content + "\n")
                    f.close
                else:
                    f = open("log_out/lanes." + time.strftime('%Y-%m.%d..%H') + ".log", 'w')
                    f.write(self.log_out[level] + " " + time.strftime('[%Y-%m.%d-%H:%M:%S]') + " " + content + "\n")
                    f.close
            else:
                os.mkdir("log_out")
                if os.path.exists("log_out/lanes." + time.strftime('%Y-%m.%d..%H') + ".log"):
                    f = open("log_out/lanes." + time.strftime('%Y-%m.%d..%H') + ".log",'a')
                    f.write(self.log_out[level] + " " + time.strftime('[%Y-%m.%d-%H:%M:%S]') + " " + content + "\n")
                    f.close
                else:
                    f = open("log_out/lanes." + time.strftime('%Y-%m.%d..%H') + ".log", 'w')
                    f.write(self.log_out[level] + " " + time.strftime('[%Y-%m.%d-%H:%M:%S]') + " " + content + "\n")
                    f.close
