from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import csv

def form():
    # ... the code for the form ...

    # Get the values from the form
    full_name = entry_1.get()
    email = entry_2.get()
    gender = var.get()
    amount = entry_3.get()

def form():

    root = Tk()
    root.geometry('600x600')
    root.title("First page")
    

    label_0 = Label(root, text="Budget Buddy",width=25,font=("underline", 20))
    label_0.place(x=60,y=53)


    label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
    label_1.place(x=90,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Email",width=20,font=("bold", 10))
    label_2.place(x=78,y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240,y=180)

    label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=80,y=230)
    var = IntVar()
    Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

    label_4 = Label(root, text="Amount of money:",width=20,font=("bold", 10))
    label_4.place(x=70,y=280)
    label_5 = Label(root, text="Phone no.:",width=20,font=("bold", 10))
    label_5.place(x=80,y=280)


    entry_2 = Entry(root)
    entry_2.place(x=240,y=280)

    Button(root, text='Submit',command=budget,width=20,bg='#3ED7E4',fg='white').place(x=180,y=380)
    # it is use for display the registration form on the window
 



    root.mainloop()
    
def budget():
   
    
   import tkinter as tk 
   class MainWindow:
       def __init__(self):
           self.root = tk.Tk() # Initiate new tkinter object
           self.root.geometry("920x740") # Set dimension size
           self.root.resizable(width=False, height=False) # Lock app dimension
           self.root.title("Budget Buddy") # Window title
           self.root.configure(bg='#89CFF0')  # Set the background color of the window
           self.style = ('Monospace', 18)
           self.draw('  💰💵 💵💰\n\n"A penny saved is a penny earned"\n \nPlease enter your amount to continue...\n')
           self.buttons()
           self.root.mainloop() # Keep UI alive

   # ... rest of the code ...

   ###############
   #   WIDGETS   #
   ###############

       def draw(self, msg):
           self.frameText = tk.Frame(self.root, height=19, width=50)
           self.textBox = tk.Text(self.frameText, height=19, width=50, relief='flat', bg='light yellow', font=self.style)
           self.textBox.insert(1.0, msg)
           self.textBox.config(state='disabled')
           self.frameText.grid(row=0, column=0)
           self.textBox.pack(padx=3, pady=3)
       
       
       def pie():      
               import tkinter as tk
               from tkinter import ttk
               from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
               from matplotlib.figure import Figure
        
               # Create a new tkinter window
               root = tk.Tk()
               root.geometry('600x600')
               root.title('Budget Buddy')
               root.configure(bg='#000080')
        
               # Define the data for the pie chart
               labels = ['Mess', 'Transportation', 'Rent', 'Bills']
               sizes = [55, 65, 75, 85]
               colors= ['#89CFF0', '#6699ff', '#99b3ff','#00FFFF'] 
        
               # Create a new matplotlib figure and plot the pie chart
               fig = Figure(figsize=(7, 7))
               ax = fig.add_subplot(111)
               ax.pie(sizes, labels=labels, autopct='%1.1f%%')
               ax.set_title('Expenses')
        
               # Create a new canvas to display the figure
               canvas = FigureCanvasTkAgg(fig, master=root)
               canvas.draw()
               canvas.get_tk_widget().pack()
        
               # Start the tkinter event loop
               root.mainloop()
       def email():
           import smtplib
           import ssl

           # Setup port number and servr name

           smtp_port = 587                 # Standard secure SMTP port
           smtp_server = "smtp.gmail.com"  # Google SMTP Server

           email_from = "budgetbuddy02@gmail.com"
           email_to = "ayushmahandule@gmail.com"

           pswd = "brotaqgnsuwigbyf"

           # content of message

           message = "HI , THIS IS BUDGET BUDDY!!! You have exceeded your budget"

           # Create context
           simple_email_context = ssl.create_default_context()


           try:
               # Connect to the server
               print("Connecting to server...")
               TIE_server = smtplib.SMTP(smtp_server, smtp_port)
               TIE_server.starttls(context=simple_email_context)
               TIE_server.login(email_from, pswd)
               print("Connected to server :-)")
               
               # Send the actual email
               print()
               print(f"Sending email to - {email_to}")
               TIE_server.sendmail(email_from, email_to, message)
               print(f"Email successfully sent to - {email_to}")

           # If there's an error, print it out
           except Exception as e:
               print(e)

           # Close the port
           finally:
               TIE_server.quit()

       def buttons(self):
           self.frame = tk.Frame(self.root, height=1, width=50)
           self.frame.grid(row=0, column=1)
           self.label = tk.Label(self.frame, text='Your total amount:')
           self.entry = tk.Entry(self.frame, font=12)
           self.calBudget = tk.Button(self.frame, text='Calculate Budget', command=self.calculateBudget, width=20)
           self.viewBudget = tk.Button(self.frame, text='View Budget Plan', command=self.viewBudgetPlan, width=20)
           self.viewSpending = tk.Button(self.frame, text='Monthly expenses', command=self.popUp, width=20)
           self.pie = tk.Button(self.frame, text='Pie Chart', command=pie, width=20)
           self.email = tk.Button(self.frame, text='Send Email', command=email, width=20)
           items = [self.label, self.entry, self.calBudget, self.viewBudget, self.viewSpending, self.pie, self.email]
           for item in items:
               item.pack(padx=10, pady=20)
          
       def popUp(self):
           self.popUp = tk.Tk()
           self.popUp.geometry("500x500")
           self.popUp.title("Rent & Bills")
           self.popUp.resizable(width=False, height=False)
           self.rentLabel = tk.Label(self.popUp, text="Rent:")
           self.rentEntry = tk.Entry(self.popUp, width=25)
           self.billsLabel = tk.Label(self.popUp, text="Total Monthly Bills:")
           self.billsEntry = tk.Entry(self.popUp, width=25)
           self.messLabel = tk.Label(self.popUp, text=" Mess:")
           self.messEntry = tk.Entry(self.popUp, width=25)
           self.TransportationLabel = tk.Label(self.popUp, text=" Transportation:")
           self.TransportationEntry = tk.Entry(self.popUp, width=25)
           
           self.done = tk.Button(self.popUp, text='Done', command=self.calculateSpending)
           items = [self.rentLabel, self.rentEntry, self.billsLabel, self.billsEntry,self.messLabel,self.messEntry, self.TransportationLabel,self.TransportationEntry, self.done]
           for item in items: item.pack(pady=5)
           
           

   #################
   #   FUNCTIONS   #
   #################

       def calculateBudget(self):
           self.budget = float(self.entry.get() or 0)
           self.spending = self.budget * 0.5
           self.draw(f"Total Amount: ₹{'{:.2f}'.format(self.budget)}\nSpending Money: ₹{'{:.2f}'.format(self.spending)}")
       
       def viewBudgetPlan(self):
           self.budget = float(self.entry.get() or 0)
           self.spending = self.budget * 0.5
           self.savings = self.budget * 0.3
           self.extra = self.budget - self.spending - self.savings
           self.draw(f"Total Amount\t\t: ₹{'{:.2f}'.format(self.budget)}\nSpending Money\t\t: ₹{'{:.2f}'.format(self.spending)} \
               \nTo Save\t\t: ₹{'{:.2f}'.format(self.savings)}\nExtra\t\t: ₹{'{:.2f}'.format(self.extra)}")

       def calculateSpending(self):
          self.rent = float(self.rentEntry.get() or 0)
          self.bills = float(self.billsEntry.get() or 0)
          self.mess = float(self.messEntry.get() or 0)
          self.Transportation = float(self.TransportationEntry.get() or 0)
          self.popUp.destroy()
          self.budget = float(self.entry.get() or 0)
          self.draw(f"### TOTAL BUDGET ###\nTotal\t\t: ₹{'{:.2f}'.format(self.budget)}\nSpending Money\t\t: ₹{'{:.2f}'.format(self.budget*0.5)} \
           \n\n### EXPENSES ###\nRent\t\t: ₹{'{:.2f}'.format(self.rent)}\nBills\t\t: ₹{'{:.2f}'.format(self.bills)}\n mess\t\t: ₹{'{:.2f}'.format(self.mess)}\n Transportation\t\t: ₹{'{:.2f}'.format(self.Transportation)}")


       def calculateDaily(self):
           self.rent = float(self.rentEntry.get() or 0)
           self.bills = float(self.billsEntry.get() or 0)
           self.popUp.destroy()
           self.budget = float(self.entry.get() or 0)
           self.food = (self.budget * 0.5) - self.rent - self.bills
           self.draw(f"### TOTAL BUDGET ###\nTotal\t\t: ₹{'{:.2f}'.format(self.budget)}\nSpending Money\t\t: ₹{'{:.2f}'.format(self.budget*0.5)} \
               \n\n### EXPENSES ###\nRent\t\t: ₹{'{:.2f}'.format(self.rent)}\nBills\t\t: ₹{'{:.2f}'.format(self.bills)}\nFood\t\t: ₹{'{:.2f}'.format(self.food)}")


   if __name__ == '__main__':
       MainWindow()
   
def pie():      
       import tkinter as tk
       from tkinter import ttk
       from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
       from matplotlib.figure import Figure

       # Create a new tkinter window
       root = tk.Tk()
       root.geometry('600x600')
       root.title('Budget Buddy')

       # Define the data for the pie chart
       labels = ['Mess', 'Transportation', 'Rent', 'Bills']
       sizes = [55, 65, 75, 85]
       colors= ['#89CFF0', '#6699ff', '#99b3ff','#00FFFF'] 

       # Create a new matplotlib figure and plot the pie chart
       fig = Figure(figsize=(7, 7))
       ax = fig.add_subplot(111)
       ax.pie(sizes, labels=labels, autopct='%1.1f%%')
       ax.set_title('Expenses')

       # Create a new canvas to display the figure
       canvas = FigureCanvasTkAgg(fig, master=root)
       canvas.draw()
       canvas.get_tk_widget().pack()

       # Start the tkinter event loop
       root.mainloop()

def email():
    import smtplib
    import ssl

    # Setup port number and servr name

    smtp_port = 587                 # Standard secure SMTP port
    smtp_server = "smtp.gmail.com"  # Google SMTP Server

    email_from = "budgetbuddy02@gmail.com"
    email_to = "ayushmahandule@gmail.com"

    pswd = "brotaqgnsuwigbyf"

    # content of message

    message =  "We all know how important it is to save money, but it can be a challenging task. With expenses piling up and bills to pay, it can be hard to find ways to cut back and increase our savings. That's where Budget Buddy comes in!"

    "We at Budget Buddy believe that everyone can achieve financial stability and live a stress-free life. With our budgeting tools, you can easily track your expenses, analyze your spending habits, and identify areas where you can cut back."
                
    "But that's not all. We've also compiled a list of money-saving hacks that you can implement right away to start seeing the benefits. These include:"
    
    "Eating out less often: Cooking at home is not only healthier, but it's also much more cost-effective."
    
    "Using coupons and discount codes: Always look for ways to save money, whether it's through coupons or promotional codes."
    
    "Setting a budget: Plan your expenses in advance and stick to your budget to avoid overspending."
    
    "Paying off debts: Pay off your debts as soon as possible to avoid accruing interest charges."
    
    "Investing in a retirement plan: The earlier you start saving for retirement, the more money you'll have in the long run."
    
    "By incorporating these hacks into your daily routine, you can start saving money and worry less about your finances. Budget Buddy is here to help you achieve your financial goals and live a more fulfilling life."
    
    "If you have any questions or need assistance, please don't hesitate to contact us. We're always happy to help."
    
    "Best regards,"
    
    
    
    "Budget Buddy"

    # Create context
    simple_email_context = ssl.create_default_context()


    try:
        # Connect to the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from, pswd)
        print("Connected to server :-)")
        
        # Send the actual email
        print()
        print(f"Sending email to - {email_to}")
        TIE_server.sendmail(email_from, email_to, message)
        print(f"Email successfully sent to - {email_to}")

    # If there's an error, print it out
    except Exception as e:
        print(e)

    # Close the port
    finally:
        TIE_server.quit()





    


root = Tk()
root.title("Colorful Window")
root.geometry("800x600")

# Set the background color of the window
root.configure(bg='#008B8B')

# Load an image
image = PhotoImage(file=r"./Screenshot_20230208_084120.png")

# Create a label to display the image
image_label = ttk.Label(root, image=image)
image_label.pack(pady=50)

# Create a button
button = ttk.Button(root, text="Next", command=form)
button.pack()


root.mainloop()

