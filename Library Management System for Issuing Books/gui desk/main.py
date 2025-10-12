import datetime
import customtkinter
from PIL import Image
from test import (
    validate_member_id, validate_book_isbn, validate_issue_date,
    validate_loan_period, save_to_file
)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("850x600")
app.title("Library Management System")

header_frame = customtkinter.CTkFrame(app, corner_radius=15)
header_frame.pack(fill="x", padx=20, pady=(15, 10))

title = customtkinter.CTkLabel(
    header_frame, 
    text="Library Management System",
    font=("Segoe UI", 28, "bold")
)
title.pack(pady=10)

main_frame = customtkinter.CTkFrame(app, corner_radius=15)
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

entry_frame = customtkinter.CTkFrame(main_frame, fg_color="transparent")
entry_frame.pack(pady=20)

member_id_label = customtkinter.CTkLabel(entry_frame, text="6-digit Member ID", font=("Segoe UI", 14))
member_id_label.grid(row=0, column=0, padx=10, pady=(0,5))
member_id_entry = customtkinter.CTkEntry(entry_frame, placeholder_text="Enter 6-digit Member ID", width=300, height=40, corner_radius=8)
member_id_entry.grid(row=1, column=0, padx=10, pady=10)

book_isbn_label = customtkinter.CTkLabel(entry_frame, text="Book ISBN", font=("Segoe UI", 14))
book_isbn_label.grid(row=0, column=1, padx=10, pady=(0,5))
book_isbn_entry = customtkinter.CTkEntry(entry_frame, placeholder_text="Enter Book ISBN (978-...)", width=300, height=40, corner_radius=8)
book_isbn_entry.grid(row=1, column=1, padx=10, pady=10)

issue_date_label = customtkinter.CTkLabel(entry_frame, text="Issue Date", font=("Segoe UI", 14))
issue_date_label.grid(row=2, column=0, padx=10, pady=(10,5))
issue_date_entry = customtkinter.CTkEntry(entry_frame, placeholder_text="Enter Issue Date (YYYY-MM-DD)", width=300, height=40, corner_radius=8)
issue_date_entry.grid(row=3, column=0, padx=10, pady=10)

loan_period_label = customtkinter.CTkLabel(entry_frame, text="Loan Period", font=("Segoe UI", 14))
loan_period_label.grid(row=2, column=1, padx=10, pady=(10,5))
loan_period_entry = customtkinter.CTkEntry(entry_frame, placeholder_text="Enter Loan Period (7–30 days)", width=300, height=40, corner_radius=8)
loan_period_entry.grid(row=3, column=1, padx=10, pady=10)

status_label = customtkinter.CTkLabel(main_frame, text="", font=("Segoe UI", 13))
status_label.pack(pady=10)

button_frame = customtkinter.CTkFrame(main_frame, fg_color="transparent")
button_frame.pack(pady=10)

def set_status(message, success=True):
    color = "#00cc66" if success else "#ff3333"
    status_label.configure(text=message, text_color=color)

def clear_entries():
    member_id_entry.delete(0, 'end')
    book_isbn_entry.delete(0, 'end')
    issue_date_entry.delete(0, 'end')
    loan_period_entry.delete(0, 'end')
    set_status("Fields cleared.", True)

def save_record():
    member_id = member_id_entry.get()
    book_isbn = book_isbn_entry.get()
    issue_date = issue_date_entry.get()
    loan_period = loan_period_entry.get()

    if not validate_member_id(member_id):
        set_status("Invalid Member ID.", False)
        return
    if not validate_book_isbn(book_isbn):
        set_status("Invalid Book ISBN.", False)
        return
    if not validate_issue_date(issue_date):
        set_status("Invalid Issue Date.", False)
        return
    if not validate_loan_period(loan_period):
        set_status("Invalid Loan Period.", False)
        return

    record = f"{member_id},{book_isbn},{issue_date},{loan_period}"
    save_to_file(record)
    set_status("Record saved successfully!")
    clear_entries()

def show_records():
    try:
        with open("issued_books.txt", "r") as file:
            records = file.readlines()
            if not records:
                set_status("No records found.", False)
                return
            records_text = "\n".join(records)
            record_window = customtkinter.CTkToplevel(app)
            record_window.title("Issued Books")
            record_window.geometry("650x400")
            title = customtkinter.CTkLabel(record_window, text="Issued Books", font=("Segoe UI", 20, "bold"))
            title.pack(pady=10)
            textbox = customtkinter.CTkTextbox(record_window, width=600, height=320, corner_radius=12)
            textbox.pack(padx=20, pady=10)
            textbox.insert("0.0", records_text)
            textbox.configure(state="disabled")
    except FileNotFoundError:
        set_status("No records file found.", False)

save_button = customtkinter.CTkButton(button_frame, text="Save Record", width=150, height=40, corner_radius=10, command=save_record)
clear_button = customtkinter.CTkButton(button_frame, text="Clear Fields", width=150, height=40, corner_radius=10, fg_color="#666666", hover_color="#555555", command=clear_entries)
view_button = customtkinter.CTkButton(button_frame, text="View Records", width=150, height=40, corner_radius=10, command=show_records)

save_button.grid(row=0, column=0, padx=10)
clear_button.grid(row=0, column=1, padx=10)
view_button.grid(row=0, column=2, padx=10)

footer_label = customtkinter.CTkLabel(
    app, 
    text="Test1",
    font=("Segoe UI", 11),
    text_color="gray"
)
footer_label.pack(side="bottom", pady=8)

app.mainloop()

