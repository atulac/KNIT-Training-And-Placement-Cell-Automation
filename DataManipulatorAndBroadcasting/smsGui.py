import os
import sys
import wx
import sms
try:
    from agw import gradientbutton as GB
    bitmapDir = "bitmaps/"
except ImportError:  # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.gradientbutton as GB
    bitmapDir = "agw/bitmaps/"

wildcard = "Text File (*.txt)|*.txt|"  \
           "All files (*.*)|*.*"

recipient_id = ''

class SendSMSWx(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'New SMS Message (Plain Text)',
                          size=(500,600))
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.SetMaxSize((500,600))
        self.SetMinSize((500,600))
        self.CenterOnScreen()

        recipient_id = ''
        self.filepaths = []
        self.currentDir = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.createWidgets()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def createWidgets(self):
        p = self.panel
        self.fontmail = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)

        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.toTxtb     = wx.Button(p, wx.ID_ANY, 'Browse file of the recipients',size = (300,25), pos = (90,28))
        self.messageTxt = wx.TextCtrl(p, wx.ID_ANY, '', style=wx.TE_MULTILINE, size = (440,180), pos = (20,90))
        if len(self.messageTxt.GetValue())>140:
            self.messageBox("  Please enter less than or equal to 140 characters"," Length Limit Exceeded")

        wx.StaticText(p, wx.ID_ANY, "Sign In to your way2sms.com Account:", pos = (30,330)).SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.userlabel = wx.StaticText(p, wx.ID_ANY, "Username :", pos = (30,390)).SetFont(self.fontmail)
        self.userbox = wx.TextCtrl(p, wx.ID_ANY, "", size=(300, -1), pos = (110,390))
        self.passlabel = wx.StaticText(p, wx.ID_ANY, "Password :", pos = (30,430)).SetFont(self.fontmail)
        self.passbox = wx.TextCtrl(p, wx.ID_ANY, "", size=(300, -1), pos = (110,430), style=wx.TE_PASSWORD)
        self.createSendb()

        self.Bind(wx.EVT_BUTTON, self.onToBrowse, self.toTxtb)
        self.Bind(wx.EVT_BUTTON, self.onSendMail, self.sendb)


    def createSendb(self):
        self.sendb = GB.GradientButton(self.panel, wx.ID_ANY, None, "Send", size=(85, -1), pos = (30,480))
        self.Bind(wx.EVT_BUTTON, self.onSendMail, self.sendb)

    def messageBox(self , m, mh):
        dlg = wx.MessageDialog(self, m, mh,
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()


    def onToBrowse(self, evt):
        global recipient_id
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            recipient_id = dlg.GetPath()
            #print 'hi', recipient_id
        dlg.Destroy()
        fname = os.path.basename(recipient_id)
        wx.StaticText(self.panel, wx.ID_ANY, fname,size = (500,-1), pos = (420,22)).SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD))
        #self.toTxtb.Destroy()

    def onSendMail(self, evt):
        global recipient_id
        u = self.userbox.GetValue()
        p = self.passbox.GetValue()
        self.sendb.SetLabel("Sending..")
        if u=='' or p=='':
            self.messageBox("  Empty parameters\n", "Error")
        else:
            login_status = sms.execute(recipient_id, u, p, self.messageTxt.GetValue())
            """if login_status == 0:
                self.messageBox(" SMS Not Sent\n", "Login Successful")
            elif login_status == 1:
                self.messageBox("  SMS Sent\n", "Login Successful")
            elif login_status == 3:
                self.messageBox("  Invalid Username or Password\n", "Login Failed")
            elif login_status == 2:
                self.messageBox("  Check your internet connection!\n", "Login Failed")
            elif login_status == 4:
                self.messageBox("  Unknown problem\n", "Login Failed")"""

        self.sendb.SetLabel("Send")



    def OnClose(self, event):
        self.Destroy()