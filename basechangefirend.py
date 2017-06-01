# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Sep 12 2010)
# http://www.wxformbuilder.org/‰
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
# Class Roy'sTools
###########################################################################


class RoysTools(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Roy'sTools", pos=wx.DefaultPosition, size=wx.Size(
            640, 235), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(4, 4, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, u"待转换进制：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        gbSizer2.Add(self.m_staticText1, wx.GBPosition(
            1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(
            self, wx.ID_ANY, u"进制转换", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        self.m_staticText13.SetFont(
            wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        gbSizer2.Add(self.m_staticText13, wx.GBPosition(
            0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.wait_hex = wx.TextCtrl(
            self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wait_hex.SetMaxLength(2)
        gbSizer2.Add(self.wait_hex, wx.GBPosition(
            1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"待转换数字：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gbSizer2.Add(self.m_staticText2, wx.GBPosition(
            2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.wait_hex_num = wx.TextCtrl(
            self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.wait_hex_num, wx.GBPosition(
            2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(
            self, wx.ID_ANY, u"目标进制：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gbSizer2.Add(self.m_staticText7, wx.GBPosition(
            3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.to_hex = wx.TextCtrl(
            self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        self.to_hex.SetMaxLength(2)
        gbSizer2.Add(self.to_hex, wx.GBPosition(
            3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"转换后数字：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gbSizer2.Add(self.m_staticText3, wx.GBPosition(
            4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.hex_num = wx.TextCtrl(
            self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.hex_num, wx.GBPosition(
            4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.hex_btn = wx.Button(
            self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.hex_btn, wx.GBPosition(
            5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.hex_cp_btn = wx.Button(
            self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.hex_cp_btn, wx.GBPosition(
            5, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        fgSizer1.Add(gbSizer2, 1, wx.EXPAND, 5)

        gbSizer21 = wx.GridBagSizer(0, 0)
        gbSizer21.SetFlexibleDirection(wx.BOTH)
        gbSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText11 = wx.StaticText(
            self, wx.ID_ANY, u"待转换字符：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gbSizer21.Add(self.m_staticText11, wx.GBPosition(
            1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText131 = wx.StaticText(
            self, wx.ID_ANY, u"ASCII转换", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText131.Wrap(-1)
        self.m_staticText131.SetFont(
            wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        gbSizer21.Add(self.m_staticText131, wx.GBPosition(
            0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(
            self, wx.ID_ANY, u"进制与asc可\n同时转换多\n个字符，用\n空格隔开", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText12.Wrap(-1)
        gbSizer21.Add(self.m_staticText12, wx.GBPosition(
            4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.wait_asc_char = wx.TextCtrl(
            self, wx.ID_ANY, u"48", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer21.Add(self.wait_asc_char, wx.GBPosition(
            1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(
            self, wx.ID_ANY, u"转换后字符：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        gbSizer21.Add(self.m_staticText21, wx.GBPosition(
            2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.asc_char = wx.TextCtrl(
            self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer21.Add(self.asc_char, wx.GBPosition(
            2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.asc_btn = wx.Button(
            self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer21.Add(self.asc_btn, wx.GBPosition(
            3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.asc_cp_btn = wx.Button(
            self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer21.Add(self.asc_cp_btn, wx.GBPosition(
            3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        fgSizer1.Add(gbSizer21, 1, wx.EXPAND, 5)

        gbSizer211 = wx.GridBagSizer(0, 0)
        gbSizer211.SetFlexibleDirection(wx.BOTH)
        gbSizer211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText111 = wx.StaticText(
            self, wx.ID_ANY, u"待转换字符：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        gbSizer211.Add(self.m_staticText111, wx.GBPosition(
            1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText1311 = wx.StaticText(
            self, wx.ID_ANY, u"base64", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1311.Wrap(-1)
        self.m_staticText1311.SetFont(
            wx.Font(20, 70, 90, 90, False, wx.EmptyString))

        gbSizer211.Add(self.m_staticText1311, wx.GBPosition(
            0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.wait_base_char = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer211.Add(self.wait_base_char, wx.GBPosition(
            1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText211 = wx.StaticText(
            self, wx.ID_ANY, u"转换后字符：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText211.Wrap(-1)
        gbSizer211.Add(self.m_staticText211, wx.GBPosition(
            2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.base_char = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer211.Add(self.base_char, wx.GBPosition(
            2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.base_btn = wx.Button(
            self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer211.Add(self.base_btn, wx.GBPosition(
            4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_choice1Choices = [u"Encode", u"Decode"]
        self.m_choice1 = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        gbSizer211.Add(self.m_choice1, wx.GBPosition(
            3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.base_cp_btn = wx.Button(
            self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer211.Add(self.base_cp_btn, wx.GBPosition(
            4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        fgSizer1.Add(gbSizer211, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.hex_btn.Bind(wx.EVT_BUTTON, self.hex_btnOnButtonClick)
        self.hex_cp_btn.Bind(wx.EVT_BUTTON, self.hex_cp_btnOnButtonClick)
        self.asc_btn.Bind(wx.EVT_BUTTON, self.asc_btnOnButtonClick)
        self.asc_cp_btn.Bind(wx.EVT_BUTTON, self.asc_cp_btnOnButtonClick)
        self.base_btn.Bind(wx.EVT_BUTTON, self.base_btnOnButtonClick)
        self.base_cp_btn.Bind(wx.EVT_BUTTON, self.base_cp_btnOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def hex_btnOnButtonClick(self, event):
        event.Skip()

    def hex_cp_btnOnButtonClick(self, event):
        event.Skip()

    def asc_btnOnButtonClick(self, event):
        event.Skip()

    def asc_cp_btnOnButtonClick(self, event):
        event.Skip()

    def base_btnOnButtonClick(self, event):
        event.Skip()

    def base_cp_btnOnButtonClick(self, event):
        event.Skip()
