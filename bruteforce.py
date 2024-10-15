from tkinter import *
from tkinter import messagebox


attempts = 0
correct_password = "12345"  

def check_password():
    global attempts
    password = entry.get()
    
    if password == correct_password:
        messagebox.showinfo("Success", "Access Granted!")
        attempts = 0  
    else:
        attempts += 1
        messagebox.showwarning("Error", f"Incorrect Password! Attempt {attempts}/5")
        
        if attempts >= 5:
            messagebox.showerror("Locked Out", "Too many incorrect attempts! Try again later.")
            attempts = 0  


root = Tk()
root.title("Brute Force Protection")

Label(root, text="Enter Password:").pack(pady=10)

entry = Entry(root, show="*")
entry.pack(pady=10)

Button(root, text="Submit", command=check_password).pack(pady=10)

root.mainloop()
