from services.excel_service import ExcelService
from logic.validator import validate_data


class AppController:

    def save(self, date, name, number):
        validate_data(date, name, number)
        ExcelService.save(date, name, number)

    def get_all_data(self):
        return ExcelService.get_all()
    
    def delete_row(self, excel_row_index):
        ExcelService.delete_row(excel_row_index)

    def delete_all(self):
        ExcelService.delete_all()