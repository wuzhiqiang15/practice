# 菜单的使用

import tkinter

baseFrame = tkinter.Tk()

# 创建menu的实例（并且指定该Menu实例的位置）
# 以下代码就是指定menu实例的位置在baseFrame上
menubar = tkinter.Menu(baseFrame)

# add_command()方法，添加菜单(label )
for item in ['File', 'Edit', ' View', 'Help']:
    menubar.add_command(label=item)

# 设置主框架下显示的菜单
baseFrame['menu'] = menubar

baseFrame.mainloop()