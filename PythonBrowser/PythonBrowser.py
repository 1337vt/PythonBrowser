import wx
import wx.html2
import wx.html


class WebBrowser(wx.Frame):
    go = []
    address = []
    browser = []
    history = []

    def GoButton(self, event):
        self.browser.LoadURL(self.address.GetValue())
        return

    def OnLoad(self, event):
        self.webtitle = self.browser.GetCurrentURL()
        self.history.InsertItems([self.webtitle], 0)
        return

    def NewWindow(self, event):
        title = self.browser.GetCurrentTitle()
        self.SetTitle(title)
        second_window = WebBrowser(None, title=title)
        second_window.browser.LoadURL(event.URL)
        second_window.Show()

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, id=-1, title=title)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.browser = wx.html2.WebView.New(self)
        self.address = wx.TextCtrl(self, value="http://www.google.com")
        self.go = wx.Button(self, label="Go!", id=wx.ID_OK)
        self.history = wx.ListBox(self, size=(100, -1), style=wx.LB_SINGLE)

        
        sizer.Add(self.address, proportion=3, flag=wx.EXPAND, border=10)
        sizer.Add(self.go, proportion=3, flag=wx.EXPAND, border=10)
        sizer.Add(self.browser, proportion=85, flag=wx.EXPAND, border=10)
        sizer.Add(self.history, proportion=9, flag=wx.EXPAND, border=10)

        self.SetSizer(sizer)
        self.SetSize((800, 600))

        self.Bind(wx.EVT_BUTTON, self.GoButton, self.go)
        self.Bind(wx.html2.EVT_WEBVIEW_NAVIGATED, self.OnLoad, self.browser)
        self.Bind(wx.html2.EVT_WEBVIEW_NEWWINDOW, self.NewWindow, self.browser)


app = wx.App()
main_window = WebBrowser(None, "Web Browser")
main_window.browser.LoadURL("http://google.com")
main_window.Show()
app.MainLoop()