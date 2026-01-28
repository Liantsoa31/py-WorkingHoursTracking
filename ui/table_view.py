import tkinter as tk
from tkinter import ttk
from config.settings import TABLE_HEADERS


class TableView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_style()
        self.create_widgets()
    
    def create_style(self):
        style = ttk.Style()

        # Important pour Windows
        style.theme_use("default")

        style.configure(
            "Custom.Treeview.Heading",
            background="#d9d9d9",   # gris clair
            foreground="black",
            font=("Segoe UI", 10, "bold"),
            relief="solid",
            padding=(5, 5)
        )

        style.configure(
            "Custom.Treeview",
            rowheight=25
        )

        style.map(
            "Custom.Treeview.Heading",
            background=[("active", "#cfcfcf")]
        )

    def create_widgets(self):
        self.table = ttk.Treeview(
            self,
            columns=[header.lower() for header in TABLE_HEADERS],
            show="headings",
            style="Custom.Treeview"
        )

        for header in TABLE_HEADERS:
            self.table.heading(header.lower(), text=header, anchor="w")
            self.table.column(header.lower(), anchor="w", width=180)

        self.table.pack(fill=tk.BOTH, expand=True)

    def update_data(self, rows):
        for row in self.table.get_children():
            self.table.delete(row)

        for row in rows:
            self.table.insert("", tk.END, values=row)
