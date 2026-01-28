from openpyxl import Workbook, load_workbook
from config.settings import EXCEL_PATH, TABLE_HEADERS
import os


class ExcelService:

    @staticmethod
    def save(date, name, number):
        if os.path.exists(EXCEL_PATH):
            wb = load_workbook(EXCEL_PATH)
            ws = wb.active
        else:
            wb = Workbook()
            ws = wb.active
            ws.append(TABLE_HEADERS)

        ws.append([date, name, int(number)])
        wb.save(EXCEL_PATH)

    @staticmethod
    def get_all():
        if not os.path.exists(EXCEL_PATH):
            return []

        wb = load_workbook(EXCEL_PATH)
        ws = wb.active

        data = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            data.append(row)

        return data

    @staticmethod
    def delete_row(row_index):
        """
        Supprime une ligne spécifique dans le fichier Excel.
        row_index : ligne dans Excel (1 = header)
        """
        if not os.path.exists(EXCEL_PATH):
            return

        wb = load_workbook(EXCEL_PATH)
        ws = wb.active

        # ligne 1 = header, ligne_index >= 2
        if row_index < 2 or row_index > ws.max_row:
            return

        ws.delete_rows(row_index)
        wb.save(EXCEL_PATH)

    @staticmethod
    def delete_all():
        if not os.path.exists(EXCEL_PATH):
            return

        wb = load_workbook(EXCEL_PATH)
        ws = wb.active

        ws.delete_rows(2, ws.max_row)  # garde la ligne d’en-tête
        wb.save(EXCEL_PATH)