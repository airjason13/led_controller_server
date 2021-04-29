# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import usb_utils

out_eps = []
in_eps = []
STR_HELLO = "hello, led controller"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    devs = usb_utils.find_pico()

    for dev in devs:
        out_ep_tmp, in_ep_tmp = usb_utils.get_ep(dev)
        out_eps.append(out_ep_tmp)
        in_eps.append(in_ep_tmp)
    hello_data = STR_HELLO.encode()
    for ep in out_eps:
        ep.write(hello_data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
