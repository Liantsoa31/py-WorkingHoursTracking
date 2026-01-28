import tkinter as tk
from ui.form_view import FormView
from ui.table_view import TableView
from tkinter import messagebox
from logic.controller import AppController


class App:
    def __init__(self):
        self.controller = AppController()

        self.root = tk.Tk()
        self.root.title("Enregistrement des heures de travail")
        self.root.geometry("700x450")

        self.create_views()
        self.refresh_table()

    def create_views(self):
        self.form_view = FormView(
            self.root,
            on_save_callback=self.on_save,
            delete_selection_callback=self.on_delete_selection,
            on_delete_callback=self.on_delete_all
        )
        self.form_view.pack(anchor="w", padx=15, pady=10)

        self.table_view = TableView(self.root)
        self.table_view.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def on_save(self, date, name, number):
        try:
            self.controller.save(date, name, number)
            messagebox.showinfo("Succès", "Données enregistrées")
            self.form_view.clear()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def on_delete_selection(self):
        selected_items = self.table_view.table.selection()
        if not selected_items:
            messagebox.showwarning("Attention", "Aucune ligne sélectionnée")
            return

        confirm = messagebox.askyesno(
            "Confirmation",
            f"Voulez-vous vraiment supprimer {len(selected_items)} ligne(s) ?"
        )
        if not confirm:
            return

        # Calcul des indices Excel pour chaque ligne sélectionnée
        excel_indices = [
            self.table_view.table.index(item) + 2  # +2 car header = ligne 1
            for item in selected_items
        ]

        # Supprimer les lignes dans l’ordre décroissant pour éviter les décalages
        for row_index in sorted(excel_indices, reverse=True):
            self.controller.delete_row(row_index)

        self.refresh_table()
        messagebox.showinfo("Succès", f"{len(selected_items)} ligne(s) supprimée(s)")

    def on_delete_all(self):
        self.controller.delete_all()
        self.refresh_table()
        messagebox.showinfo("Succès", "Toutes les données ont été supprimées")

    def refresh_table(self):
        data = self.controller.get_all_data()
        self.table_view.update_data(data)

    def run(self):
        self.root.mainloop()
