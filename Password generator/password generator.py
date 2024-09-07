import tkinter as tk
from tkinter import messagebox
import random


def generate_password():
    """Generate a random password and display it in the entry field."""
    try:
        # Get the desired password length from the spinbox
        password_length = int(password_length_spinbox.get())
        
        # Generate password using ASCII characters from 33 to 126
        password = ''.join(chr(random.randint(33, 126)) for _ in range(password_length))
        
        # Clear the entry field and insert the new password
        password_display_entry.delete(0, tk.END)
        password_display_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

# Set up the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("550x550")
window.config(bg="#E3FDFD")  # Light pastel blue background

# Create and position the main frame
main_frame = tk.Frame(window, bg="#E3FDFD", padx=20, pady=20)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add title label
title_label = tk.Label(main_frame, text="Password Generator", font=("Arial", 20, "bold"), 
                       bg="#E3FDFD", fg="#71C9CE")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Add label and spinbox for password length
length_label = tk.Label(main_frame, text="Password length:", font=("Arial", 12), 
                        bg="#E3FDFD", fg="#71C9CE")
length_label.grid(row=1, column=0, sticky="e", pady=10)

password_length_spinbox = tk.Spinbox(main_frame, from_=8, to=32, width=5, font=("Arial", 12))
password_length_spinbox.grid(row=1, column=1, sticky="w", pady=10)

# Add entry field to display generated password
password_display_entry = tk.Entry(main_frame, width=40, font=("Arial", 12), bg="#CBF1F5")
password_display_entry.grid(row=2, column=0, columnspan=2, pady=20)

# Add button to generate password
generate_button = tk.Button(main_frame, text="Generate Password", width=20, command=generate_password, 
                            bg="#A6E3E9", fg="white", font=("Arial", 12, "bold"),
                            activebackground="#71C9CE", activeforeground="white", 
                            relief=tk.FLAT, cursor="hand2")
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main event loop
window.mainloop()