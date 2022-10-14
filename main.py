# import all classes / functions from the tkinter
import tkinter
from tkinter import *


# Function for clearing the contents of all entry boxes
def clear_all():
    # whole content of entry boxes is deleted
    salary_field.delete(0, END)
    current_savings_field.delete(0, END)
    periodic_field.delete(0, END)
    match_field.delete(0, END)
    time_field.delete(0, END)
    return_field.delete(0, END)
    projection_field.delete(0, END)

    # set focus on the current_savings_field entry box
    salary_field.focus_set()


# Function to find compound interest
def calculate_return():
    # get a content from entry box
    salary = int(salary_field.get())

    current_savings = int(current_savings_field.get())

    periodic = float(periodic_field.get()) / 100

    match = float(match_field.get()) / 100

    time = int(time_field.get())

    interest = float(return_field.get()) / 100

    check = checked.get()

    # Calculates compound interest
    rate = (salary * (periodic + match)) / 12
    CI = current_savings + (rate * (((1 + (interest / 12)) ** (12 * time)) - 1) / (interest / 12))
    CI_inflation = current_savings + (rate * (((1 + ((interest-.03) / 12)) ** (12 * time)) - 1) / ((interest-.03) / 12))

    # insert method inserting the
    # value in the text entry box.
    if check == 1:
        projection_field.insert(10, "${:,.2f}".format(CI_inflation))
    else:
        projection_field.insert(10, "${:,.2f}".format(CI))

def help_button():
    label13.grid(row=13, column=0, columnspan=2, rowspan=5, padx=10, pady=10)


# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # Set the configuration of GUI window
    root.geometry("800x800")

    # set the name of tkinter GUI window
    root.title("Investment Calculator")

    # Create a yearly salary Amount : label
    label1 = Label(root, text="Yearly Salary (no commas) : ",
                   fg='black')

    # Create a principal Amount : label
    label2 = Label(root, text="Current Savings : ",
                   fg='black')

    label3 = Label(root, text="Periodic Investment (% Salary) : ",
                   fg='black')

    # Create a Match : label
    label4 = Label(root, text="Match (% Salary) : ",
                   fg='black')

    # Create a Time : label
    label5 = Label(root, text="Years to Invest : ",
                   fg='black')

    # Create a Expected Return : label
    label6 = Label(root, text="Expected Return (%) : ",
                   fg='black')

    label7 = Label(root, text="Advanced Options",
                   fg='black')

    # Create a Include Inflation : label
    label8 = Label(root, text="Include Inflation : ",
                   fg='black')

    # Create a Projected Return : label
    label10 = Label(root, text="Projected Balance : ",
                   fg='black')

    label13 = Label(root,
                    text="""    How to use this program	
                    Yearly Salary – Current Annual Income 
                    Current Savings– Amount already saved
                    Periodic Investment – Amount you wish to save (% of salary)	
                    Company Match Amount – Amount your company contributes (% of salary)	
                    Years to Invest – Years to reach your investment goal/retirement
                    Expected Annual Return – What percent you expect your investment to grow (i.e. 8%)
                    Inflation – Choose whether you want the results to include inflation adjustments.
                    """,
                   fg='black')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=4, column=0, padx=10, pady=10)
    label5.grid(row=5, column=0, padx=10, pady=10)
    label6.grid(row=6, column=0, padx=10, pady=10)
    label7.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    label8.grid(row=8, column=0, pady=10)
    label10.grid(row=10, column=0, padx=10, pady=10)



    # Create a entry box
    # for filling or typing the information.
    salary_field = Entry(root)
    current_savings_field = Entry(root)
    periodic_field = Entry(root)
    match_field = Entry(root)
    time_field = Entry(root)
    return_field = Entry(root)
    projection_field = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    salary_field.grid(row=1, column=1, padx=10, pady=10)
    current_savings_field.grid(row=2, column=1, padx=10, pady=10)
    periodic_field.grid(row=3, column=1, padx=10, pady=10)
    match_field.grid(row=4, column=1, padx=10, pady=10)
    time_field.grid(row=5, column=1, padx=10, pady=10)
    return_field.grid(row=6, column=1, padx=10, pady=10)

    projection_field.grid(row=10, column=1, padx=10, pady=10)


    # def print_selection():
    #     if (var1.get() == 1):
    #         l.config(text='I love Python ')
    #     else:
    #         l.config(text='I love both')
    checked = tkinter.IntVar()
    c1 = Checkbutton(root, onvalue=1, offvalue=0, variable=checked)
    c1.grid(row=8, column=1, pady=10)

    # Create a Submit Button and attached
    # to calculate_ci function
    button1 = Button(root, text="Submit", bg="cyan",
                     fg="black", command=calculate_return)

    # Create a Clear Button and attached
    # to clear_all function
    button2 = Button(root, text="Clear", bg="cyan",
                     fg="black", command=clear_all)

    # Create Help Button
    button3 = Button(root, text="Help", bg="cyan",
                     fg="black", command=help_button)

    button1.grid(row=9, column=1, pady=10)
    button2.grid(row=11, column=1, pady=10)
    button3.grid(row=12, column=1, pady=10)


    # Start the GUI
    root.mainloop()