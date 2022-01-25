#The block of code below imports the libraries needed to help make the code work
#The tkinter library is needed to create the user interface for the user to interact with 
import tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
#The math library is needed to do some of the equations for the statistical tests
import math
#The OS library is needed to print the solution for the statistical test that had been carried out
import os
#The numpy and matplotlib libraries are needed to create the graphs
import matplotlib.pyplot as plt
import numpy as np

#This class contains all the functions to be used
class Statistics:
   ###This function below is a constructor that creates an instance of the Statistics class
   def __init__(self, *args, **kw):
      super(Statistics, self).__init__(*args, **kw)
      self.mainWindow()

   ###This function is used to create the first main window that the user sees and can interact with 
   def mainWindow(self):
      #'main' is a window created from the root that has been set up
      #we can destroy the main window without the program crashing
      #global makes this varaible known everywhere and not just in this function
      global main
      main = Toplevel(root)
      main.focus_force()
      #This line below sets the background colour of the window
      main.configure(background = "thistle1")
      #This line below sets the size of the window
      main.geometry("300x300+200+200")

      #These two lines set a variable that will help with changing which window is displayed when a button is clicked
      #This can be done using the goDo function
      global v
      v = IntVar()

      #These are all widgets that can be displayed on the window
      #This below is a Label that is acting like a heading
      mainLabel = tkinter.Label(main, text = "Statistical Analysis", background = "thistle1")

      #These Radiobuttons below give the user a choice as to which ststistical test they want to carry out
      csRadioButton = Radiobutton(main, text = "Chi-Squared", variable = v, value = 1, bg = "thistle1")
      srRadioButton = Radiobutton(main, text = "Spearmans Rank", variable = v, value = 2, bg = "thistle1")
      ttRadioButton = Radiobutton(main, text = "T-test", variable = v, value = 3, bg = "thistle1")
      liRadioButton = Radiobutton(main, text = "Lincoln Index", variable = v, value = 4, bg = "thistle1")

      #These two lines of code are buttons 
      #The user can quit the program or they can continue with the statistical test they want to do      
      goButton = tkinter.Button(main, text = "go", command = self.goDo)
      quitButton = tkinter.Button(main, text = "quit", command = root.destroy)

      #This next block of code places the widgets on the window by using pack()
      #These are all packed in the order to be placed on the window
      mainLabel.pack()
      csRadioButton.pack()
      srRadioButton.pack()
      ttRadioButton.pack()
      liRadioButton.pack()        
      goButton.pack()
      quitButton.pack()

   ###This function is used to navigate through the 4 statistic test windows
   def goDo(self):
      if v.get() == 1:
         #Go to chiSquaredWindow 
         self.chiSquaredWindow()
      if v.get() == 2:
         #Go to spearmansRankWindow 
         self.spearmansRankWindow()
      if v.get() == 3:
         #Go to tTestWindow 
         self.tTestWindow()
      if v.get() == 4:
         #Go to lincolnIndexWindow 
         self.lincolnIndexWindow()

   ###The chi-squared statistic test main window   
   def chiSquaredWindow(self):
      #The line below destroys the main window 
      main.destroy()
      global cswindow
      global cscategoriesEntry

      #These four lines of code set up the chiSquaredWindow with all its features
      cswindow = Toplevel(root)
      cswindow.focus_force()
      cswindow.configure(background = "thistle1")
      cswindow.geometry("600x500+100+100")

      #These two lines below add vertical scrollbar to the window
      scrollbar = Scrollbar(cswindow)
      scrollbar.pack(side=RIGHT, fill=Y)

      csLabel = tkinter.Label(cswindow, text = "CHI-SQUARED", background = "thistle1")
      cscategoriesLabel = tkinter.Label(cswindow, text = "How many categories of data were collected? (number of independent variables)", bg = "thistle1")
      #This line below is an entry box which is another widget, this is so the user can enter in data
      cscategoriesEntry = tkinter.Entry(cswindow)
      cscategoryButton = tkinter.Button(cswindow, text = "Enter", command = self.cscategories)
      backButton1 = tkinter.Button(cswindow, text = "back to main", command = self.toMainFromcswindow)
        
      csLabel.pack()
      cscategoriesLabel.pack()
      cscategoriesEntry.pack()
      cscategoryButton.pack()
      backButton1.pack(side = BOTTOM)
        
   ###This method is used to work out the number of categories of data
   ###It is for the user to enter in all the information required
   def cscategories(self):
      global category
      global csindependentvarEntry
      global csdependentvarEntry
      global csSiteEntry
      global indVarList
      global siteValList

      #exception handling of the number of categories
      #It tries and gets the correct data type which is an integer from the user
      access = False
      try:
         cate = cscategoriesEntry.get()
         category = int(cate)
      #If the correct data type isn't entered it comes up with an error box for the user to see what the error is
      except:
         messagebox.showinfo("ERROR", "You haven't entered an integer (whole number)")

      #These two variables below are used to store the data entered in by the user
      indVarList = []
      siteValList = []
      
      no = 1
      #This is a for loop that repeates the entry boxes for the the independet variables depending on the number of categories
      for x in range (0,category):
         csindependentvarLabel = tkinter.Label(cswindow, text = "What was independent variable " + str(no) + " in the investigation?", bg = "thistle1")
         csindependentvarEntry = tkinter.Entry(cswindow,width = 30)
         #The independent variable name(s) that was entered is(are) added to the indVarList list
         indVarList.append(csindependentvarEntry)
            
         csSiteLabel = tkinter.Label(cswindow, text = "The number found at this site?", background = "thistle1")
         csSiteEntry = tkinter.Entry(cswindow)
         #The value for each site entered is added to the siteValList list
         siteValList.append(csSiteEntry)   

         no = no + 1
         csindependentvarLabel.pack()
         csindependentvarEntry.pack()
         csSiteLabel.pack()
         csSiteEntry.pack()
        
      csdependentvarLabel = tkinter.Label(cswindow, text = "What was the dependent variable in the investigation?", bg = "thistle1")
      csdependentvarEntry = tkinter.Entry(cswindow,width = 30)
      entryButton = tkinter.Button(cswindow, text = "Calculate", command = self.chisquared)

      csdependentvarLabel.pack()
      csdependentvarEntry.pack()
      entryButton.pack()
        
   ###This function is where the chi-squared test is worked out            
   def chisquared(self):
      global sumSiteVal
      global values
      global mean
      global C
      global A
      global sumofCList
      global X
      global csdnull
      global theIndependentVars
      global csans
      global csdof

      #exception handling of the dependent variable
      #It tries and gets the correct data type which is a string from the user
      try:
         csd = csdependentvarEntry.get()
         csdnull = str(csd)
      #If the correct data type isn't enetered it gives the user an error
      except:
         messagebox.showinfo("ERROR", "You haven't entered the correct data type (need to enter text)")
         
      independent = []
      for csindependentvarEntry in indVarList:
         #Checks if a value is definitely entered into the entry box and if not an error is shown
         if csindependentvarEntry == "":
            messagebox.showinfo("ERROR", "You havent entered any text")
         #exception handling independent variable
         #It tries and gets a string from the user
         try:
            csi = csindependentvarEntry.get()
            indep = str(csi)
         #If a string isn't entered, it sends an error to the user
         except:
            messagebox.showinfo("ERROR", "You haven't entered the correct data type (need to enter text)")
         independent.append(indep)

      #this helps improve the layout of the code when it is needed
      theIndependentVars = (" and ".join(map(str, independent)))

      values = []
      for csSiteEntry in siteValList:
         #exception handling site values
         #An integer needs to be entered by the user otherwise an error come up
         try:
            v = csSiteEntry.get()
            val = int(v)
         except:
            messagebox.showinfo("ERROR", "You haven't entered an integer (a whole number)")
         values.append(int(val))

      #The line below gets the sum of the values entered so the mean can be worked out 
      sumSiteVal = sum(values)

      #The next two lines gets the mean observed data
      mean = (sumSiteVal)/category
      mean = round(mean,4)

      #This next block of code does the (observed-mean)^2/mean at each site
      C = []
      for n in range(0, category):
         A = ((values[n]-mean)*(values[n]-mean))/mean
         A = round(A,4)
         C.append(A)

      #This line now gets the sum of the values in both sites
      sumofCList = sum(C)

      #chi-squared value rounded to 3 decimal places and then converted into a string
      #This is so it can be used in the method window that the user can see
      X = str(round(sumofCList,3))
         
      #This works out the degree of freedom which is needed for accepting or rejecting the null hypothesis
      csdof = category-1

      #This gets the critical value of the test being done at a probability of 0.05 (P=0.05)
      cscriticalValList = [3.84,5.99,7.82]
      for n in range(0,len(cscriticalValList)):
         cscriticalVal = cscriticalValList[csdof-1]

      #This block of code works out if the the hypothesis significant or not
      if float(X) >= float(cscriticalVal):
         csans = "The chi-squared value of " + str(X) + " is greater than the critical value of " + str(cscriticalVal)+ "\n so we reject the null hypothesis at a 5% significance level, \n as there is only a 5% probability that the result is due to chance"
      else:
         csans = "The chi-squared value of " + str(X) + " is less than the critical value of " + str(cscriticalVal) + "\n so we accept the null hypothesis at a 5% significance level, \n as there is a 95% probability that results are due to chance"

      #The final result is then shown on screen
      chisquaredLabel = tkinter.Label(cswindow, text = "The chi-squared value is: " + X, background = "thistle1")
      #The null hypothesis is also shown on screen
      csnullHypothesisLabel = tkinter.Label(cswindow, text = "The null hypothesis is:", background = "thistle1")
      csnullHypothesisDataLabel = tkinter.Label(cswindow, text = "There is no significant difference in " + str(csdnull) + " in " + str(theIndependentVars), bg = "thistle1")
      cscriticalValCompLabel = tkinter.Label(cswindow, text = csans, bg = "thistle1")
      #The worked solution can then be seen when a button is clicked
      methodButton = tkinter.Button(cswindow, text = "Click here to see the worked solution", command = self.csMethodWindow)
      #The graph of this test can then be seen when a button is clicked
      graphButton = tkinter.Button(cswindow, text = "Click to see the graph", command = self.csGraph)

      chisquaredLabel.pack()
      csnullHypothesisLabel.pack()
      csnullHypothesisDataLabel.pack()
      cscriticalValCompLabel.pack()
      methodButton.pack()
      graphButton.pack()

   ###This function shows the working out of the chi-squared test with each step shown    
   def csMethodWindow(self):
      #This line destroys the cswindow that was created 
      cswindow.destroy()
      global csmethwindow

      #This sets up the new window with the new features
      csmethwindow = Toplevel(root)
      csmethwindow.focus_force()
      csmethwindow.configure(background = "thistle1")
      csmethwindow.geometry("600x400+100+100")

      #Here the method for working out this statistic is worked out
      methodLabel = tkinter.Label(csmethwindow, text = "The worked solution", bg = "thistle1")
      #total found at the sites
      totalSiteLabel = tkinter.Label(csmethwindow, text = "The total found at each site is below in the list:",bg = "thistle1") 
      totalSiteDataLabel = tkinter.Label(csmethwindow, text = str(values), bg = "thistle1")
      #total found all together
      totalSecondLabel = tkinter.Label(csmethwindow, text = "Add the values above in the list to get the combined total:",bg = "thistle1")
      totalSecondDataLabel = tkinter.Label(csmethwindow, text = str(sumSiteVal),bg = "thistle1")
      #mean expected
      meanLabel = tkinter.Label(csmethwindow, text = "Calculate the mean by doing this (" + str(sumSiteVal) + ")/" + str(category),bg = "thistle1") 
      meanDataLabel = tkinter.Label(csmethwindow, text = str(mean), bg= "thistle1")
      #now need an inbetween step to get the final answer
      #for each site we need the (observed - expected)^2/mean
      siteLabel = tkinter.Label(csmethwindow, text = "For each site we need to work out the (observed - mean)^2/mean",bg = "thistle1")

      methodLabel.pack()
      totalSiteLabel.pack()
      totalSiteDataLabel.pack()
      totalSecondLabel.pack()
      totalSecondDataLabel.pack()
      meanLabel.pack()
      meanDataLabel.pack()
      siteLabel.pack()
      
      #This for loop shows the actual values needed
      for n in range(0, category):
         sitesLabel = tkinter.Label(csmethwindow, text = "(" + str(values[n]) + "-" + str(mean) + ")^/" + str(mean) + ":",bg = "thistle1")
         siteDataLabel = tkinter.Label(csmethwindow, text = str(C[n]),bg = "thistle1")
         sitesLabel.pack()
         siteDataLabel.pack()        

      chiSquaredValLabel = tkinter.Label(csmethwindow, text = "The values calculated above for each site are added together to give the final answer:",bg = "thistle1")
      chiSquaredValDataLabel = tkinter.Label(csmethwindow, text = str(X),bg = "thistle1")
      #This button is used to print out a hard copy of the method
      printButton = tkinter.Button(csmethwindow, text = "Print the method", command = self.csprint)
      backButton = tkinter.Button(csmethwindow, text = "back to main", command = self.toMainfromcsmethwindow)     

      chiSquaredValLabel.pack()
      chiSquaredValDataLabel.pack()
      printButton.pack()
      backButton.pack(side = BOTTOM)

   ###This function is used to draw a graph of the chi-squared test using the data provided
   def csGraph(self):
      #95% conidence level or P=0.05
      cscriticalValList = [3.84,5.99,7.82]
      xPoints = [1,2,3]

      #plot the X value 
      plt.scatter(csdof, float(X))
      plt.axis([0.9,xPoints[-1],0.0,float(X)+1])

      #plot the 95% confidence level
      plt.plot(xPoints,cscriticalValList)

      #give the graph some axis titles
      plt.xlabel("Degree of Freedom")
      plt.ylabel("Chi-Sqauared")
      plt.title("The Chi-Squared value and degree of freedom at P=0.05")
      plt.show()

   ###This gives the Spearmans Rank window a scrollbar
   def srScrollfunction(self,event):
      #the colour here makes the whole bg coloured
      srcanvas.configure(scrollregion=srcanvas.bbox("all"),width=430,height=470, bg = "thistle1")

   ###This is the spearmans rank main window
   def spearmansRankWindow(self):
      #The main window is destroyed
      main.destroy()
      global srwindow
      global srindependentvarEntry
      global srdependentvarEntry
      global xtotalEntry
      global xvalEntry
      global backButton2
      global srcanvas
      global srframe

      #Here are all the features of the window  
      srwindow = Toplevel(root)
      srwindow.focus_force()
      srwindow.configure(background = "thistle1")
      srwindow.geometry("475x500+100+100")

      #This frame is created so the scrollbar can be added to it further down
      frame = Frame(srwindow, relief=GROOVE, width = 100, height = 100)
      frame.place(x=10, y=10)

      srcanvas = Canvas(frame)
      #the background here changes the colour of the frame 
      srframe = Frame(srcanvas, bg = "thistle1")
      scrollbar = tkinter.Scrollbar(frame, orient="vertical", command = srcanvas.yview)
      srcanvas.configure(yscrollcommand=scrollbar.set)

      #Here the scrollbar is added to the frame
      scrollbar.pack(side="right", fill="y")
      srcanvas.pack(side="left")

      srcanvas.create_window((0,0),window=srframe,anchor='nw')
      srframe.bind("<Configure>",self.srScrollfunction)

      #The next lines of code add the widgets to the window
      srLabel = tkinter.Label(srframe, text = "SPEARMANS RANK", background = "thistle1")
      srindependentvarLabel = tkinter.Label(srframe, text = "What was the independent variable in the investigation?", bg = "thistle1")
      srindependentvarEntry = tkinter.Entry(srframe,width = 30)
      srdependentvarLabel = tkinter.Label(srframe, text = "What was the dependent variable in the investigation?", bg = "thistle1")
      srdependentvarEntry = tkinter.Entry(srframe,width = 30)    
      xtotalLabel = tkinter.Label(srframe, text = "How many values for the dependent and independent variables?", background = "thistle1")
      xtotalEntry = tkinter.Entry(srframe)
      xtotalGoButton = tkinter.Button(srframe, text = "Enter", command = self.xvarentries)
      backButton2 = tkinter.Button(srframe, text = "back to main", command = self.toMainFromsrwindow)

      #The widgets are then packed
      srLabel.pack()
      srindependentvarLabel.pack()
      srindependentvarEntry.pack()
      srdependentvarLabel.pack()
      srdependentvarEntry.pack()
      xtotalLabel.pack()
      xtotalEntry.pack()
      xtotalGoButton.pack()
      backButton2.pack(side = BOTTOM)

   ###This function gets the spearmans rank x variable values from the user 
   def xvarentries(self):
      global xvalEntry
      global xval
      global xcount
      global xtotal

      #exception handling total number of variables in both variables window
      #Tries to get an integer from the user, if not an error is shown
      try:
         xtot = xtotalEntry.get()
         xtotal = int(xtot)
      except:
         messagebox.showinfo("ERROR", "You haven't entered an integer (a whole number)")

      xvalLabel = tkinter.Label(srframe, text = "Give the independent variable values below", background = "thistle1")
      xvalLabel.pack()
      xcount = 0
      xval = []
      for xcount in range (0,xtotal):
         #This is where the user enters the independent variable values
         xvalEntry = tkinter.Entry(srframe)
         xval.append(xvalEntry)
         xvalEntry.pack()
      #Here the yvarentries() function is called   
      self.yvarentries() 

   ###This function gets the spearmans rank y variables from the user
   def yvarentries(self):
      global yvalEntry
      global yval

      yvalLabel = tkinter.Label(srframe, text = "Give the dependent variable values below", background = "thistle1")
      yvalLabel.pack()

      ycount = 0
      yval = []
      for ycount in range (0,xtotal):
         #This is where the user enters the dependent variable values
         yvalEntry = tkinter.Entry(srframe)
         yval.append(yvalEntry)
         yvalEntry.pack()

      calculateButton = tkinter.Button(srframe, text = "Calculate", command = self.spearmansrank)
      calculateButton.pack()

   ###This is the spearmans rank working out window   
   def spearmansrank(self,*args):
      global copyofx
      global copyofy
      global xfinalRank
      global yfinalRank
      global D
      global D2
      global SD2
      global n
      global r
      global srans
      global srinull
      global srdnull
      global nop

      #null hypothesis
      #exception handling independent and dependent variables
      try:
         #Tries to get strings from the user, if not an error would be shown 
         sri = srindependentvarEntry.get()
         srinull = str(sri)
         srd = srdependentvarEntry.get()
         srdnull = str(srd)
      except:
         messagebox.showinfo("ERROR", "You haven't entered the correct data type (need to enter text)")

      #get x entries into a list
      xvalues = []
      for xvalEntry in xval:
         #exception handling x entries
         #tries to get a float from the user, if not an error would be shown
         try:
            p = xvalEntry.get()
            a = float(p)
         except:
            messagebox.showinfo("ERROR", "You haven't entered a number (can be a decimal)")
         xvalues.append(a)

      #This for loop convert items in list to float
      for i in range (0, len(xvalues)):
         xvalues[i] = float(xvalues[i])

      #This block of code gets the y entries into a list
      yvalues = []
      for yvalEntry in yval:
         #exception handling y entries
         #It tries to get a float, if not an error would be shown
         try:
            q = yvalEntry.get()
            b = float(q)
         except:
            messagebox.showinfo("ERROR", "You haven't entered a number(can be a decimal)")
         yvalues.append(b)

      #This converts the items in a list to float
      for n in range (0, len(yvalues)):
         yvalues[n] = float(yvalues[n])

      #r is the spearmans rank variable
      r = 0

      #the ranking of x variable list
      #need to make a copy of list x to do this
      copyofx = xvalues.copy()
      #need a list to store the values visited
      xvisitedValues = []
      #need a list to store the positions
      xpositions = []

      # need to sort the list
      xsorted = xvalues.sort()
      #enumerate through the list
      for e, j in enumerate(xvalues):
         #if the value from the list isn't in the list xvisitedValues
         if j not in xvisitedValues:
            #assign the value in the list to the variable name value
            xvalue = j
            #num is the number of times the no is repeated in the list
            xnum = xvalues.count(j)
            #this resets the posadd so new values can be added to it
            xposadd = 0
            #now iterate again through the list
            xiterate = 0
            for xiterate in range(0, len(xvalues)):
               #if the value is the same as the value in the position checking
               if j == xvalues[xiterate]:               
                  xgetpos = xiterate
                  #add the position of the (value + 1) to list visitedValues
                  #cannot start at 0 so must add 1
                  xposadd = xposadd + (xgetpos + 1)
                  xvisitedValues.append(xvalues[xgetpos])               
                     
            for add in range(0, xnum):
               xpositions.append(xposadd/xnum)

      #need an empty list to store the positions in the correct order
      xfinalRank = []
      #make the list have 0's in each position of the length of copyofx list
      for item in copyofx:
         xfinalRank.append(0)
      #make another copy of list x
      xcopy2 = xvalues.copy()

      #want to go through each item in list copyofx
      for e, j in enumerate(copyofx):
         #find the item j in t
         # .index gets the first occurence of the j item we are looking for
         xpos = xcopy2.index(j)
         #find the position of the occurence in the positions list and store in finalRank
         xfinalRank[e] = xpositions[xpos]
         #need to add a zero to the item in that position in list xcopy2 so it doesnt get found again
         xcopy2[xpos] = 0

      #the ranking of y variable list
      #need to make a copy of list y to do this
      copyofy = yvalues.copy()
      #need a list to store the values visited
      yvisitedValues = []
      #need a list to store the positions
      ypositions = []

      # need to sort the list
      ysorted = yvalues.sort()
      #enumerate through the list
      for e, j in enumerate(yvalues):
         #if the value from the list isn't in the list visitedValues
         if j not in yvisitedValues:
            #assign the value in the list to the variable name value
            yvalue = j
            #num is the number of times the no is repeated in the list
            ynum = yvalues.count(j)
            #this resets the posadd so new values can be added to it
            yposadd = 0
            #now iterate again through the list
            yiterate = 0
            for yiterate in range(0, len(yvalues)):
               #if the value is the same as the value in the position checking
               if j == yvalues[yiterate]:               
                  ygetpos = yiterate
                  #add the position of the (value + 1) to list visitedValues
                  #cannot start at 0 so must add 1
                  yposadd = yposadd + (ygetpos + 1)
                  yvisitedValues.append(yvalues[ygetpos])               
                     
            for add in range(0, ynum):
               ypositions.append(yposadd/ynum)

      #need an empty list to store the positions in the correct order
      yfinalRank = []
      #make the list have 0's in each position of the length of c list
      for item in copyofy:
         yfinalRank.append(0)
      #make another copy of list a
      ycopy2 = yvalues.copy()

      #want to go through each item in list copyofy
      for e, j in enumerate(copyofy):
         #find the item j in t
         # .index gets the first occurence of the j item we are looking for
         ypos = ycopy2.index(j)
         #find the position of the occurence in the positions list and store in finalRank
         yfinalRank[e] = ypositions[ypos]
         #need to add a zero to the item in that position in list t so it doesnt get found again
         ycopy2[ypos] = 0

      #subracting values from two lists
      D = []
      #t value will help iterate through each item in the lists
      t = 0
      for t in range (0, len(xfinalRank)):
         d = xfinalRank[t] - yfinalRank[t]
         t = t + 1
         D.append(d)

      #now need to square all the values in the D list
      #add the squared values to the list D2
      D2 = []
      e = 0
      for e in range (0, len(D)):
         d2 = D[e]*D[e]
         e = e + 1
         D2.append(d2)

      #need to find the sum of the values in the D2 list and multiply it by 6
      SD2 = (sum(D2))*6

      #need to find (n^3)-n
      n = ((xtotal)*(xtotal)*(xtotal))-(xtotal)

      #finally use all these values to get the spearmans rank value
      r = 1 - (SD2/n)
      r = str(round(r,3))

      #number of pairs for the critical value
      nop = xtotal

      #check if the hypothesis is significant or not at a probability of 0.5 (P=0.05)
      #starts at a minimum of 5 pairs
      srcriticalValList = [1,0.886,0.786,0.738,0.700,0.648,0.618,0.587,0.560,0.538,0.521,0.505,0.485,0.472,0.460,0.447]
      for n in range(0,len(srcriticalValList)):
         srcriticalVal = srcriticalValList[nop-5]

      #This then works out if the null hypothesis is significant or not?
      if float(r) >= float(srcriticalVal):
         srans = "The spearmans rank value of " + str(r) + " is greater than the critical value of " + str(srcriticalVal)+ "\n We reject null hypothesis at a 5% significance level, \n as there is only a 5% probability that the results are due to chance"
      else:
         srans = "The spearmans rank value of " + str(r) + " is less than the critical value of " + str(srcriticalVal)+ "\n We accept the null hypothesis at a 5% significance level, \n as there is a 95% probability that the results are due to chance"

      #Here all the final information is displayed on the window
      spearmansRankLabel = tkinter.Label(srframe, text = "The spearmans rank value is: " + r , background = "thistle1")
      srnullHypothesisLabel = tkinter.Label(srframe, text = "The null hypothesis is:", background = "thistle1")
      srnullHypothesisDataLabel = tkinter.Label(srframe, text = "There is no significant correlation between " + str(srinull) + " and " + str(srdnull), bg = "thistle1")
      srcriticalValCompLabel = tkinter.Label(srframe, text = srans, bg = "thistle1")
      #Two buttons are being displayed, one shows the method, the other shows a graph
      methodButton = tkinter.Button(srframe, text ="Click here to see the full method", command = self.srMethodWindow)
      graphButton = tkinter.Button(srframe, text="Click to see graph", command = self.srGraph)

      spearmansRankLabel.pack()
      srnullHypothesisLabel.pack()
      srnullHypothesisDataLabel.pack()
      srcriticalValCompLabel.pack()  
      methodButton.pack()
      graphButton.pack()

   ###This function contains the method for working out the spearmans rank
   #each step is shown   
   def srMethodWindow(self):
      #Here the srwindow is destroyed as this new one is created
      srwindow.destroy()
      global srmethwindow
      #The features of the new window created are mentioned here
      srmethwindow = Toplevel(root)
      srmethwindow.focus_force()
      srmethwindow.configure(background = "thistle1")
      srmethwindow.geometry("700x500+100+100")

      methodLabel = tkinter.Label(srmethwindow, text = "The worked method", bg = "thistle1")
      #var 1 original list
      var1ListLabel = tkinter.Label(srmethwindow, text = "The first variable value list: " ,bg = "thistle1")
      var1ListDataLabel = tkinter.Label(srmethwindow, text = str(copyofx), bg = "thistle1")
      #var 1 ranked list
      var1RankLabel = tkinter.Label(srmethwindow, text = "The first variable value list ranked in ascending order: " ,bg = "thistle1")
      var1RankDataLabel = tkinter.Label(srmethwindow, text = str(xfinalRank),bg = "thistle1") 
      #var 2 original list
      var2ListLabel = tkinter.Label(srmethwindow, text = "The second variable value list: " ,bg = "thistle1")
      var2ListDataLabel = tkinter.Label(srmethwindow, text = str(copyofy), bg = "thistle1")
      #var 2 ranked list
      var2RankLabel = tkinter.Label(srmethwindow, text = "The second variable value list are ranked in ascending order: " ,bg = "thistle1")
      var2RankDataLabel = tkinter.Label(srmethwindow, text = str(yfinalRank), bg = "thistle1")
      #differences in rank
      rankDiffLabel = tkinter.Label(srmethwindow, text = "Find the difference between each item in the ranked lists: " , bg = "thistle1")
      rankDiffDataLabel = tkinter.Label(srmethwindow, text = str(D), bg = "thistle1")
      #square each ranked value
      squaredRankLabel = tkinter.Label(srmethwindow, text = "The above list items are now squared to give this: " , bg = "thistle1")
      squaredRankDataLabel = tkinter.Label(srmethwindow, text = str(D2), bg = "thistle1")
      #sum of the values
      sumRankValsLabel = tkinter.Label(srmethwindow, text = "The sum of the values given above are: " ,bg = "thistle1")
      sumRankValsDataLabel = tkinter.Label(srmethwindow, text = str(SD2/6), bg = "thistle1")
      #sum *6
      sum6Label = tkinter.Label(srmethwindow, text = "The above value is now multiplied by 6: " ,bg = "thistle1")
      sum6DataLabel = tkinter.Label(srmethwindow, text = str(SD2), bg = "thistle1")
      #(n^3)-1
      nvaluesLabel = tkinter.Label(srmethwindow, text = "(n^3)-n is now worked out (n is no of items): " ,bg = "thistle1")
      nvaluesDataLabel = tkinter.Label(srmethwindow, text = str(n), bg = "thistle1")
      #final equation
      srFinalAnsLabel = tkinter.Label(srmethwindow, text = " Do 1-(" + str(SD2) + "/" + str(n) +") to get the final answer of: " , bg = "thistle1")
      srFinalAnsDataLabel = tkinter.Label(srmethwindow, text = str(r), bg = "thistle1")

      #This button is used to print out a hard copy of the method
      printButton = tkinter.Button(srmethwindow, text = "Print the method", command = self.srprint)
      backButton = tkinter.Button(srmethwindow, text = "back to main", command = self.toMainFromsrmethwindow)

      methodLabel.pack()
      var1ListLabel.pack()
      var1ListDataLabel.pack()
      var1RankLabel.pack()
      var1RankDataLabel.pack()
      var2ListLabel.pack()
      var2ListDataLabel.pack()
      var2RankLabel.pack()
      var2RankDataLabel.pack()
      rankDiffLabel.pack()
      rankDiffDataLabel.pack()
      squaredRankLabel.pack()
      squaredRankDataLabel.pack()
      sumRankValsLabel.pack()
      sumRankValsDataLabel.pack()
      sum6Label.pack()
      sum6DataLabel.pack()
      nvaluesLabel.pack()
      nvaluesDataLabel.pack()
      srFinalAnsLabel.pack()
      srFinalAnsDataLabel.pack()

      printButton.pack()
      backButton.pack(side = BOTTOM)

   ###This function is to draw the spearmans rank graph
   def srGraph(self):
      #95% conidence level or P=0.05
      srcriticalValList = [1,0.886,0.786,0.738,0.700,0.648,0.618,0.587,0.560,0.538,0.521,0.505,0.485,0.472,0.460,0.447]
      xPoints = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

      #plot the r value
      plt.scatter(nop,np.absolute(r))
      plt.axis([0,nop+1,0.0,1.0])

      #plot the 95% confidence level
      plt.plot(xPoints,srcriticalValList)

      #give the graph some axies titles
      plt.xlabel("Degree of Freedom")
      plt.ylabel("Spearmans Rank Correlation Coefficient")
      plt.title("The Spermans Rank value and degrees of freedom at P=0.05")
      plt.show()
     

   ###This function is the lincoln index main window
   def lincolnIndexWindow(self):
      #Here the main window is destroyed
      main.destroy()
      global liwindow
      global lincoln
      global firsttotalEntry
      global secondtotalEntry
      global fromFirstEntry
      var = StringVar()

      #Here are the characteristics of the window 
      liwindow = Toplevel(root)
      liwindow.focus_force()
      liwindow.configure(background = "thistle1")
      liwindow.geometry("400x400+200+200")

      liLabel = tkinter.Label(liwindow, text = "LINCOLN INDEX", background = "thistle1")
      firsttotalLabel = tkinter.Label(liwindow, text = "How many did you catch in the first sample?", background = "thistle1")
      firsttotalEntry = tkinter.Entry(liwindow)

      secondtotalLabel = tkinter.Label(liwindow, text = "How many did you catch in the second sample?", background = "thistle1")
      secondtotalEntry = tkinter.Entry(liwindow)

      fromFirstLabel = tkinter.Label(liwindow, text = "How many from the second sample were also in the first one?", bg = "thistle1")
      fromFirstEntry = tkinter.Entry(liwindow)

      enterButton = tkinter.Button(liwindow, text = "Calculate", command = self.lincoln)
      backButton3 = tkinter.Button(liwindow, text = "back to main", command = self.toMainFromliwindow)

      liLabel.pack()
      firsttotalLabel.pack()
      firsttotalEntry.pack()
      secondtotalLabel.pack()
      secondtotalEntry.pack()
      fromFirstLabel.pack()
      fromFirstEntry.pack()
      enterButton.pack()
      backButton3.pack(side = BOTTOM)

   ###The lincoln index working out window    
   def lincoln(self):
      global n
      global s01
      global s02
      global r
      global N

      #exception handling first sample total
      #It tries to get an integer, otherwise it shows a error message
      try:
         s01 = firsttotalEntry.get()
         #s01 = 0
         s1 = int(s01)
      except:
         messagebox.showinfo("ERROR", "You haven't entered an integer (a whole number)")

      #exception handling second sample total
      #It tries to get an integer otherwise an error is shown
      try:    
         s02 = secondtotalEntry.get()
         #s02 = 0
         s2 = int(s02)
      except:
         messagebox.showinfo("ERROR", "You haven't entered an integer (a whole number)")

      #exception handling the second ones in the first one
      #It tries to get an integer or an error message is shown
      try:
         r = fromFirstEntry.get()
         R = int(r)
      except:
         messagebox.showinfo("ERROR", "You haven't entered an integer (a whole number)")
         
      if r != 0:
         n =(s1)*(s2)/(R)
         n = round(n,4)
         N = str(n)
      else:
         n = 0
         N = str(n)
         
      lincolnLabel = tkinter.Label(liwindow, text = "The Estimated Population is " + N, background = "thistle1")
      methodButton = tkinter.Button(liwindow, text = "Click here to see the full method", command = self.liMethodWindow)

      lincolnLabel.pack()
      methodButton.pack()

   ###The lincoln Index method window
   def liMethodWindow(self):
      liwindow.destroy()
      global limethwindow
      limethwindow = Toplevel(root)
      limethwindow.focus_force()
      limethwindow.geometry("500x500+200+200")
      limethwindow.configure(background = "thistle1")

      methodLabel = tkinter.Label(limethwindow, text = "The worked method:", bg = "thistle1")
      #first sample
      firstSampleLabel = tkinter.Label(limethwindow, text = "The total from first sample:", bg = "thistle1")
      firstSampleDataLabel = tkinter.Label(limethwindow, text = str(s01), bg = "thistle1")
      #second sample
      secondSampleLabel = tkinter.Label(limethwindow, text = "The total from second sample:", bg = "thistle1")
      secondSampleDataLabel = tkinter.Label(limethwindow, text = str(s02), bg = "thistle1")
      #same data
      sameAsFirstSampleLabel = tkinter.Label(limethwindow, text = "The samples collected in the second that were found in the first:", bg = "thistle1")
      sameASFirstSampleDataLabel = tkinter.Label(limethwindow, text = str(r), bg = "thistle1")
      #estimating the population size
      estimatedPopLabel = tkinter.Label(limethwindow, text = "(First sample total x Second sample total)/samples the same to give the final answer:",  bg = "thistle1")
      estimatedPopDataLabel = tkinter.Label(limethwindow, text = "(" + s01 + "*" + s02 + ")/" + r, bg = "thistle1")
      estimatedPopulationLabel = tkinter.Label(limethwindow, text = N,  bg = "thistle1")

      printButton = tkinter.Button(limethwindow, text = "Print the method", command = self.liprint)
      backButton = tkinter.Button(limethwindow, text = "back to main", command = self.toMainFromlimethwindow)

      methodLabel.pack()
      firstSampleLabel.pack()
      firstSampleDataLabel.pack()
      secondSampleLabel.pack()
      secondSampleDataLabel.pack()
      sameAsFirstSampleLabel.pack()
      sameASFirstSampleDataLabel.pack()
      estimatedPopLabel.pack()
      estimatedPopDataLabel.pack()
      estimatedPopulationLabel.pack()
      printButton.pack()
      backButton.pack(side = BOTTOM)

   ##The tTest scrollbar function
   def ttScrollfunction(self,event):
      ttcanvas.configure(scrollregion=ttcanvas.bbox("all"),width=465,height=470, bg = "thistle1")

   ###The t-Test main window
   def tTestWindow(self):
      main.destroy()
      global ttwindow
      global ttindependentvarEntry
      global ttdependentvarEntry
      global totalsEntry
      global ttframe
      global ttcanvas

      ttwindow = Toplevel(root)
      ttwindow.focus_force()
      ttwindow.geometry("500x500+100+100")
      ttwindow.configure(background = "thistle1")

      frame = Frame(ttwindow,relief=GROOVE,width=100,height=100,bd=1, bg="thistle1")
      frame.place(x=10,y=10)

      ttcanvas=Canvas(frame)
      ttframe=Frame(ttcanvas,bg = "thistle1")
      scrollbar = Scrollbar(frame, orient="vertical", command=ttcanvas.yview)
      ttcanvas.configure(yscrollcommand=scrollbar.set)

      #add the scrollbar
      scrollbar.pack(side="right", fill="y")
      ttcanvas.pack(side="left")

      ttcanvas.create_window((0,0),window=ttframe,anchor="nw")
      ttframe.bind("<Configure>",self.ttScrollfunction)

      ttLabel = tkinter.Label(ttframe, text = "T-TEST", background = "thistle1")
      ttindependentvarLabel = tkinter.Label(ttframe, text = "What are the independent variables in the investigation?", bg = "thistle1")
      ttindependentvarEntry = tkinter.Entry(ttframe,width = 30)
      ttdependentvarLabel = tkinter.Label(ttframe, text = "What is the dependent variable in the investigation?", bg = "thistle1")
      ttdependentvarEntry = tkinter.Entry(ttframe,width = 30)
      totalsLabel = tkinter.Label(ttframe, text = "How many values for variable 1 and 2?", background = "thistle1")
      totalsEntry = tkinter.Entry(ttframe)
      totalsGoButton = tkinter.Button(ttframe, text = "Enter", command = self.xvalsentries)
      backButton4 = tkinter.Button(ttframe, text = "back to main", command = self.toMainFromttwindow)

      ttLabel.pack()
      ttindependentvarLabel.pack()
      ttindependentvarEntry.pack()
      ttdependentvarLabel.pack()
      ttdependentvarEntry.pack()
      totalsLabel.pack()
      totalsEntry.pack()
      totalsGoButton.pack()
      backButton4.pack(side = BOTTOM)

   ###The t-Test x variable window    
   def xvalsentries(self):
      global xvalueEntry
      global xvaluelist
      global totals

      #exception handling no of variables
      try:
         tots = totalsEntry.get()
         totals = int(tots)
      except:
         messagebox.showinfo("ERROR", "You haven't entered an integer (a whole number)")

      xvalueLabel = tkinter.Label(ttframe, text = "Give the first variable values below", background = "thistle1")
      xvalueLabel.pack()
      xcounted = 0
      xvaluelist = []
      for xcounted in range (0,totals):
         xvalueEntry = tkinter.Entry(ttframe)
         xvaluelist.append(xvalueEntry)
         xvalueEntry.pack() 

      xvalueButton = tkinter.Button(ttframe, text = "Enter", command = self.yvalsentries)
      xvalueButton.pack()

   ###The t-Test y variable window
   def yvalsentries(self):
      global yvalueEntry
      global yvaluelist

      yvalueLabel = tkinter.Label(ttframe, text = "Give the second variable values below", background = "thistle1")
      yvalueLabel.pack()

      ycounted = 0
      yvaluelist = []
      for ycounted in range (0,totals):
         yvalueEntry = tkinter.Entry(ttframe)
         yvaluelist.append(yvalueEntry)
         yvalueEntry.pack()

      calculationButton = tkinter.Button(ttframe, text = "Calculate", command = self.ttest)
      calculationButton.pack()

   ###The t-Test working out window
   def ttest(self):
      global totals
      global x
      global y
      global sumx
      global x2
      global sumx2
      global sumy
      global y2
      global sumy2
      global xmean
      global ymean
      global xvar
      global yvar
      global din
      global v1
      global v2
      global t
      global ttinull
      global ttdnull
      global dof
      global ttans

      #null hypothesis
      #exception handling independent and dependent variables
      try:
         tti = ttindependentvarEntry.get()
         ttinull = str(tti)
         ttd = ttdependentvarEntry.get()
         ttdnull = str(ttd)
      except:
         messagebox.showinfo("ERROR", "You haven't entered the correct data type (need to enter text)")

      #get x entries into a list
      x = []
      for xvalueEntry in xvaluelist:
         #exception handling x vals
         try:
            r = xvalueEntry.get()
            a = float(r)
         except:
            messagebox.showinfo("ERROR", "You haven't entered a number (can be a decimal)")
         x.append(a)

      #convert items in list to float
      for p in range (0, len(x)):
         x[p] = float(x[p])

      #get the y entries into a list
      y = []
      for yvalueEntry in yvaluelist:
         #exception handling y vals
         try:
            s = yvalueEntry.get()
            b = float(s)
         except:
            messagebox.showinfo("ERROR", "You haven't entered a number (can be a decimal)")     
         y.append(b)

      #convert items in a list to float
      for q in range (0, len(y)):
         y[q] = float(y[q])

      #get the sum of the values in the x list
      sumx = sum(x)

      #find the x-squared vales with the sum 
      i = 0
      x2 = []
      for i in range (0, len(x)):
         xs = x[i] * x[i]
         i = i + 1
         xs = round(xs,3)
         x2.append(xs)

      sumx2 = sum(x2)

      #get the sum of the values in the y list
      sumy = sum(y)

      #find the y-squared vales with the sum 
      e = 0
      y2 = []
      for e in range (0, len(x)):
         ys = y[e] * y[e]
         e = e + 1
         y2.append(ys)

      sumy2 = sum(y2)

      #the x mean
      xmean =(sumx)/totals
      xmean = round(xmean,4)

      #the y mean
      ymean = (sumy)/totals
      ymean = round(ymean,4)

      #the xvariance
      #sumx**2 is sumx squared
      xa = (sumx**2)/totals
      xvar = (sumx2 - xa) /(totals - 1)
      xvar = round(xvar,4)

      #the yvariance
      ya = (sumy**2)/totals
      yvar = (sumy2 - ya) /(totals - 1)
      yvar = round(yvar,4)

      #the difference in means
      #abs gives the +ve value
      din = abs(xmean - ymean)
      din = round(din,4)

      #the addition of variance over total no of data items
      v1 = xvar/totals
      v1 = round(v1,4)
      v2 = yvar/totals
      v2 = round(v2,4)

      #the t value
      #sqrt has to be imported from the math library
      t = din/ (math.sqrt(v1+v2))
      t = str(round(t,3))

      #once the t-value is found
      #the degree of freedom needs to be calculated and then compared to table values

      dof = (totals + totals)-2
      dof = str(dof)

      #check if the hypothesis is significant or not P=0.05
      #starts at a minimum of 1 
      ttcriticalValList = [12.706,4.303,3.182,2.776,2.571,2.447,2.365,2.306,2.262,2.228,2.201,2.179,2.160,2.145,2.131,2.120,2.110,2.101,2.093,2.086,2.08,2.074,2.069,2.064,2.060,2.056,2.052,2.048]
      for n in range(0,len(ttcriticalValList)):
         g = int(dof)- 1
         ttcriticalVal = ttcriticalValList[g]

      #is it significant?
      if float(t) >= float(ttcriticalVal):
         ttans = "The T-Test value of " + str(t) + " is greater than the critical value of " + str(ttcriticalVal)+ "\n We reject null hypothesis at a 5% significance level, \n as there is a 5% probability that the results due to chance"
      else:
         ttans = "The T-Test value of " + str(t) + " is less than the critical value of " + str(ttcriticalVal)+ "\n We accept the null hypothesis at a 5% significance level, \n as there is a 95% probability that the results are due to chance"

      ttestLabel = tkinter.Label(ttframe, text = "The T-test value is: " + t, background = "thistle1")
      dofLabel = tkinter.Label(ttframe, text = "The degree of freedom is: " + dof, background = "thistle1")
      srnullHypothesisLabel = tkinter.Label(ttframe, text = "The null hypothesis is:", background = "thistle1")
      srnullHypothesisDataLabel = tkinter.Label(ttframe, text = "There is no significant difference between " + str(ttdnull) + " in " + str(ttinull), bg = "thistle1")
      ttcriticalValCompLabel = tkinter.Label(ttframe, text = ttans, bg = "thistle1")
      methodButton = tkinter.Button(ttframe, text = "Click here to see the full method", command = self.ttMethodWindow)
      graphButton = tkinter.Button(ttframe, text = "Click to see graph", command = self.ttGraph)

      ttestLabel.pack()
      dofLabel.pack()
      srnullHypothesisLabel.pack()
      srnullHypothesisDataLabel.pack()
      ttcriticalValCompLabel.pack()
      methodButton.pack()
      graphButton.pack()

   ###The method for working out the t-test is below, each step is shown   
   def ttMethodWindow(self):
      ttwindow.destroy()
      global ttmethwindow
      ttmethwindow = Toplevel(root)
      ttmethwindow.focus_force()
      ttmethwindow.geometry("500x700+100+100")
      ttmethwindow.configure(background = "thistle1")

      methodLabel = tkinter.Label(ttmethwindow, text = "The worked Method", bg = "thistle1")
      #total no of items in variable 1 and 2
      totalItemsLabel = tkinter.Label(ttmethwindow, text = "The number of items in variable 1 and 2: " + str(totals), bg = "thistle1")
      #variable 1 list values
      xListLabel = tkinter.Label(ttmethwindow, text = "The variable 1 values:", bg = "thistle1")
      xListDataLabel = tkinter.Label(ttmethwindow, text = str(x), bg = "thistle1")
      #variable 1 list values squared
      x2ListLabel = tkinter.Label(ttmethwindow, text = "The variable 1 values are squared to give:", bg = "thistle1")
      x2ListDataLabel = tkinter.Label(ttmethwindow, text = str(x2), bg = "thistle1")
      #sum of variable 1 list values
      sumxValsLabel = tkinter.Label(ttmethwindow, text = "Now find the sum of the variable 1 values: " + str(sumx), bg = "thistle1")
      #sum of variable 1 list squared
      sumx2ValsLabel = tkinter.Label(ttmethwindow, text = "Now find the sum of the variable 1 values squared: " + str(sumx2), bg = "thistle1")
      #variable 2 list values
      yListLabel = tkinter.Label(ttmethwindow, text = "The variable 2 values:", bg = "thistle1")
      yListDataLabel = tkinter.Label(ttmethwindow, text = str(y), bg = "thistle1")
      #variable 2 list values squared
      y2ListLabel = tkinter.Label(ttmethwindow, text = "The variable 2 values are squared to give:", bg = "thistle1")
      y2ListDataLabel = tkinter.Label(ttmethwindow, text = str(y2), bg = "thistle1")
      #sum of variable 2 list values
      sumyValsLabel = tkinter.Label(ttmethwindow, text = "Now find the sum of the variable 2 values: " + str(sumy),bg = "thistle1")
      #sum of variable 2 list squared
      sumy2ValsLabel = tkinter.Label(ttmethwindow, text = "Now find he sum of the variable 2 values squared: " + str(sumy2),bg = "thistle1")
      #x mean
      xmeanLabel = tkinter.Label(ttmethwindow, text = "Find the mean of the variable 1 values: " + str(xmean),bg = "thistle1")
      #y mean
      ymeanLabel = tkinter.Label(ttmethwindow, text = "Find the mean of the variable 2 values: " + str(ymean),bg = "thistle1")
      #difference in mean
      diffInMeanLabel = tkinter.Label(ttmethwindow, text = "Find the differences in mean, giving this as a positive value (modulus)",bg = "thistle1")
      diffInMeanDataLabel = tkinter.Label(ttmethwindow, text = str(din), bg = "thistle1")
      #x variance
      xvarLabel = tkinter.Label(ttmethwindow, text = "Find the variance of variable 1",bg = "thistle1")
      xvarianceLabel = tkinter.Label(ttmethwindow, text = str(sumx2) + "-((" + str(sumx) + "^2)/" + str(totals) + ")/" + str(totals) + "-1",bg = "thistle1") 
      xvarDataLabel = tkinter.Label(ttmethwindow, text = str(xvar), bg = "thistle1")
      #y variance
      yvarlabel = tkinter.Label(ttmethwindow, text = "Find the variance of variable 2",bg = "thistle1")
      yvarianceLabel = tkinter.Label(ttmethwindow, text = str(sumy2) + "-((" + str(sumy) + "^2)/" + str(totals) + ")/" + str(totals) + "-1",bg = "thistle1") 
      yvarDataLabel = tkinter.Label(ttmethwindow, text = str(yvar), bg = "thistle1")
      #variable 1
      var1Label = tkinter.Label(ttmethwindow, text = "Now work out the variable 1 variance / number of items",bg = "thistle1")
      variable1Label = tkinter.Label(ttmethwindow, text = str(xvar) + "/" + str(totals), bg = "thistle1")
      var1DataLabel = tkinter.Label(ttmethwindow, text = str(v1), bg = "thistle1")
      #variable 2
      var2Label = tkinter.Label(ttmethwindow, text = "Now work out the variable 2 variance / number of items",bg = "thistle1")
      variable2Label = tkinter.Label(ttmethwindow, text = str(yvar) + "/" + str(totals), bg = "thistle1")
      var2DataLabel = tkinter.Label(ttmethwindow, text = str(v2), bg = "thistle1")
      #t value
      tvalueLabel = tkinter.Label(ttmethwindow, text = "Now do the difference in mean / squareroot of the sum of the two above values" ,bg = "thistle1")
      ttValueLabel = tkinter.Label(ttmethwindow, text = str(din) + "/ squareroot(" + str(v1) + "+" + str(v2) + ") gives the final answer:", bg = "thistle1")
      ttValuedataLabel = tkinter.Label(ttmethwindow, text = str(t), bg = "thistle1")
      printButton = tkinter.Button(ttmethwindow, text = "Print the method", command = self.ttprint)
      backButton = tkinter.Button(ttmethwindow, text = "back to main", command = self.toMainFromttmethwindow)

      methodLabel.pack()
      totalItemsLabel.pack()
      xListLabel.pack()
      xListDataLabel.pack()
      x2ListLabel.pack()
      x2ListDataLabel.pack()
      sumxValsLabel.pack()
      sumx2ValsLabel.pack()
      yListLabel.pack()
      yListDataLabel.pack()
      y2ListLabel.pack()
      y2ListDataLabel.pack()
      sumyValsLabel.pack()
      sumy2ValsLabel.pack()
      xmeanLabel.pack()
      ymeanLabel.pack()
      diffInMeanLabel.pack()
      diffInMeanDataLabel.pack()
      xvarLabel.pack()
      xvarianceLabel.pack()
      xvarDataLabel.pack()
      yvarlabel.pack()
      yvarianceLabel.pack()
      yvarDataLabel.pack()
      var1Label.pack()
      var1DataLabel.pack()
      var2Label.pack()
      var2DataLabel.pack()
      tvalueLabel.pack()
      ttValueLabel.pack()
      ttValuedataLabel.pack()
      printButton.pack()
      backButton.pack(side = BOTTOM)

   ###The Ttest graph
   def ttGraph(self):
      #95% conidence level or P=0.05
      #starts at a minimum of 1 to 28
      ttcriticalValList = [12.706,4.303,3.182,2.776,2.571,2.447,2.365,2.306,2.262,2.228,2.201,2.179,2.160,2.145,2.131,2.120,2.110,2.101,2.093,2.086,2.08,2.074,2.069,2.064,2.060,2.056,2.052,2.048]
      xPoints = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

      #plot the t value
      plt.scatter(float(dof),float(t))
      plt.axis([0,float(dof)+1,0.0,12.706])

      #plot the 95% confidence level
      plt.plot(xPoints,ttcriticalValList)

      #give the graph some axies titles
      plt.xlabel("Degree of Freedom")
      plt.ylabel("T-test")
      plt.title("The T-test value and degrees of freedom at P=0.05")
      plt.show()

   #These all help with the transition between windows
   def toMainFromcswindow(self):
      cswindow.destroy()
      self.mainWindow()
     
   def toMainFromsrwindow(self):
      srwindow.destroy()
      self.mainWindow()

   def toMainFromliwindow(self):
      liwindow.destroy()
      self.mainWindow()

   def toMainFromttwindow(self):
      ttwindow.destroy()
      self.mainWindow()

   def toMainFromwtwindow(self):
      wtwindow.destroy()
      self.mainWindow()

   def toMainFrommwindow(self):
      mwindow.destroy()
      self.mainWindow()

   def toMainFromidwindow(self):
      idwindow.destroy()
      self.mainWindow()
     
   def toMainFromaiwindow(self):
      aiwindow.destroy()
      self.mainWindow()

   def toMainFromsrmethwindow(self):
      srmethwindow.destroy()
      self.mainWindow()

   def toMainfromcsmethwindow(self):
      csmethwindow.destroy()
      self.mainWindow()

   def toMainFromlimethwindow(self):
      limethwindow.destroy()
      self.mainWindow()

   def toMainFromttmethwindow(self):
      ttmethwindow.destroy()
      self.mainWindow()

   def toMainFrompicturewindow(self):
      picturewindow.destroy()
      self.mainWindow()
        
   ###This will help further how the user can see the worked method, by enabling it to be printed out, a hard copy can be given to students or the teaacher can use the hard copy
   def srprint(self):
      #try and open up a spearmans rank file to store the data
      try:
         spearmansRankFile = open("spearmansRank.txt","r")
      #if the file cannot be found make one
      except:
         spearmansRankFile = open("spearmansRank.txt","a")
         
      #add the required data to the file
      spearmansRankFile = open("spearmansRank.txt","w")
      spearmansRankFile.write("The Worked Method" + "\n\n")
      spearmansRankFile.write("The first variable value list:" + "\n")
      spearmansRankFile.write(str(copyofx) + "\n\n")
      spearmansRankFile.write("The first variable value list ranked in ascending order:" + "\n")
      spearmansRankFile.write(str(xfinalRank) + "\n\n")
      spearmansRankFile.write("The second variable value list:" + "\n")
      spearmansRankFile.write(str(copyofy) + "\n\n")
      spearmansRankFile.write("The second variable value list ranked in ascending order:" + "\n")
      spearmansRankFile.write(str(yfinalRank) + "\n\n")
      spearmansRankFile.write("Find the difference between each item in the ranked lists:" + "\n")
      spearmansRankFile.write(str(D) + "\n\n")
      spearmansRankFile.write("The above items are now squared to give this:" + "\n")
      spearmansRankFile.write(str(D2) + "\n\n")
      spearmansRankFile.write("The sum of the values given above are:" + "\n")
      spearmansRankFile.write(str(SD2/6) + "\n\n")
      spearmansRankFile.write("The above value is now multiplied by 6:" + "\n")
      spearmansRankFile.write(str(SD2) + "\n\n")
      spearmansRankFile.write("(n^3)-n is now worked out (n is the number of items):" + "\n")
      spearmansRankFile.write(str(n) + "\n\n")
      spearmansRankFile.write("Do 1-" +  str(SD2) + "/" + str(n) + " to get the final answer of:" + "\n")
      spearmansRankFile.write(str(r) + "\n\n")

      spearmansRankFile.write("The number of pairs of data:" + str(nop) + "\n")
      spearmansRankFile.write("The null hypothesis is:" + "\n")
      spearmansRankFile.write("There is no significant correlation between " + str(srinull) + " and " + str(srdnull) + "\n\n")
      spearmansRankFile.write(str(srans) + "\n")

      os.startfile("spearmansRank.txt","print")
      spearmansRankFile.close()                       

   ###This will help further how the user can see the worked method, by enabling it to be printed out, a hard copy can be given to students or the teaacher can use the hard copy
   def csprint(self):
      #try and open up a chi-squared file to store the data
      try:
         chiSquaredFile = open("chiSquared.txt","r")
      #if the file cannot be found make one
      except:
         chiSquaredFile = open("chiSquared.txt","a")      
         
      #add the required data to the file
      chiSquaredFile = open("chiSquared.txt","w")
      chiSquaredFile.write("The Worked Method" + "\n\n")
      chiSquaredFile.write("The total found at each site is below in the list:" + "\n")
      chiSquaredFile.write(str(values) + "\n\n")
      chiSquaredFile.write("Add the values above in the list to get the combined totals:" + "\n")
      chiSquaredFile.write(str(sumSiteVal) + "\n\n")
      chiSquaredFile.write("Calculate the mean by doing this: (" + str(sumSiteVal) + ")/" + str(category) + "\n")
      chiSquaredFile.write(str(mean) + "\n\n")
      chiSquaredFile.write("For each site we need to work out the (observed - mean)^2/mean  :" + "\n")
      for n in range(0, category):
         chiSquaredFile.write("(" + str(values[n]) + "-" + str(mean) + ")/" + str(mean) + "\n")
         chiSquaredFile.write(str(C[n]) + "\n")
      chiSquaredFile.write("\nThe values calculated above for each site are added together to give the final answer:" + "\n")
      chiSquaredFile.write(str(X) + "\n\n")

      chiSquaredFile.write("The degree of freedom is: " + str(csdof) + "\n\n")
      chiSquaredFile.write("The null hypothesis is:" + "\n")
      chiSquaredFile.write("There is no significant difference in " + str(csdnull) + " in " + str(theIndependentVars) + "\n\n")
      chiSquaredFile.write(str(csans) + "\n")

      os.startfile("chiSquared.txt","print")
      chiSquaredFile.close()                       

   ###This will help further how the user can see the worked method, by enabling it to be printed out, a hard copy can be given to students or the teaacher can use the hard copy
   def liprint(self):
      #try and open up a lincoln index file to store the data
      try:
         lincolnIndexFile = open("lincolnIndex.txt","r")
      #if the file cannot be found make one
      except:
         lincolnIndexFile = open("lincolnIndex.txt","a")
         
      #add the required data to the file
      lincolnIndexFile = open("lincolnIndex.txt","w")
      lincolnIndexFile.write("The Worked Method" + "\n\n")
      lincolnIndexFile.write("The total from the first sample:" + "\n")
      lincolnIndexFile.write(str(s01) + "\n\n")
      lincolnIndexFile.write("The total from the second sample:" + "\n")
      lincolnIndexFile.write(str(s02) + "\n\n")
      lincolnIndexFile.write("The samples collected in the second that were found in the first:" + "\n")
      lincolnIndexFile.write(str(r) + "\n\n")
      lincolnIndexFile.write("First sample total x Second sample total/ Samples the Same, to give the final answer:" + "\n")
      lincolnIndexFile.write(str(s01) + "*" + str(s02) + "/" + str(r)  + "\n")
      lincolnIndexFile.write(str(N) + "\n\n")
      os.startfile("lincolnIndex.txt","print")
      lincolnIndexFile.close()                       

   ###This will help further how the user can see the worked method, by enabling it to be printed out, a hard copy can be given to students or the teaacher can use the hard copy    
   def ttprint(self):
      #try and open up a lincoln index file to store the data
      try:
         tTestFile = open("tTest.txt","r")
      #if the file cannot be found make one
      except:
         tTestFile = open("tTest.txt","a")
         
      #add the required data to the file
      tTestFile = open("tTest.txt","w")
      tTestFile.write("The Worked Method" + "\n\n")
      tTestFile.write("The number of items in variable 1 and 2:" + "\n")
      tTestFile.write(str(totals) + "\n\n")
      tTestFile.write("The variable 1 values:" + "\n")
      tTestFile.write(str(x) + "\n\n")
      tTestFile.write("The variable 1 values are squared to give:" + "\n")
      tTestFile.write(str(x2) + "\n\n")
      tTestFile.write("Now find the sum of the variable 1 values squared:" + "\n")
      tTestFile.write(str(sumx2) + "\n\n")
      tTestFile.write("The variable 2 values:" + "\n")
      tTestFile.write(str(y) + "\n\n")
      tTestFile.write("The variable 2 values are squared to give:" + "\n")
      tTestFile.write(str(y2) + "\n\n")
      tTestFile.write("Now find the sum of the variable 2 values squared:" + "\n")
      tTestFile.write(str(sumy2) + "\n\n")
      tTestFile.write("Find the mean of the variable 1 values:" + "\n")
      tTestFile.write(str(xmean) + "\n\n")
      tTestFile.write("Find the mean of the variable 2 values:" + "\n")
      tTestFile.write(str(ymean) + "\n\n")
      tTestFile.write("Find the differences in mean, giving this as a positive value (modulus):" + "\n")
      tTestFile.write(str(din) + "\n\n")
      tTestFile.write("Find the variance of variable 1:" + "\n")
      tTestFile.write(str(sumx2) + "-((" + str(sumx) + "^2)/" + str(totals) + ")/" + str(totals) + "-1" + "\n")
      tTestFile.write(str(xvar) + "\n\n")
      tTestFile.write("Find the variance of variable 2:" + "\n")
      tTestFile.write(str(sumy2) + "-((" + str(sumy) + "^2)/" + str(totals) + ")/" + str(totals) + "-1" + "\n")
      tTestFile.write(str(yvar) + "\n\n")
      tTestFile.write("Now work out the (variable 1 variance / number of items)  :" + "\n")
      tTestFile.write(str(xvar) + "/" + str(totals) + "\n")
      tTestFile.write(str(v1) + "\n\n")
      tTestFile.write("Now work out the (variable 2 variance / number of items)   :" + "\n")
      tTestFile.write(str(yvar) + "/" + str(totals) + "\n")
      tTestFile.write(str(v2) + "\n\n")
      tTestFile.write("Now do the difference in mean / squareroot of the sum of the two above values:" + "\n")
      tTestFile.write(str(din) + "/ squareroot(" + str(v1) + str(v2) + "), gives a final answer:" + "\n")
      tTestFile.write(str(t) + "\n\n")

      tTestFile.write("The degree of freedom is: " + str(dof) + "\n\n")  
      tTestFile.write("The null hypothesis is:" + "\n")
      tTestFile.write("There is no significant difference between " + str(ttdnull) + " in " + str(ttinull) + "\n\n")
      tTestFile.write(str(ttans) + "\n")

      os.startfile("tTest.txt","print")
      tTestFile.close()   

#MAIN PROGRAM#
root = Tk()
root.iconify()
#call the mainWindow def to get the main tkinter screen
Statistics()  

#add all code before this line below - should only work if this is the last thing
root.mainloop()





















