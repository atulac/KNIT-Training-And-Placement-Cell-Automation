An python based application designed to automate tasks related to Training and Placement Cell, KNIT Sultanpur. 

The application has got different panels based on its functionalities.</br>It deals in:</br></br>
      1. Fetching data of students from website <a href = "http://knit.ac.in/">knit.ac.in </a></br> 
      2. Organizing and Presenting them (The Extract Sheets Panel) </br>
      3. Filtering them as per company's criteria (The Import Sheets Panel)</br>
      4. Automating emailing and message sending to students regarding any formal announcements from Career Development Cell (The Message Broadcasting Panel) </br>     

The application on the whole helps in analyzing and filtering the data of students who qualify the criteria of the companies visiting the campus in a few clicks. </br> 


<h2>The Extract Sheets Panel</h2>
The database fetched is so organized that it covers every minute detail of the student(s) being analyzed. It covers:</br></br>
      1. Semester-wise marks of the students </br>
      2. Status of the students (Passed, Failed, Backlogged) </br>
      3. Carry over marks of each semester (if applicable) </br>
      4. Pending backlogs.</br>
      5. Unfair means flag (to keep a check on the conduct) 
      </br></br>
      
Besides, the database presentation section has been divided into a few different tabs to get needed insight into it and not more.
Users need to select the required details and can save the extracted data to any desired location
by browsing with ‘Extract and Save As’ button.The tab division are as follows:</br></br>
      1. Precise Sheet (shows only semester-wise-carry-over-results updated marks)</br>
      2. Carry Overs Sheet (shows only carry-over details of the student(s))</br>
      3. Detailed Sheet (detailed including semester marks, carry-overs, pending backlogs and status all at once)</br>
      4. Branch Changers (the students list who switch branches after first year)</br>
      5. UFM (the students who are found doing any misconduct in examination)</br>
      
<h2>The Import Sheet Panel</h2>
The criterion as per which the database can be filtered are : </br></br>
      1. Percentage Range</br>
      2. Year Gaps</br>
      3. Date Of Birth</br>
      4. Number of Backlogs allowed</br></br>
     
One needs to browse in a sheet and explicitly set one or more criteria to be applied onto the sheet.
Clicking ‘Save’ button saves changes to the same sheet while clicking on the ‘Save As’ button
creates a new file at the desired location.
      
<h2>The Merge Sheets Panel</h2>
The Panel has been specifically designed for merging sheets.
The sheets can only be merged if the two sheets to be merged contain ROLL as the common column.
<h2>The Broadcast Message Panel</h2>
<b>Mail Broadcasting:</b> This feature of the application is specific to sending mail to one or a group of
email id. The mail can only be send by/to the Gmail users.
The list of receiver’s email address needs to be a .txt file with successive email
id on each new line.
This file can be selected from ‘Browse file of the recipients’ button in the panel.</br></br>
<b>SMS Broadcasting:</b> This feature of the application is for sending short messages to a list of mobile
numbers.
 
<h2>Modules Used </h2>

<b>Data Extraction</b>: urllib2, bs4/beautifulSoup
<b>GUI Development</b>: wx
<b>Database</b>: MySQLdb
<b>Working with Excel</b>:xlrd,xlwt,pandas,numpy,prettyTable
<b>Email and SMS</b>: email,smtplib,socket,cookielib,getpass,datetime
<b>General Modules</b>: os,sys,collections
