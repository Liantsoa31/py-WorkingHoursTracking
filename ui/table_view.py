import tkinter as tk
from tkinter import ttk
from config.settings import TABLE_HEADERS
from services.date_service import get_month_key, get_month_label


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

        self.month_var = tk.StringVar()
        self.month_combo = ttk.Combobox(
            self,
            textvariable=self.month_var,
            state="readonly",
            width=20
        )
        self.month_combo.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

        self.month_combo.bind("<<ComboboxSelected>>", self.on_month_change)
        
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
        self.all_rows = rows
        self._build_months()
        self._refresh_table()

    def _build_months(self):
        months = {}

        for row in self.all_rows:
            date_str = row[0]
            key = get_month_key(date_str)
            label = get_month_label(date_str)
            months[key] = label

        self.months = months

        values = ["Tous les mois"] + list(months.values())
        self.month_combo["values"] = values

        if not self.month_var.get():
            self.month_combo.current(0)
    
    def on_month_change(self, event=None):
        self._refresh_table()

    def _refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        selected = self.month_var.get()

        for row in self.all_rows:
            if selected != "Tous les mois":
                date_str = row[0]
                key = get_month_key(date_str)

                if self.months.get(key) != selected:
                    continue

            self.table.insert("", tk.END, values=row)

