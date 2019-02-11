# tkinter的常用组件
"""
- 按钮
    Button             按钮组件
    RadioButton        单选框组件
    CheckButton        选择按钮组件
    Listbox            列表框组件
 
- 文本输入组件
    Entry               单行文本框组件
    Text                多行文本框组件
    
- 标签组件
    Label               标签组件，可以显示图片和文字
    Message             标签组件，可以根据内容将文字换行

- 菜单
    Menu                菜单组件
    MenuButton          菜单按钮组件，可以使用Menu代替

- 滚动条
    scale               滑动组件
    Scrollbar           滚动条组件
    
- 其他组件
    Canvas              画布组件
    Frame               框架组件，将多个组件编组
    Toplevel            创建子窗口容器组件
"""

# 组件的布局方式
"""
组件有三种布局方式：
    - pack：按照方位布局
    - place：按照坐标布局
    - grid：网格布局
    
- pack布局：
    - 最简单，代码量最少，挨个摆放，默认从上到下，系统自动设置
    - 通用使用方式为：组件对象.pack()
    
- palce 布局
    - 明确方位的摆放

- grid 布局
    - 通用使用方式：组件对象.grid()
"""

import  tkinter

# 创建一个tkinter的主界面
base = tkinter.Tk()

# 设置主界面的标题
base.wm_title("Label Test")

# 设置Label组件
lb = tkinter.Label(base, text="Python Label")
# 设置Label组件显示的位置
lb.pack()

# 消息循环（使主界面一直存在）
base.mainloop()
