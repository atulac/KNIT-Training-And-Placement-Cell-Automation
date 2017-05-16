import wx
from wx.lib import masked
import wx.lib.filebrowsebutton as filebrowse
import export
import merge
import os
import importdb
from wx.lib.wordwrap import wordwrap
import wx.lib.scrolledpanel as scrolled
import xlrd
import wx.lib.buttons as buttons
import sys
import Mail
import smsGui

try:
    from agw import gradientbutton as GB
    bitmapDir = "bitmaps/"
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.gradientbutton as GB
    bitmapDir = "agw/bitmaps/"

year = ''
branch = ''
colList = []
pathm1 = ''
pathm2 = ''
table = ''
n1 = 1
n2 = 0

wildcard = "Python source (*.py)|*.py|"             \
           "Compiled Python (*.pyc)|*.pyc|"         \
           "Text File (*.txt)|*.txt|"               \
           "Excel Workbook (*.xlsx)|*.xlsx|"        \
           "Excel 97-2003 Workbook (*.xls)|*.xls|"  \
           "All files (*.*)|*.*"

class MainWindow1(wx.Frame):
    def __init__(self,parent,id):

        wx.Frame.__init__(self, parent, id,"KNIT TPO", size=(1000,700))

        self.Maximize(True)
        self.SetAutoLayout(True)

        self.font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD)


        self.panelA = scrolled.ScrolledPanel(self, -1, style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panelA" )
        lc = wx.LayoutConstraints()
        lc.top.SameAs(self, wx.Top, 10)
        lc.left.SameAs(self, wx.Left, 10)
        lc.bottom.PercentOf(self, wx.Bottom, 37)
        lc.right.PercentOf(self, wx.Right, 51)
        self.panelA.SetConstraints(lc)
        self.panelA.SetupScrolling()


        self.panelB = scrolled.ScrolledPanel(self, -1, style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panelB" )
        lc = wx.LayoutConstraints()
        lc.top.Below(self.panelA, 7)
        lc.right.PercentOf(self, wx.Right, 51)
        lc.bottom.SameAs(self, wx.Bottom, 10)
        lc.left.SameAs(self, wx.Left, 10)
        self.panelB.SetConstraints(lc)
        self.panelB.SetupScrolling()


        self.panelC = scrolled.ScrolledPanel(self, -1, style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panelC" )
        lc = wx.LayoutConstraints()
        lc.top.SameAs(self, wx.Top, 10)
        lc.right.SameAs(self, wx.Right, 10)
        lc.bottom.PercentOf(self, wx.Bottom, 37)
        lc.left.RightOf(self.panelA, 7)
        self.panelC.SetConstraints(lc)
        self.panelC.SetupScrolling()

        self.panelE = wx.Window(self, -1, style=wx.SIMPLE_BORDER)
        lc = wx.LayoutConstraints()
        lc.top.Below(self.panelC, 7)
        lc.right.SameAs(self, wx.Right, 10)
        lc.bottom.SameAs(self, wx.Bottom, 140)
        lc.left.RightOf(self.panelA, 7)
        self.panelE.SetConstraints(lc)


        self.panelD = wx.Window(self, -1, style=wx.SIMPLE_BORDER)
        lc = wx.LayoutConstraints()
        lc.top.Below(self.panelE, 7)
        lc.right.SameAs(self, wx.Right, 10)
        lc.bottom.SameAs(self, wx.Bottom, 10)
        lc.left.RightOf(self.panelB, 7)
        self.panelD.SetConstraints(lc)


        self.Fit()
        self.SetMinSize((1000, 700))

        self.e1b = wx.Button(self.panelA,label="Precise Sheet", pos=(1,225), size=(136.8,22))
        self.e2b = wx.Button(self.panelA,label="CarryOvers Sheet", pos=(136.8,225), size=(138,22))
        self.e3b = wx.Button(self.panelA,label="Detailed Sheet", pos=(273.6,225), size=(138,22))
        self.e4b = wx.Button(self.panelA,label="Branch Changers", pos=(410.4,225), size=(138,22))
        self.e5b = wx.Button(self.panelA,label="UFM", pos=(547.2,225), size=(136.8,22))
        self.Bind(wx.EVT_BUTTON, self.onE1b, self.e1b)
        self.Bind(wx.EVT_BUTTON, self.onE2b, self.e2b)
        self.Bind(wx.EVT_BUTTON, self.onE3b, self.e3b)
        self.Bind(wx.EVT_BUTTON, self.onE4b, self.e4b)
        self.Bind(wx.EVT_BUTTON, self.onE5b, self.e5b)
        self.e1b.Enable(False)

        self.ExportData(1)
        self.ImportData()
        self.MergeData()
        self.BroadcastMessage()
        self.MainPanel()

        self.Bind(wx.EVT_CLOSE, self.OnClose)





#<<-----------------------------------------------------Extract Sheets Panel----------------------------------------------------------------->>


    def ExportData(self, n):
        global year, branch, table
        year = ''
        branch = ''
        yearList = ['First Year','Second Year','Third Year']
        branchList = ['CSE','EL','CE','IT','ME','EE','MCA']

        exbmpreset = wx.Bitmap(os.path.normpath(os.getcwd()+"\\reset.jpg"))
        self.expresetb = buttons.GenBitmapButton(self.panelA, -1, exbmpreset, pos = (630,10), style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, self.onE1b, self.expresetb)

        wx.StaticText(self.panelA, -1, "Extract Sheets ", (20, 20)).SetFont(self.font)

        wx.StaticText(self.panelA, -1, "Select Year : ", (70, 90), (75, -1))
        self.chyr = wx.Choice(self.panelA, -1, pos =(150, 85), size = (100,-1), choices = yearList)

        self.sb = wx.StaticText(self.panelA, -1, "Select Branch : ", (310, 90), (85, -1))
        self.chbr = wx.Choice(self.panelA, -1, pos = (400, 85), size = (100,-1), choices = branchList)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice2, self.chbr)
        if n == 1:
            table = 'precise'
        if n == 2:
            table = 'grade_status'
        if n == 3:
            table = 'detailed'
        if n == 4:
            table = 'branch_changers'
            self.sb.Hide()
            branch = 'CSE'  #default branch
            self.chbr.Hide()
        if n == 5:
            table = 'ufm'
            self.sb.Hide()
            branch = 'CSE'  #default branch
            self.chbr.Hide()

        self.Bind(wx.EVT_CHOICE, self.EvtChoice1, self.chyr)

        self.expdoneb = wx.Button(self.panelA,label="Extract and Save As", pos=(150,155), size=(350,25))
        #exbmbdone = wx.Bitmap(os.path.normpath(os.getcwd()+"\\extractb.png"))
        #self.expdoneb = buttons.GenBitmapButton(self.panelA, -1, exbmbdone, pos = (145,140), style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, self.SaveEvt, self.expdoneb)
        self.expdoneb.Enable(False)

    def resetExportData(self):
        self.sb.Destroy()
        self.chyr.Destroy()
        self.chbr.Destroy()
        self.expdoneb.Destroy()
        self.expresetb.Destroy()

#<<-----------------------------------------------------End of Extract Sheets Panel----------------------------------------------------------------->>
















#<<-----------------------------------------------------Import Sheets Panel----------------------------------------------------------------->>


    def ImportData(self):
        global colList, n1, n2
        colList = []
        n1 = 1
        n2 = 0

        imbmpreset = wx.Bitmap(os.path.normpath(os.getcwd()+"\\reset.jpg"))
        self.impresetb = buttons.GenBitmapButton(self.panelB, -1, imbmpreset, pos = (630,10), style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, self.resetImportData, self.impresetb)

        global fontim
        fontim = wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD)

        wx.StaticText(self.panelB,-1, "Import Sheets ", (20, 20)).SetFont(self.font)

        self.fbbimp = filebrowse.FileBrowseButton(self.panelB, -1, size=(470, -1), pos=(70,95), changeCallback = self.ImpfbbCallback )
        self.fbbimp.SetLabel("Select File")

        self.ImpCreateEditb()
        self.ImpCreateDoneb()


    def resetImportData(self,event):
        global n1, n2
        self.impsaveb.Destroy()
        self.impsaveasb.Destroy()
        if n1 == 1:
            self.fbbimp.Destroy()
            self.impconvb.Destroy()
            self.impeditb.Destroy()
            self.impresetb.Destroy()
            n1 = 0
        if n2 == 1:
            self.impcb.Destroy()
            self.impcb1.Destroy()
            self.impcb2.Destroy()
            self.impcb3.Destroy()
            self.impcb4.Destroy()
            #self.impsaveb.Destroy()
            #self.impsaveasb.Destroy()
            self.min0.Destroy()
            self.min1.Destroy()
            self.min2.Destroy()
            self.min3.Destroy()
            self.min4.Destroy()
            self.max1.Destroy()
            self.max2.Destroy()
            self.max3.Destroy()
            #self.max4.Destroy()
            #wx.StaticText(self.panelB, -1, "                ", pos=(360, 170)).SetFont(fontim)
            #wx.StaticText(self.panelB, -1, "                ", pos=(360, 210)).SetFont(fontim)
            #wx.StaticText(self.panelB, -1, "                ", pos=(360, 250)).SetFont(fontim)
            #wx.StaticText(self.panelB, -1, "                ", pos=(360, 290)).SetFont(fontim)
            self.impdpc.Destroy()
            self.impresetb.Destroy()
            n2 = 0
        self.ImportData()


#<<-----------------------------------------------------End of Import Sheets Panel----------------------------------------------------------------->>











#<<-------------------------------------------------------------Merge Database Panel----------------------------------------------------------------->>


    def MergeData(self):
        global pathm1, pathm2
        pathm1 = ''
        pathm2 = ''
        mergebmpreset = wx.Bitmap(os.path.normpath(os.getcwd()+"\\reset.jpg"))
        self.mergeresetb = buttons.GenBitmapButton(self.panelC, -1, mergebmpreset, pos = (595,10), style=wx.BORDER_NONE)
        self.Bind(wx.EVT_BUTTON, self.resetMergeData, self.mergeresetb)

        wx.StaticText(self.panelC,-1, "Merge Sheets ", (20, 20)).SetFont(self.font)

        self.fbb1 = filebrowse.FileBrowseButton(self.panelC, -1, size=(450, -1), pos=(70,70), changeCallback = self.fbbCallback1 )
        self.fbb1.SetLabel("1st File :")
        self.fbb2 = filebrowse.FileBrowseButton(self.panelC, -1, size=(450, -1), pos=(70,120), changeCallback = self.fbbCallback2 )
        self.fbb2.SetLabel("2nd File :")

        self.mergeb = wx.Button(self.panelC,label="Merge and Save As", pos=(137,190), size=(350,25))
        self.Bind(wx.EVT_BUTTON, self.MergeEvt, self.mergeb)
        self.mergeb.Enable(False)


    def resetMergeData(self, event):
        self.fbb1.Destroy()
        self.fbb2.Destroy()
        self.mergeb.Destroy()
        self.mergeresetb.Destroy()
        self.MergeData()

#<<----------------------------------------------------------End of Merge Database Panel-------------------------------------------------------------->>















#<<-------------------------------------------------------------Broadcast Message Panel----------------------------------------------------------------->>


    def BroadcastMessage(self):
        self.BMhead = wx.StaticText(self.panelE,-1, "Broadcast Message ", (20, 20)).SetFont(self.font)

        brbmpmail = wx.Bitmap(os.path.normpath(os.getcwd()+"\\mail.png"))
        #brbmpmail.SetMaskColour("white")
        self.brmailb = buttons.GenBitmapButton(self.panelE, -1, brbmpmail, pos = (125,105), style=wx.BORDER_NONE)

        brbmpsms = wx.Bitmap(os.path.normpath(os.getcwd()+"\\sms2.png"))
        #brbmpsms.SetMaskColour("white")
        self.brsmsb = buttons.GenBitmapButton(self.panelE, -1, brbmpsms, pos = (380,105), style=wx.BORDER_NONE)

        self.Bind(wx.EVT_BUTTON, self.onEmail, self.brmailb)
        self.Bind(wx.EVT_BUTTON, self.onSMS, self.brsmsb)


    def onEmail(self, event):
        Mail.runMail()

    def onSMS(self, event):
        app2 = wx.App()
        frame2 = smsGui.SendSMSWx()
        frame2.Show()
        #frame2.Bind(wx.EVT_CLOSE, frame2.OnClose2)
        app2.MainLoop()

    #def OnClose2(x, event):
        #x.Destroy()

#<<---------------------------------------------------------End of Broadcast Message Panel-------------------------------------------------------------->>
















#<<-------------------------------------------------------------The Main App Panel-------------------------------------------------------------------->>

    def MainPanel(self):
        aboutb = wx.Button(self.panelD,label="About", pos=(80,40), size= (200,30))
        self.Bind(wx.EVT_BUTTON, self.aboutevt, aboutb)

        helpb = wx.Button(self.panelD,label="In-App-Tutorial", pos=(400,40), size= (200,30))
        self.Bind(wx.EVT_BUTTON, self.onAppTutb, helpb)


#<<------------------------------------------------------------End The Main App Panel----------------------------------------------------------------->>














#<<***********************************************************Function Calling************************************************************************>>


    def messageBoxOK(self , m, mh):
        dlg = wx.MessageDialog(self, m, mh,
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

    def messageBoxYES(self , m, mh):
        global n1
        dlg = wx.MessageDialog(self, m, mh,
                               #wx.OK | wx.ICON_INFORMATION
                               wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION
                               )
        if dlg.ShowModal() == wx.ID_YES:
            pass
        dlg.Destroy()



#=======================================================Functions of Export==================================================================


    def onE1b(self, event):
        self.resetExportData()
        self.ExportData(1)
        self.e1b.Enable(False)
        self.e2b.Enable(True)
        self.e3b.Enable(True)
        self.e4b.Enable(True)
        self.e5b.Enable(True)

    def onE2b(self, event):
        self.resetExportData()
        self.ExportData(2)
        self.e2b.Enable(False)
        self.e1b.Enable(True)
        self.e3b.Enable(True)
        self.e4b.Enable(True)
        self.e5b.Enable(True)

    def onE3b(self, event):
        self.resetExportData()
        self.ExportData(3)
        self.e3b.Enable(False)
        self.e2b.Enable(True)
        self.e1b.Enable(True)
        self.e4b.Enable(True)
        self.e5b.Enable(True)

    def onE4b(self, event):
        global year
        self.resetExportData()
        self.ExportData(4)
        self.e4b.Enable(False)
        self.e2b.Enable(True)
        self.e3b.Enable(True)
        self.e1b.Enable(True)
        self.e5b.Enable(True)

    def onE5b(self, event):
        global year
        self.resetExportData()
        self.ExportData(5)
        self.e5b.Enable(False)
        self.e2b.Enable(True)
        self.e3b.Enable(True)
        self.e1b.Enable(True)
        self.e4b.Enable(True)

    def EvtChoice1(self, event):
        global year
        year = event.GetString()
        if branch != '':
            self.expdoneb.Enable(True)

    def EvtChoice2(self, event):
        global branch
        branch = event.GetString()
        if year != '':
            self.expdoneb.Enable(True)

    def SaveEvt(self, evt):
        global year, branch, table
        dlg = wx.FileDialog(
              self, message="Save file as ...", defaultDir=os.getcwd(),
              defaultFile="", wildcard=wildcard, style=wx.SAVE )

        dlg.SetFilterIndex(4)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            export.execute(table, year, branch, path)

        dlg.Destroy()




#=======================================================Functions of Import==================================================================



    def ImpfbbCallback(self, evt):
        global colList
        try:
            self.impeditb.Enable(True)
            self.impconvb.Enable(True)
            self.impeditb.Show()
            self.impconvb.Show()
            self.impsaveb.Show()
            self.impsaveasb.Show()
            self.pathimp = evt.GetString()
            colList = importdb.execute(self.pathimp)
        except xlrd.biffh.XLRDError:
            self.OnXLRDError()


    def ImpCreateEditb(self):
        self.impeditb = wx.Button(self.panelB,label="Set Criteria", pos=(160,250), size=(350,27))
        self.Bind(wx.EVT_BUTTON, self.ImpOnEditbEvt, self.impeditb)
        self.impeditb.Enable(False)
        self.impconvb = wx.Button(self.panelB, -1, "Convert Marks to Percentage", pos = (250, 180))
        self.Bind(wx.EVT_BUTTON, self.ImpOnConvbEvt, self.impconvb)
        self.impconvb.Enable(False)


    def ImpCreateDoneb(self):
        self.impsaveb = wx.Button(self.panelB,label="Save", pos=(360,380), size=(140,-1))
        self.Bind(wx.EVT_BUTTON, self.ImpOnSavebEvt, self.impsaveb)
        self.impsaveb.Enable(False)
        self.impsaveb.Hide()
        self.impsaveasb = wx.Button(self.panelB,label="Save As", pos=(510,380), size=(140,-1))
        self.Bind(wx.EVT_BUTTON, self.ImpOnSaveAsbEvt, self.impsaveasb)
        self.impsaveasb.Enable(False)
        self.impsaveasb.Hide()


    def OnXLRDError(self):
        self.messageBoxOK('  The file you have selected is Empty.  \n \n  Please select a valid file...  \n',
                               'XLRD Error!',)


    def ImpOnConvbEvt(self, event):
        #self.messageBoxYES("This action will convert marks details(if any) to percentage format.\nDo you want to continue?"," Confirmation")
        dlg = wx.MessageDialog(self,"This action will convert marks details(if any) to percentage format.\nDo you want to continue?"," Confirmation",
                               #wx.OK | wx.ICON_INFORMATION
                               wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION
                               )
        if dlg.ShowModal() == wx.ID_YES:
            importdb.convertToPercent()
            self.impconvb.Disable()
            self.impsaveb.Enable()
            self.impsaveasb.Enable()
        dlg.Destroy()


    def ImpOnEditbEvt(self, event):
        global counter,n1,n2
        n1 = 0
        n2 = 1
        counter = 0
        self.impeditb.Hide()
        self.impconvb.Hide()
        self.fbbimp.Hide()
        #self.impsaveb.Show()
        #self.impsaveasb.Show()
        self.impsaveasb.Enable(True)
        self.impsaveb.Enable(True)
        self.ImpSetCriteria()


    def ImpOnSaveAsbEvt(self, evt):
        if n1==0 and n2==1:
            importdb.another()
            self.impGetValue()
        dlg = wx.FileDialog(
              self, message="Save file as ...", defaultDir=os.getcwd(),
              defaultFile="", wildcard=wildcard, style=wx.SAVE )
        dlg.SetFilterIndex(4)
        if dlg.ShowModal() == wx.ID_OK:
            pathsaveas = dlg.GetPath()
            importdb.save(pathsaveas)
        dlg.Destroy()


    def ImpOnSavebEvt(self, evt):
        if n1==0 and n2==1:
            importdb.another()
            self.impGetValue()
        self.imppathsave = self.pathimp
        #self.messageBoxYES("This action will overwrite the existing file in the directory.\nDo you want to continue?"," Confirmation")
        dlg = wx.MessageDialog(self, "This action will overwrite the existing file in the directory.\nDo you want to continue?"," Confirmation",
                               #wx.OK | wx.ICON_INFORMATION
                               wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION
                               )
        if dlg.ShowModal() == wx.ID_YES:
            importdb.save(self.imppathsave)
        dlg.Destroy()

    def ImpSetCriteria(self):
        global colList

        self.impcb = wx.CheckBox(self.panelB, -1, label = "Age Limit", pos = (40, 130))
        self.min0 = masked.Ctrl(self.panelB, pos = (240, 125), size = (500,-1), controlType=masked.controlTypes.NUMBER)
        self.min0.Enable(False)
        self.impdpc = wx.GenericDatePickerCtrl(self.panelB, size=(120,-1), pos = (420,125), style = wx.TAB_TRAVERSAL | wx.DP_DROPDOWN | wx.DP_SHOWCENTURY | wx.DP_ALLOWNONE )
        self.impdpc.Enable(False)
        self.impcb.Disable()
        #self.Bind(wx.EVT_DATE_CHANGED, self.ImpOnDateChanged, self.impdpc)

        self.impcb1 = wx.CheckBox(self.panelB, -1, label = "Aggregate (College)", pos = (40, 170) )
        self.min1 = masked.Ctrl(self.panelB, fractionWidth=2, pos =(240, 165), size = (50,-1), controlType=masked.controlTypes.NUMBER )
        self.min1.Enable(False)
        #self.toLabel = wx.StaticText(self.panelB, -1, "To", pos=(380, 170)).SetFont(fontim)
        self.max1 = masked.Ctrl(self.panelB, fractionWidth=2, pos =(420, 165), size = (50,-1), controlType=masked.controlTypes.NUMBER )
        self.max1.Enable(False)
        self.impcb1.Disable()

        self.impcb2 = wx.CheckBox(self.panelB, -1,label = "10th %", pos = (40, 210) )
        self.min2 = masked.Ctrl(self.panelB, fractionWidth=2, pos =(240, 205), controlType=masked.controlTypes.NUMBER )
        self.min2.Enable(False)
        #self.toLabel = wx.StaticText(self.panelB, -1, "To", pos=(380, 210)).SetFont(fontim)
        self.max2 = masked.Ctrl(self.panelB, fractionWidth=2, pos =(420, 205), controlType=masked.controlTypes.NUMBER )
        self.max2.Enable(False)
        self.impcb2.Disable()

        self.impcb3 = wx.CheckBox(self.panelB, -1,label = "12th %", pos = (40, 250) )
        self.min3 = masked.Ctrl(self.panelB, fractionWidth=2, pos =(240, 245), controlType=masked.controlTypes.NUMBER )
        self.min3.Enable(False)
        #self.toLabel = wx.StaticText(self.panelB, -1, "To", pos=(380, 250)).SetFont(fontim)
        self.max3 = masked.Ctrl(self.panelB, fractionWidth=2, pos =(420, 245), controlType=masked.controlTypes.NUMBER )
        self.max3.Enable(False)
        self.impcb3.Disable()

        self.impcb4 = wx.CheckBox(self.panelB, -1,label = "Top Rankers upto", pos = (40, 290) )
        self.min4 = masked.Ctrl(self.panelB, pos =(240, 285), controlType=masked.controlTypes.NUMBER )
        self.min4.Enable(False)
        #self.toLabel = wx.StaticText(self.panelB, -1, "To", pos=(380, 290)).SetFont(fontim)
        #self.max4 = masked.Ctrl(self.panelB, fractionWidth=2, pos =(420, 285), controlType=masked.controlTypes.NUMBER )
        #self.max4.Enable(False)
        self.impcb4.Disable()

        self.Bind(wx.EVT_CHECKBOX, self.ImpOnDateCheckBox, self.impcb)
        self.Bind(wx.EVT_CHECKBOX, self.ImpOnCheckBox1, self.impcb1)
        self.Bind(wx.EVT_CHECKBOX, self.ImpOnCheckBox2, self.impcb2)
        self.Bind(wx.EVT_CHECKBOX, self.ImpOnCheckBox3, self.impcb3)
        self.Bind(wx.EVT_CHECKBOX, self.ImpOnCheckBox4, self.impcb4)


        if 'DOB' in colList:
            self.impcb.Enable()
        if 'TOTAL' in colList:
            self.impcb1.Enable()
            self.impcb4.Enable()
        if '10th' in colList:
            self.impcb2.Enable()
        if '12th' in colList:
            self.impcb3.Enable()

    def ImpOnDateCheckBox(self, event):
        self.min0.Enable(self.impcb.GetValue())
        self.impdpc.Enable(self.impcb.GetValue())

    def ImpOnCheckBox1(self, event):
        self.min1.Enable(self.impcb1.GetValue())
        self.max1.Enable(self.impcb1.GetValue())

    def ImpOnCheckBox2(self, event):
        self.min2.Enable(self.impcb2.GetValue())
        self.max2.Enable(self.impcb2.GetValue())

    def ImpOnCheckBox3(self, event):
        self.min3.Enable(self.impcb3.GetValue())
        self.max3.Enable(self.impcb3.GetValue())

    def ImpOnCheckBox4(self, event):
        self.min4.Enable(self.impcb4.GetValue())
        #self.max4.Enable(self.impcb4.GetValue())

    def impGetValue(self):
        if self.impcb.GetValue() == True:
            p = str(self.impdpc.GetValue())
            d = p[3:5]
            m = p[:2]
            y = "20"+p[6:8]
            p = d + "-" + m + "-" + y
            print p
            importdb.dobRange(self.min0.GetValue(),p)

        if self.impcb1.GetValue() == True:
            importdb.totalRange(self.min1.GetValue(),self.max1.GetValue())

        if self.impcb2.GetValue() == True:
            importdb.tenth(self.min2.GetValue(),self.max2.GetValue())

        if self.impcb3.GetValue() == True:
            importdb.intermediate(self.min3.GetValue(),self.max3.GetValue())

        if self.impcb4.GetValue() == True:
            importdb.toppers(self.min4.GetValue())


#=======================================================Functions of Merge==================================================================



    def fbbCallback1(self, evt):
        global pathm1, pathm2
        pathm1 = evt.GetString()
        print pathm1
        if pathm2 != '':
            self.mergeb.Enable(True)


    def fbbCallback2(self, evt):
        global pathm2, pathm1
        pathm2 = evt.GetString()
        print pathm2
        if pathm1 != '':
            self.mergeb.Enable(True)

    def MergeEvt(self, evt):
        global pathm1, pathm2
        dlg = wx.FileDialog(
              self, message="Save file as ...", defaultDir=os.getcwd(),
              defaultFile="", wildcard=wildcard, style=wx.SAVE )
        dlg.SetFilterIndex(4)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print path
            merge.execute(pathm1, pathm2, path)
        dlg.Destroy()






#=======================================================Functions of The Main App Panel==================================================================


    def aboutevt(self, event):
        info = wx.AboutDialogInfo()
        info.Name = "KNIT TPO Application"
        info.Version = "alpha"
        info.Copyright = "(C) The Shadow Inc.\n"
        info.Description = wordwrap(
            "This application has been specifically designed to ease out the tasks    related to"
            "Training and Placement Cell, KNIT Sultanpur.\n\n"
            "Created and Owned by the Shadow Inc.",
            400,wx.ClientDC(self))

        info.Developers = ["Atul Chaturvedi and Ayush Aman."]
        wx.AboutBox(info)

    def onAppTutb(self,evt):
        from tutwindow import TutorialWindow1
        app1 = wx.App()
        frame1 = TutorialWindow1(parent = None, id=-1)
        frame1.Show()
        app1.MainLoop()


    def OnClose(self, event):
        self.Destroy()
        sys.exit()

#=======================================================Functions of The Broadcast Message Panel==================================================================



#<<********************************************************End of Function Calling***************************************************************>>




if __name__ == '__main__':
    app = wx.App()
    frame = MainWindow1(parent = None, id=-1)
    frame.Show()
    app.MainLoop()
