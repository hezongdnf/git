# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 自己的 __name__ 在自己用时就是 main，当自己作为模块被调用时就是自己的名字
    print(__name__)  # __main__
    print(print_hi.__name__)  #print_hi
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
