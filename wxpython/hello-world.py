# wxPython入门小例子
import wx


def main():
    # 创建应用程序对象
    app = wx.App()
    # 创建容器(窗口)，并显示
    frm = wx.Frame(None, title="Hello World", size=(800, 500))
    frm.Center()
    frm.Show()
    # 执行主循环
    app.MainLoop()


if __name__ == '__main__':
    main()
