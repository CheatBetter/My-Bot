"""

MIT License

Copyright (c) 2023 CheatBetter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

"""

Logger utility (This is stolen from one of my latest library that is soon to be released)

"""
import time as tim
from colorama import Style, Fore
from typing import Any
from enum import Enum

class LogLevel(Enum):
    INFO = Fore.WHITE
    DEBUG = Fore.CYAN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    EXIT = Fore.BLACK

class Logger:
    """A simple logger for discord bots

    Args:
        name (str): Name of the logger
        time (bool): If the logger should display time
        color (colorama.Fore): Color of the logger name
        style (colorama.Style): Style of the logger name
        t_color (colorama.Fore): Color of the logger time
        t_style (colorama.Style): Style of the logger time 
        version (str): Version of the discord bot
        dev_mode (bool): If the bot is in development mode
    """
    def __init__(self, name: str, time: bool, color: Fore, style: Style, t_color: Fore, t_style: Style, version: str, dev_mode: bool) -> None:
        self.name = name
        self.time = time
        self.color = color
        self.style = style
        self.t_color = t_color
        self.t_style = t_style
        self.version = version
        self.dev_mode = dev_mode
    
    def log(self, msg: str, level: LogLevel, time: bool, dev_mode: bool) -> Any:
        """Main logging function, used throughout the class and can be used to make custom messages

        Args:
            msg (str): The message it logs
            level (LogLevel): Level of log
            time (bool): If it displays time
            dev_mode (bool): If it is in dev mode
        """        
        if time and dev_mode is True:
            print(f"{self.t_color or Fore.CYAN}{self.t_style or Style.BRIGHT}[{tim.ctime()}] ({self.color}{self.style}{self.name}) {Fore.RED}{Style.BRIGHT}DEV {level.value}{Style.DIM}{level.name} ---> {msg}{Style.RESET_ALL}")
            return
        if time is True:
            print(f"{self.t_color or Fore.CYAN}{self.t_style or Style.BRIGHT}[{tim.ctime()}] ({self.color}{self.style}{self.name}) {level.value}{Style.DIM}{level.name} ---> {msg}{Style.RESET_ALL}")
            return
        if dev_mode is True:
            print(f"({self.color}{self.style}{self.name}){Fore.RED}{Style.BRIGHT} DEV {level.value}{Style.DIM}{level.name} ---> {msg}{Style.RESET_ALL}")
            return
    
    def debug(self, msg: str) -> Any:
        """Logs a debug message

        Args:
            msg (str): Message it logs
        """        
        self.log(msg=msg, level=LogLevel.DEBUG, time=self.time, dev_mode=self.dev_mode)
    
    def info(self, msg: str) -> Any:
        """Logs a informational message

        Args:
            msg (str): Message it logs
        """        
        self.log(msg=msg, level=LogLevel.INFO, time=self.time, dev_mode=self.dev_mode)
    

    def warn(self, msg: str) -> Any:
        """Logs a warning message

        Args:
            msg (str): Message it logs
        """        
        self.log(msg=msg, level=LogLevel.WARNING, time=self.time, dev_mode=self.dev_mode)
    
    def error(self, msg: str) -> Any:
        """Logs a error message

        Args:
            msg (str): Message it logs
        """        
        self.log(msg=msg, level=LogLevel.ERROR, time=self.time, dev_mode=self.dev_mode)