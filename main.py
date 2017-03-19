# Created by Khoroshikh Arkadiy on 18.03.17.
#
# MIT Licence
import xlrd
import time
import os
from windows import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.abonent_index = 12  # номер столбца по умолчанию для Абонента
        self.duration = 7  # номер столбца по умолчанию для Продолжительности
        self.sh = {}
        self.info_rings = {}
        self.path_file = ''
        self.path_to_save = 'Result.txt'

        self.open_btn.clicked.connect(self.open_file)
        self.action_open.triggered.connect(self.open_file)
        self.action_exit.triggered.connect(lambda: exit(0))
        self.action_about.triggered.connect(self.about)
        self.start_bt.clicked.connect(self.run)
        self.statusbar.showMessage('© Khoroshikh Arkadiy 2017')
        self.progress_pg.setVisible(0)
        self.start_bt.setVisible(0)

    def read_xls(self):
        """
        Чтение xls файла
        """
        book = xlrd.open_workbook(self.path_file)
        self.sh = book.sheet_by_index(0)

    def get_index_attributes(self):
        """
        Получаем номера столбцов для Абонента и Продолжительности
        """
        for c_row in range(0, 250):
            keys = [self.sh.cell(c_row, col_index).value for col_index in range(self.sh.ncols)]
            if 'Абонент' in keys:
                self.abonent_index = keys.index('Абонент')
                self.duration = keys.index('Длительность')
                break

    def create_out_dict(self):
        """
        Записываем данные о кол-ве звонков и их продолжительности по каждому сотруднику в
        отельный словарь
        """
        self.start_bt.setDisabled(True)
        total_row = len(range(self.sh.nrows))

        for rx in range(self.sh.nrows):
            row_table = self.sh.row(rx)
            name_staff = row_table[self.abonent_index].value

            if name_staff != '' and name_staff != 'Абонент':
                time_ring_cell = row_table[self.duration].value
                t_ring = time.strptime(time_ring_cell, '%M:%S')

                if name_staff in self.info_rings:
                    self.info_rings[name_staff]['Количество звонков'] += 1
                    self.info_rings[name_staff]['Время(сек)'] += (t_ring[4] * 60) + t_ring[5]
                else:
                    self.info_rings[name_staff] = {}
                    self.info_rings[name_staff]['Количество звонков'] = 0
                    self.info_rings[name_staff]['Время(сек)'] = (t_ring[4] * 60) + t_ring[5]

            percent = rx * 100 / total_row
            self.progress_pg.setValue(percent)

    def save_to_out(self):
        self.progress_pg.setValue(100)
        file = open(self.path_to_save, 'w')
        for name, count in self.info_rings.items():
            text = '{} - {}\n'.format(name, count)
            print(text)
            file.write(text)
        file.close()

    def run(self):
        self.progress_pg.setVisible(1)
        self.read_xls()
        self.get_index_attributes()
        self.create_out_dict()
        self.save_to_out()

    def open_file(self):
        filters = 'Excel файлы (*.xls)'
        filename = QFileDialog.getOpenFileName(self, 'Открыть файл', os.path.expanduser('~'), filters)
        if filename[0]:
            self.file_name_le.setText(filename[0])
            self.path_file = filename[0]
            self.start_bt.setVisible(1)

    def about(self):
        QMessageBox.question(self, 'О программе', 'Данная программа написана для парсинга Excel файлов.', QMessageBox.Ok)



if __name__ == '__main__':
    app = QApplication([])
    w = App()
    w.show()
    app.exec_()
