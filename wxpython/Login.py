# 基于WxPython的【登录】界面设计
# 实现功能清单：
# 1、登录：校验用户名和密码的正确性（已实现50%）
# 2、注册：校验用户名和密码的合法性（TODO）
# 3、找回密码：重新设置的密码，不得与原密码一致，不得设置含非法字符的密码（TODO）
# 4、勾选记住密码可30内免登录（TODO）
# 5、登录成功后，跳转到【每日计划管理系统】界面并注销原登录界面（DONE）

import webbrowser

import wx
from wx.lib.stattext import GenStaticText

import WorkPlanManage as wpk
import tools.verify as verify


class MyLogin:
    # 初始化登陆窗口，及其窗口控件
    def __init__(self, parent, fid, title, pos, size):
        self.window = wx.Frame(parent, fid, title, pos, size)
        self.window.Center()
        self.panel = wx.Panel(self.window)
        self.userText = wx.StaticText(parent=self.panel, label="用户名", pos=(100, 50))
        self.userTextCtrl = wx.TextCtrl(parent=self.panel, value="请输入手机号或者邮箱", size=(200, 25), pos=(150, 50),
                                        style=wx.TE_WORDWRAP)
        self.pwdText = wx.StaticText(parent=self.panel, label="密码", pos=(100, 90))
        self.pwdTextCtrl = wx.TextCtrl(parent=self.panel, size=(200, 25), pos=(150, 90), style=wx.TE_PASSWORD)
        # 记住密码
        self.rememberPwd = wx.CheckBox(parent=self.panel, label="记住密码（30天内有效）", pos=(100, 130))
        # 登录
        self.loginButton = wx.Button(parent=self.panel, label="登录", pos=(100, 160), size=(250, 30))
        # 忘记密码 | 注册新账号
        self.forgetPwdButton = wx.Button(parent=self.panel, label="忘记密码", pos=(150, 210))
        self.registerButton = wx.Button(parent=self.panel, label="注册账号", pos=(240, 210))
        # 阅读并接受 《服务条款》和 《隐私政策》
        self.readText = GenStaticText(parent=self.panel, label="阅读并接受", pos=(80, 290))
        self.linkWid = SuperLink(self.panel, label="《服务条款》", pos=(150, 290))
        self.linkWid.SetUrl("https://m.baidu.com/")
        self.andText = GenStaticText(parent=self.panel, label="和", pos=(250, 290))
        self.linkWid = SuperLink(self.panel, label="《隐私政策》", pos=(270, 290))
        self.linkWid.SetUrl("https://weread.qq.com/")

    # 登录相关的事件
    def event_login(self):
        self.loginButton.Bind(wx.EVT_BUTTON, self.CheckLogin)
        self.forgetPwdButton.Bind(wx.EVT_BUTTON, self.RecoverPwd)
        self.registerButton.Bind(wx.EVT_BUTTON, self.Register)

    def CheckLogin(self, e):
        print("CheckLogin =========> login start")
        # 勾选记住密码，可30内免登录
        if not self.rememberPwd.GetValue():
            # 校验用户名,是否符合手机号或者邮箱
            userName = self.userTextCtrl.GetValue()
            if not (verify.verify_mobile(userName) or verify.verify_mail(userName)):
                print("CheckLogin =========> userName error, userName = " + userName)
                msgDialog = wx.MessageDialog(None, "用户名错误，请输入正确的手机号或者邮箱!", "Error", wx.OK | wx.ICON_ERROR)
                msgDialog.ShowModal()
                return
                # 校验密码,需要连接数据库去校验 TODO
            pwd = self.pwdTextCtrl.GetValue()
            if pwd != "123456":
                print("CheckLogin =========> password error, password = " + pwd)
                pwdDialog = wx.MessageDialog(None, "密码错误，请输入正确的登录密码!", "Error", wx.OK | wx.ICON_ERROR)
                pwdDialog.ShowModal()
                return
        print("CheckLogin =========> login success")
        # 登录成功，则跳转到另一个主页窗口，并注销当前窗口
        self.SkipPlanPage()

    def RecoverPwd(self, e):
        print("RecoverPwd =========> recover start")
        findMsgDialog = wx.MessageDialog(None, "是否要找回密码?", "Question", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        modalValue = findMsgDialog.ShowModal()
        # 选择是的话（5103-是，5104-否），继续找回密码
        if modalValue == 5103:
            tipMsgDialog = wx.MessageDialog(None, "程序员小哥哥正在火速开发中，敬请期待哦......", "提示", wx.OK)
            tipMsgDialog.ShowModal()
        else:
            print("RecoverPwd =========> recover exit")
            return
        print("RecoverPwd =========> recover success")

    def Register(self, e):
        print("Register =========> register start")
        registerMsgDialog = wx.MessageDialog(None, "是否要注册新账号?", "Question",
                                             wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        modalValue = registerMsgDialog.ShowModal()
        # 选择是的话（5103-是，5104-否），继续注册
        if modalValue == 5103:
            tipMsgDialog = wx.MessageDialog(None, "程序员小哥哥正在火速开发中，敬请期待哦......", "提示", wx.OK)
            tipMsgDialog.ShowModal()
        else:
            print("Register =========> register exit")
            return
        print("Register =========> register success")

    def SkipPlanPage(self):
        # 销毁登录窗口
        self.window.Destroy()
        # 跳转到主页窗口
        print("SkipPlanPage =========> skip to work plan manage page")
        homePage = wpk.MyWork(parent=None, fid=-1, title="每日计划管理系统", pos=(300, 300), size=(950, 750))
        homePage.window.Show()


class SuperLink(GenStaticText):
    def __init__(self, *args, **kwargs):
        super(SuperLink, self).__init__(*args, **kwargs)
        self.font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, True, "Verdana")
        self.font2 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, "Verdana")
        self.SetFont(self.font2)
        # self.SetForegroundColour("#0000ff")
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
        self.Bind(wx.EVT_MOTION, self.OnMouseEvent)

    def SetUrl(self, url):
        self.url = url

    def OnMouseEvent(self, e):
        if e.LeftUp():
            webbrowser.open_new(self.url)
        elif e.Moving():
            self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            self.SetFont(self.font1)
            self.SetForegroundColour("#0000ff")
        else:
            self.SetCursor(wx.NullCursor)
            self.SetFont(self.font2)
            self.SetForegroundColour(wx.NullColour)
        e.Skip()


def main():
    app = wx.App()
    # 账号登录窗口
    login = MyLogin(parent=None, fid=-1, title="账号登录", pos=(200, 200), size=(500, 400))
    login.window.Show()
    login.event_login()
    app.MainLoop()


if __name__ == '__main__':
    main()
