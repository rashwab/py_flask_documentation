import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QMessageBox
)

from collections import defaultdict


from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

tickets = defaultdict(dict)

BG_COLOR = "#cce7ff"
BTN_COLOR = "#81d4fa"
TEXT_COLOR = "#0d47a1"
FONT_FAMILY = "Comic Sans MS"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ticket System")
        self.setFixedSize(450, 500)

        central = QWidget()
        central.setStyleSheet(f"background-color: {BG_COLOR};")
        self.setCentralWidget(central)

        font_title = QFont(FONT_FAMILY, 16, QFont.Weight.Bold)
        font_label = QFont(FONT_FAMILY, 12, QFont.Weight.Bold)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QLabel(" Ticket System ")
        title.setFont(font_title)
        title.setStyleSheet(f"color: {TEXT_COLOR};")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        label_name = QLabel("Customer Name:")
        label_name.setFont(font_label)
        label_name.setStyleSheet(f"color: {TEXT_COLOR};")
        layout.addWidget(label_name)

        self.entry_name = QLineEdit()
        self.entry_name.setFont(font_label)
        layout.addWidget(self.entry_name)

        label_issue = QLabel("Issue Description:")
        label_issue.setFont(font_label)
        label_issue.setStyleSheet(f"color: {TEXT_COLOR};")
        layout.addWidget(label_issue)

        self.entry_issue = QLineEdit()
        self.entry_issue.setFont(font_label)
        layout.addWidget(self.entry_issue)

        self.btn_create = QPushButton("Create Ticket")
        self.btn_create.setFont(font_label)
        self.btn_create.setStyleSheet(
            f"background-color: {BTN_COLOR}; color: {TEXT_COLOR}; padding: 8px;"
        )
        self.btn_create.clicked.connect(self.create_ticket)
        layout.addWidget(self.btn_create)

        label_list = QLabel("All Tickets:")
        label_list.setFont(font_label)
        label_list.setStyleSheet(f"color: {TEXT_COLOR};")
        layout.addWidget(label_list)

        self.listbox_tickets = QListWidget()
        self.listbox_tickets.setFont(font_label)
        layout.addWidget(self.listbox_tickets)

        central.setLayout(layout)

    def create_ticket(self):
        customer_name = self.entry_name.text().strip()
        issue_description = self.entry_issue.text().strip()

        if not customer_name or not issue_description:
            QMessageBox.warning(self, "Input Error", "Please enter both name and issue description.")
            return

        ticket_id = f"ticket{len(tickets) + 1}"
        tickets[ticket_id] = {"customer": customer_name, "issue": issue_description}

        QMessageBox.information(self, "Success", f"Ticket {ticket_id} created!")
        self.entry_name.clear()
        self.entry_issue.clear()
        self.update_ticket_list()

    def update_ticket_list(self):
        self.listbox_tickets.clear()
        for ticket_id, info in tickets.items():
            self.listbox_tickets.addItem(f"{ticket_id}: {info['customer']} - {info['issue']}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
