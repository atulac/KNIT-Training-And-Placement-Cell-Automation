import wx
import wx.richtext as rt

class  TutorialWindow1(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.SetSize((800,730))
        self.CenterOnScreen()
        self.SetMinSize((800,730))
        self.SetMaxSize((800,730))

        self.CreateStatusBar()
        self.SetStatusText("In-App-Tutorial")

        self.rtc = rt.RichTextCtrl(self, style=wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER);
        wx.CallAfter(self.rtc.SetFocus)

        self.rtc.Freeze()
        self.rtc.BeginSuppressUndo()

        self.rtc.BeginParagraphSpacing(0, 20)
        self.rtc.BeginLeftIndent(50)

        self.rtc.BeginAlignment(wx.TEXT_ALIGNMENT_CENTRE)
        self.rtc.BeginBold()
        self.rtc.BeginFontSize(15)
        self.rtc.BeginUnderline()
        self.rtc.WriteText("The Extract Sheets Panel:")
        self.rtc.EndUnderline()
        self.rtc.EndFontSize()
        self.rtc.Newline()
        self.rtc.EndBold()
        self.rtc.Newline()
        self.rtc.EndAlignment()

        self.rtc.BeginFontSize(10)
        self.rtc.WriteText("The tab buttons in the panel highlight the content of the sheets they contain.")
        self.rtc.Newline()
        self.rtc.WriteText("Users need to select the required details and can save the extracted data to any "
                            " desired location by browsing with 'Extract and Save As' button.")
        self.rtc.Newline()
        self.rtc.WriteText("The contents contained in respective tabs are as follows:")
        self.rtc.Newline()
        self.rtc.BeginBold()
        self.rtc.WriteText("Tab1: Precise Sheet:  ")
        self.rtc.EndBold()
        self.rtc.WriteText("The sheet contains semester-wise-carry over-results-updated marks of the students.")

        self.rtc.Newline()
        self.rtc.BeginBold()
        self.rtc.WriteText("Tab2: Carry Overs Sheet:  ")
        self.rtc.EndBold()
        self.rtc.WriteText("The sheet contains the details of Carry Overs (if any) of the students.")

        self.rtc.Newline()
        self.rtc.BeginBold()
        self.rtc.WriteText("Tab3: Detailed Sheet:  ")
        self.rtc.EndBold()
        self.rtc.WriteText("The sheet presents detailed analysis of students' performance viz., marks, carry over and its clearance.")

        self.rtc.Newline()
        self.rtc.BeginBold()
        self.rtc.WriteText("Tab4: Branch Changers:  ")
        self.rtc.EndBold()
        self.rtc.WriteText("The sheet lists out the details of students who got their branch changed in the second year.")

        self.rtc.Newline()
        self.rtc.BeginBold()
        self.rtc.WriteText("Tab5: UFM:  ")
        self.rtc.EndBold()
        self.rtc.WriteText(": The sheet contains the roll number of the students who were found accused of any kind of 'Unfair Means'.")
        self.rtc.EndFontSize()

        self.rtc.Newline()
        self.rtc.Newline()
        self.rtc.Newline()
        self.rtc.BeginAlignment(wx.TEXT_ALIGNMENT_CENTRE)
        self.rtc.BeginBold()
        self.rtc.BeginFontSize(15)
        self.rtc.BeginUnderline()
        self.rtc.WriteText("The Import Sheets Panel:")
        self.rtc.EndUnderline()
        self.rtc.EndFontSize()
        self.rtc.Newline()
        self.rtc.EndBold()
        self.rtc.Newline()
        self.rtc.EndAlignment()

        self.rtc.BeginFontSize(10)
        self.rtc.WriteText("The panel deals with data manipulations over any  sheet.")
        self.rtc.Newline()
        self.rtc.WriteText("One needs to browse in a sheet and explicitly set one or more criteria to be applied onto the sheet.")
        self.rtc.Newline()
        self.rtc.WriteText("Clicking 'Save' button saves changes to the same sheet while clicking on the 'Save As' button "
                           "creates a new file at the desired location.")
        self.rtc.Newline()
        self.rtc.EndFontSize()

        self.rtc.Newline()
        self.rtc.Newline()
        self.rtc.Newline()
        self.rtc.BeginAlignment(wx.TEXT_ALIGNMENT_CENTRE)
        self.rtc.BeginBold()
        self.rtc.BeginFontSize(15)
        self.rtc.BeginUnderline()
        self.rtc.WriteText("The Merge Sheets Panel:")
        self.rtc.EndUnderline()
        self.rtc.EndFontSize()
        self.rtc.Newline()
        self.rtc.EndBold()
        self.rtc.Newline()
        self.rtc.EndAlignment()

        self.rtc.BeginFontSize(10)
        self.rtc.WriteText("The Panel has been specifically designed for merging sheets.")
        self.rtc.Newline()
        self.rtc.WriteText("The sheets can only be merged if the two sheets to be merged contain ROLL as the common column.")
        self.rtc.Newline()
        self.rtc.EndFontSize()

        self.rtc.Newline()
        self.rtc.Newline()
        self.rtc.Newline()
        self.rtc.BeginAlignment(wx.TEXT_ALIGNMENT_CENTRE)
        self.rtc.BeginBold()
        self.rtc.BeginFontSize(15)
        self.rtc.BeginUnderline()
        self.rtc.WriteText("The Broadcast Message Panel:")
        self.rtc.EndUnderline()
        self.rtc.EndFontSize()
        self.rtc.Newline()
        self.rtc.EndBold()
        self.rtc.Newline()
        self.rtc.EndAlignment()

        self.rtc.BeginFontSize(10)
        self.rtc.Newline()
        self.rtc.BeginBold()
        self.rtc.WriteText("Mail Broadcasting:  ")
        self.rtc.EndBold()
        self.rtc.WriteText("This feature of the application is specific to sending mail to one or a group of"
                           " email id. The mail can only be send by/to the Gmail users.")
        self.rtc.Newline()
        self.rtc.WriteText("The list of receiver's email address needs to be a .txt file with successive email"
                           " id on each new line")
        self.rtc.Newline()
        self.rtc.WriteText("This file can be selected from 'Browse file of the recipients' button in the panel.")

        self.rtc.Newline()
        self.rtc.BeginBold()
        self.rtc.WriteText("SMS Broadcasting:  ")
        self.rtc.EndBold()
        self.rtc.WriteText("This feature of the application is for sending short messages to a list of mobile"
                           " numbers.")
        self.rtc.Newline()
        self.rtc.WriteText("The list of receiver's mobile numbers needs to be a .txt file with successive phone "
                           "numbers on each new line.")
        self.rtc.Newline()
        self.rtc.WriteText("This file can be selected from 'Browse file of the recipients' button in the panel.")
        self.rtc.EndFontSize()
        self.rtc.Newline()


        # Create and initialize text attributes
        self.textAttr = rt.RichTextAttr()
        self.SetFontStyle(fontColor=wx.Colour(0, 0, 0), fontBgColor=wx.Colour(255, 255, 255), fontFace='Times New Roman', fontSize=10, fontBold=False, fontItalic=False, fontUnderline=False)
        self.SetFontStyle(fontBold=True)
        self.SetFontStyle(fontItalic=True)
        self.SetFontStyle(fontBold=False)
        self.SetFontStyle(fontItalic=False)
        self.rtc.Newline()

        self.SetFontStyle(fontBold=True)
        self.SetFontStyle(fontUnderline=True)
        self.SetFontStyle(fontBold=False)
        self.SetFontStyle(fontUnderline=False)
        self.rtc.Newline()
        self.rtc.EndParagraphSpacing()

        self.rtc.EndSuppressUndo()
        self.rtc.Thaw()

        self.rtc.SetEditable(False)
        #self.rtc.EnableScrolling(False,True)

    def SetFontStyle(self, fontColor = None, fontBgColor = None, fontFace = None, fontSize = None,
                     fontBold = None, fontItalic = None, fontUnderline = None):
      if fontColor:
         self.textAttr.SetTextColour(fontColor)
      if fontBgColor:
         self.textAttr.SetBackgroundColour(fontBgColor)
      if fontFace:
         self.textAttr.SetFontFaceName(fontFace)
      if fontSize:
         self.textAttr.SetFontSize(fontSize)
      if fontBold != None:
         if fontBold:
            self.textAttr.SetFontWeight(wx.FONTWEIGHT_BOLD)
         else:
            self.textAttr.SetFontWeight(wx.FONTWEIGHT_NORMAL)
      if fontItalic != None:
         if fontItalic:
            self.textAttr.SetFontStyle(wx.FONTSTYLE_ITALIC)
         else:
            self.textAttr.SetFontStyle(wx.FONTSTYLE_NORMAL)
      if fontUnderline != None:
         if fontUnderline:
            self.textAttr.SetFontUnderlined(True)
         else:
            self.textAttr.SetFontUnderlined(False)
      self.rtc.SetDefaultStyle(self.textAttr)



