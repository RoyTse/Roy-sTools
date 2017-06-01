#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import basechangefirend
import deci
import base64
# 首先，从源文件中将主窗体继承下来.就是修改过name属性的主窗体。


class MianWindow(basechangefirend.RoysTools):
    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。新建一个，然后再调用

    def init_main_window(self):
        pass

    def hex_btnOnButtonClick(self, event):
        try:
            Wait_hex = int(self.wait_hex.GetValue())
            Wait_hex_num = int(self.wait_hex_num.GetValue())
            To_hex = int(self.to_hex.GetValue())
        except Exception as e:
            dlg = wx.MessageDialog(
                None, u"输入有误", u"警告信息", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
        else:
            ten_hex = int(deci.N_2_decimal(Wait_hex_num, Wait_hex))
            list_Hex_num = deci.decimal_2_N(ten_hex, To_hex)
            list1 = []
            for x in reversed(list_Hex_num):
                x = str(x)
                list1.append(x)
            Hex_num = "".join(list1)
            self.hex_num.SetValue(Hex_num)

        finally:
            event.Skip()

    def hex_cp_btnOnButtonClick(self, event):
        # 取得剪贴板并确保其为打开状态
        text_obj = wx.TextDataObject()
        text_obj.SetText(self.hex_num.GetValue())
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_obj)
            wx.TheClipboard.Close()

    def asc_btnOnButtonClick(self, event):
        self.asc_char.Clear()
        Wait_asc_char = self.wait_asc_char.GetValue()
        wac = Wait_asc_char.split()
        for x in wac:
            int_asc_char = int(x)
            try:
                asc_char = chr(int_asc_char)
            except Exception as e:
                dlg = wx.MessageDialog(
                    None, u"输入有误", u"警告信息", wx.YES_NO | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
            else:
                self.asc_char.AppendText(asc_char)
            finally:
                pass
        event.Skip()

    def asc_cp_btnOnButtonClick(self, event):
        text_obj = wx.TextDataObject()
        text_obj.SetText(self.asc_char.GetValue())
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_obj)
            wx.TheClipboard.Close()

    def base_btnOnButtonClick(self, event):
        if self.m_choice1.GetStringSelection() == 'Encode':
            try:
                Base_char = base64.b64encode(self.wait_base_char.GetValue())
            except Exception as e:
                dlg = wx.MessageDialog(
                    None, u"输入有误", u"警告信息", wx.YES_NO | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
            else:
                self.base_char.SetValue(Base_char)
            finally:
                pass
        elif self.m_choice1.GetStringSelection() == 'Decode':
            try:
                Base_char = base64.b64decode(self.wait_base_char.GetValue())
            except Exception as e:
                dlg = wx.MessageDialog(
                    None, u"输入有误", u"警告信息", wx.YES_NO | wx.ICON_ERROR)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
            else:
                self.base_char.SetValue(Base_char)
            finally:
                pass
        event.Skip()

    def base_cp_btnOnButtonClick(self, event):
        text_obj = wx.TextDataObject()
        text_obj.SetText(self.base_char.GetValue())
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_obj)
            wx.TheClipboard.Close()

if __name__ == '__main__':
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = MianWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()
