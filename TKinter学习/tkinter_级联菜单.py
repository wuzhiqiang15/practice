# 级联菜单的使用

import  tkinter


baseFrame = tkinter.Tk()
# 创建一个Menu实例，位置在主框架(baseFrame)上
menubar = tkinter.Menu(baseFrame)
# 创建一个Menu实例，位置在menubar这个菜单上
emenu = tkinter.Menu(menubar)

# 给emenu菜单增加子菜单
for item in ['Copy', 'Past', 'Cut']:
    emenu.add_command(label=item)

# 给menubar菜单增加子菜单
menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_command(label='About')

# 设置主框架(baseFrame)中显示的菜单是menubar
baseFrame['menu'] = menubar

baseFrame.mainloop()