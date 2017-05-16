import os
import sys
import wx
import mymail
try:
    from agw import gradientbutton as GB
    bitmapDir = "bitmaps/"
except ImportError:  # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.gradientbutton as GB
    bitmapDir = "agw/bitmaps/"

wildcard = "Text File (*.txt)|*.txt|"  \
           "All files (*.*)|*.*"

recipient_id = ''

class SendMailWx(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'New Email Message (Plain Text)',
                          size=(800,550))
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.SetMaxSize((800,550))
        self.SetMinSize((800,550))
        self.CenterOnScreen()

        recipient_id = ''
        self.filepaths = []
        self.currentDir = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.createWidgets()
        self.attachTxt.Hide()
        self.editAttachBtn.Hide()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def createWidgets(self):
        p = self.panel
        self.fontmail = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)

        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.toLbl      = wx.StaticText(p, wx.ID_ANY, 'To :', size=(60,-1), pos = (20,20))
        self.toTxtb     = wx.Button(p, wx.ID_ANY, 'Browse file of the recipients',size = (300,25), pos = (90,18))
        self.subjectLbl = wx.StaticText(p, wx.ID_ANY, 'Subject :', size=(60,-1), pos = (20,57))
        self.subjectTxt = wx.TextCtrl(p, wx.ID_ANY, '', size = (680,-1), pos = (90,55))
        self.attachBtn  = wx.Button(p, wx.ID_ANY, 'Attachments', pos = (20,310))
        self.attachTxt  = wx.TextCtrl(p, wx.ID_ANY, '', style=wx.TE_MULTILINE, size = (520, -1), pos = (120,310))
        self.attachTxt.Disable()
        self.editAttachBtn = wx.Button(p, wx.ID_ANY, 'Edit Attachments', pos = (660,310))
        self.messageTxt = wx.TextCtrl(p, wx.ID_ANY, '', style=wx.TE_MULTILINE, size = (750,200), pos = (20,100))

        #wx.StaticText(p, wx.ID_ANY, "Sign In :", pos = (20,420)).SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.userlabel = wx.StaticText(p, wx.ID_ANY, "E-mail :", pos = (20,390)).SetFont(self.fontmail)
        self.userbox = wx.TextCtrl(p, wx.ID_ANY, "", size=(300, -1), pos = (110,390))
        self.passlabel = wx.StaticText(p, wx.ID_ANY, "Password :", pos = (20,430)).SetFont(self.fontmail)
        self.passbox = wx.TextCtrl(p, wx.ID_ANY, "", size=(300, -1), pos = (110,430), style=wx.TE_PASSWORD)
        self.createSendb()

        self.Bind(wx.EVT_BUTTON, self.onAttach, self.attachBtn)
        self.Bind(wx.EVT_BUTTON, self.onAttachEdit, self.editAttachBtn)
        self.Bind(wx.EVT_BUTTON, self.onToBrowse, self.toTxtb)
        self.Bind(wx.EVT_BUTTON, self.onSendMail, self.sendb)

        self.toLbl.SetFont(font)
        self.subjectLbl.SetFont(font)


    def createSendb(self):
        self.sendb = GB.GradientButton(self.panel, wx.ID_ANY, None, "Send", size=(85, -1), pos = (20,470))
        self.Bind(wx.EVT_BUTTON, self.onSendMail, self.sendb)

    def messageBox(self , m, mh):
        dlg = wx.MessageDialog(self, m, mh,
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

    def onAttach(self, event):

        attachments = self.attachTxt.GetLabel()
        filepath = ''

        # create a file dialog
        wildcard = "All files (*.*)|*.*"
        dialog = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        # if the user presses OK, get the path
        if dialog.ShowModal() == wx.ID_OK:
            self.attachTxt.Show()
            self.editAttachBtn.Show()
            filepath = dialog.GetPath()
            #print filepath
            # Change the current directory to reflect the last dir opened
            os.chdir(os.path.dirname(filepath))
            self.currentDir = os.getcwd()

            # add the user's file to the filepath list
            if filepath != '':
                self.filepaths.append(filepath)

            # get file size
            fSize = self.getFileSize(filepath)

            # modify the attachment's label based on it's current contents
            if attachments == '':
                attachments = '%s (%s)' % (os.path.basename(filepath), fSize)
            else:
                temp = '%s (%s)' % (os.path.basename(filepath), fSize)
                attachments = attachments + '; ' + temp
            self.attachTxt.SetLabel(attachments)
        dialog.Destroy()

    def getFileSize(self, f):
        import math
        fSize = os.stat(f).st_size
        if fSize >= 1073741824: # gigabyte
            fSize = int(math.ceil(fSize/1073741824.0))
            size = '%s GB' % fSize
        elif fSize >= 1048576:  # megabyte
            fSize = int(math.ceil(fSize/1048576.0))
            size = '%s MB' % fSize
        elif fSize >= 1024:           # kilobyte
            fSize = int(math.ceil(fSize/1024.0))
            size = '%s KB' % fSize
        else:
            size = '%s bytes' % fSize
        return size

    def onAttachEdit(self, event):
        from Mail2 import EditDialog
        #print 'in onAttachEdit...'
        attachments = ''

        dialog = EditDialog(self.filepaths)
        dialog.ShowModal()
        self.filepaths = dialog.filepaths
        #print 'Edited paths:\n', self.filepaths
        dialog.Destroy()

        if self.filepaths == []:
            # hide the attachment controls
            self.attachTxt.Hide()
            self.editAttachBtn.Hide()
        else:
            for path in self.filepaths:
                # get file size
                fSize = self.getFileSize(path)
                # Edit the attachments listed
                if attachments == '':
                    attachments = '%s (%s)' % (os.path.basename(path), fSize)
                else:
                    temp = '%s (%s)' % (os.path.basename(path), fSize)
                    attachments = attachments + '; ' + temp

            self.attachTxt.SetLabel(attachments)

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
        if u=='' or p=='':
            self.messageBox("  Empty parameters\n", "Error")
        else:
            self.sendb.SetLabel("Sending..")
            login_status = mymail.execute(u, p, recipient_id, self.subjectTxt.GetValue(), self.messageTxt.GetValue(), self.filepaths)
            if login_status == 0:
                self.messageBox(" E-Mail Not Sent\n", "Login Successful")
            elif login_status == 1:
                self.messageBox("  Mail Sent\n", "Login Successful")
            elif login_status == 3:
                self.messageBox("  Invalid Username or Password\n", "Login Failed")
            elif login_status == 2:
                self.messageBox("  Check your internet connection!\n", "Login Failed")
            elif login_status == 4:
                self.messageBox("  Unknown problem\n", "Login Failed")
            self.sendb.SetLabel("Send")



    def OnClose(self, event):
        self.Destroy()

def runMail():
    if __name__ == 'Mail':
        app1 = wx.App()
        frame1 = SendMailWx()
        frame1.Show()
        #SendMailWx.Bind(wx.EVT_CLOSE, SendMailWx.OnClose)
        app1.MainLoop()
