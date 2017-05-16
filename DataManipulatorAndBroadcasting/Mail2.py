import wx
import os
import sys

class EditDialog(wx.Dialog):
    def __init__(self, filepaths):
        wx.Dialog.__init__(self, None, -1, 'Edit Attachments', size=(190,150))
        self.currentDir = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.filepaths = filepaths

        instructions = 'Check the items below that you no longer wish to attach to the email'
        lbl = wx.StaticText(self, wx.ID_ANY, instructions)
        #addBtn = wx.Button(self, wx.ID_ANY, 'Add')
        deleteBtn = wx.Button(self, wx.ID_ANY, 'Delete Items')
        cancelBtn = wx.Button(self, wx.ID_ANY, 'Cancel')

        #self.Bind(wx.EVT_BUTTON, self.onAdd, addBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(lbl, 0, wx.ALL, 5)

        self.chkList = wx.CheckListBox(self, wx.ID_ANY, choices=self.filepaths)
        mainSizer.Add(self.chkList, 0, wx.ALL, 5)

        #btnSizer.Add(addBtn, 0, wx.ALL|wx.CENTER, 5)
        btnSizer.Add(deleteBtn, 0, wx.ALL|wx.CENTER, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(mainSizer)
        self.Fit()
        self.Layout()

    def onCancel(self, event):
        self.Close()

    def onDelete(self, event):
        print 'in onDelete'
        numberOfPaths = len(self.filepaths)
        for item in range(numberOfPaths):
            val = self.chkList.IsChecked(item)
            if val == True:
                path = self.chkList.GetString(item)
                print path
                for i in range(len(self.filepaths)-1,-1,-1):
                    if path in self.filepaths[i]:
                        del self.filepaths[i]
        print 'new list =&gt; ', self.filepaths
        self.Close()

    """def onAdd(self, event):
        #attachments = self.attachTxt.GetLabel()
        filepath = ''

        # create a file dialog
        wildcard = "All files (*.*)|*.*"
        dialog = wx.FileDialog(None, 'Choose a file', self.currentDir,
                               '', wildcard, wx.OPEN)
        # if the user presses OK, get the path
        if dialog.ShowModal() == wx.ID_OK:
            #self.attachTxt.Show()
            #self.editAttachBtn.Show()
            filepath = dialog.GetPath()
            print filepath
            # Change the current directory to reflect the last dir opened
            os.chdir(os.path.dirname(filepath))
            self.currentDir = os.getcwd()

        # add the user's file to the filepath list
            if filepath != '':
                self.filepaths.append(filepath)

            # get file size
            fSize = self.getFileSize(filepath)"""

    """def getFileSize(self, f):
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
        return size"""