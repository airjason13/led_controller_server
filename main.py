# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5 import QtWidgets
from mainwindow_c import MainWindow
from flask_plugin import *
import sys
import usb_utils
from flask import Flask

web_app = Flask(__name__)
from routes import *

out_eps = []
in_eps = []
STR_HELLO = "hello, led controller"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    qtapp = QtWidgets.QApplication([])
    window = MainWindow()
    window.move(0, 0)
    webapp = ApplicationThread(web_app)
    webapp.start()

    devs = usb_utils.find_pico()

    for dev in devs:
        out_ep_tmp, in_ep_tmp = usb_utils.get_ep(dev)
        out_eps.append(out_ep_tmp)
        in_eps.append(in_ep_tmp)
    hello_data = STR_HELLO.encode()
    for ep in out_eps:
        ep.write(hello_data)

    window.show()
    sys.exit(qtapp.exec_())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
