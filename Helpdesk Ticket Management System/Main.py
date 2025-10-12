import tkinter as tk
from tkinter import messagebox
from collections import defaultdict

tickets = defaultdict(dict)

BG_COLOR = "#cce7ff"
BTN_COLOR = "#81d4fa"
TEXT_COLOR = "#0d47a1"
FONT = ("Comic Sans MS", 12, "bold")

root = tk.Tk()
root.title("Ticket System")
root.geometry("450x500")
root.configure(bg=BG_COLOR)

def create_ticket():
    customer_name = entry_name.get().strip()
    issue_description = entry_issue.get().strip()

    if not customer_name or not issue_description:
        messagebox.showwarning("Input Error", "Please enter both name and issue description.")
        return

    ticket_id = f"ticket{len(tickets)+1}"
    tickets[ticket_id] = {"customer": customer_name, "issue": issue_description}

    messagebox.showinfo("Success", f"Ticket {ticket_id} created!")
    entry_name.delete(0, tk.END)
    entry_issue.delete(0, tk.END)
    update_ticket_list()

def update_ticket_list():
    listbox_tickets.delete(0, tk.END)
    for ticket_id, info in tickets.items():
        listbox_tickets.insert(tk.END, f"{ticket_id}: {info['customer']} - {info['issue']}")

title = tk.Label(root, text=" Ticket System ", bg=BG_COLOR, fg=TEXT_COLOR, font=("Comic Sans MS", 16, "bold"))
title.pack(pady=10)

label_name = tk.Label(root, text="Customer Name:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=40, font=FONT)
entry_name.pack(pady=5)

label_issue = tk.Label(root, text="Issue Description:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
label_issue.pack(pady=5)
entry_issue = tk.Entry(root, width=40, font=FONT)
entry_issue.pack(pady=5)

btn_create = tk.Button(root, text="Create Ticket", bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT, command=create_ticket)
btn_create.pack(pady=15)

label_list = tk.Label(root, text="All Tickets:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
label_list.pack(pady=5)

listbox_tickets = tk.Listbox(root, width=50, font=FONT)
listbox_tickets.pack(pady=5)

root.mainloop()
