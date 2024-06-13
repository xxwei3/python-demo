# 基于WxPython的【每日计划管理系统】界面设计
# 实现功能清单：TODO

import wx
from wx.lib.stattext import GenStaticText


class MyWork:
    def __init__(self, parent, fid, title, pos, size):
        self.window = wx.Frame(parent, fid, title, pos, size)
        self.window.Center()
        self.panel = wx.Panel(self.window)
        self.readText = GenStaticText(parent=self.panel, label="欢迎欢迎", pos=(80, 250))
