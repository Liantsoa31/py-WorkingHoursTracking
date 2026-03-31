import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from config.settings import FORM_LABELS


class FormView(tk.Frame):
    def __init__(self, parent, on_save_callback, delete_selection_callback, on_delete_callback):
        super().__init__(parent)

        self.on_save_callback = on_save_callback
        self.delete_selection_callback = delete_selection_callback
        self.on_delete_callback = on_delete_callback
        self.create_widgets()

    def create_widgets(self):
        self.entries = {}

        for i, label in enumerate(FORM_LABELS):
            tk.Label(self, text=label).grid(row=i, column=0, padx=2, pady=2, sticky="w")

            if label.lower() == 'date':
                entry = DateEntry(self, width=22, date_pattern="dd-mm-yyyy", background="darkblue", foreground="white", borderwidth=2)
            else :
                entry = tk.Entry(self, width=25)

            entry.grid(row=i, column=1, padx=2, pady=2, sticky="w")

            self.entries[label] = entry

        button_frame = tk.Frame(self)
        button_frame.grid(row=len(FORM_LABELS), columnspan=2, pady=(10, 0))

        tk.Button(
            button_frame,
            text="Enregistrer",
            font=("Segoe UI", 10, "bold"),
            command=self.on_save
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            button_frame,
            text="Supprimer sélection",
            fg="white",
            bg="orange",
            font=("Segoe UI", 10, "bold"),
            command=self.on_delete_selection
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            button_frame,
            text="Supprimer tout",
            fg="white",
            bg="red",
            font=("Segoe UI", 10, "bold"),
            command=self.on_delete
        ).pack(side=tk.LEFT, padx=5)

    def on_save(self):
        data = [self.entries[label].get() for label in FORM_LABELS]
        self.on_save_callback(*data)

    def on_delete_selection(self):
        if hasattr(self, 'delete_selection_callback'):
            self.delete_selection_callback()

    def on_delete(self):
        confirm = messagebox.askyesno(
            "Confirmation",
            "Voulez-vous vraiment supprimer toutes les entrées ?"
        )
        if confirm:
            self.on_delete_callback()

    def clear(self):
        for label, entry in self.entries.items():
            if label == "Date": continue
            entry.delete(0, tk.END)
