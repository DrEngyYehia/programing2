from tkinter import *
from tkinter import messagebox

wind = Tk()
wind.title("Bank Misr loan application")
wind.geometry("1920x1080")
wind.configure(bg = "black")
wind.configure(bd = 20)

def calculate_and_plan_loan():
    job = job_entry.get() 
    loan_amount = int(amount_entry.get())
    years = int(years_entry.get())
    if years >= 1 and years <= 7:
        interest_rate = get_interest_rate(years)
        plan_loan(loan_amount, interest_rate, years)
    else:
        messagebox.showerror("Error", "No. of years must be between 1 and 7")

def get_interest_rate(years):
    interest_rates = {1: 13.76, 2: 13.74, 3: 14.06, 4: 14.46, 5: 14.87, 6: 15.29, 7: 15.71}
    return interest_rates.get(years, 0)

def plan_loan(loan_amount, interest_rate, years):
    interest_in_one_year = (loan_amount * (interest_rate / 100))
    total_interests = (interest_in_one_year * years)
    total_loan = (loan_amount + total_interests)
    monthly_payment = (total_loan / (years * 12))
    output_label1.config(text=f"Interest per year = {interest_in_one_year} EGP", fg="white")
    output_label2.config(text=f"Total interest = {total_interests} EGP", fg="white")
    output_label3.config(text=f"Total loan= {total_loan} EGP", fg="white")
    output_label4.config(text=f"Monthly payment = {monthly_payment} EGP", fg="white")

def exit_program():
    wind.quit()

def clear_entries():
    amount_entry.delete(0, 'end')
    years_entry.delete(0, 'end')

frame_top = Frame(wind, bg="black")
frame_top.pack(side=TOP)
frame_bottom = Frame(wind, bg="black", bd=30)
frame_bottom.pack(side=BOTTOM)

logo = PhotoImage(file="Assgnment2\image.png")
label_logo = Label(frame_top, image=logo, bg="black")
label_logo.pack()

label_job = Label(frame_top, text="Job name:", bg="black", fg="white")
label_job.pack()
job_entry = Entry(frame_top, bd=4, fg="black", bg="white", width=30)
job_entry.pack()

label_amount = Label(frame_top, text="Loan amount :", bg="black", fg="white")
label_amount.pack()
amount_entry = Entry(frame_top, bd=4 , fg="black", bg="white", width=30)
amount_entry.pack()

label_years = Label(frame_top, text="Number of years  :", bg="black", fg="white")
label_years.pack()
years_entry = Entry(frame_top, bd=4, fg="black", bg="white", width=30 )
years_entry.pack()

button_calculate = Button(frame_top, text="Calculate", command=calculate_and_plan_loan, bg="blue", fg="white", width=10)
button_calculate.pack()
button_exit = Button(frame_top, text="Exit", command=exit_program, bg="blue", fg="white",  width=10)
button_exit.pack()
button_clear = Button(frame_top, text="Clear", command=clear_entries, bg="blue", fg="white",  width=10)
button_clear.pack()

output_label1 = Label(frame_bottom, bg="black", font=("Arial", 25))
output_label1.pack()
output_label2 = Label(frame_bottom, bg="black", font=("Arial", 25))
output_label2.pack()
output_label3 = Label(frame_bottom, bg="black", font=("Arial", 25))
output_label3.pack()
output_label4 = Label(frame_bottom, bg="black", font=("Arial", 25))
output_label4.pack()

wind.mainloop()