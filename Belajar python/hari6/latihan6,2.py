import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QLineEdit, QTableWidget, 
    QTableWidgetItem, QMessageBox
)

class Tugas:
    def _init_(self, id, judul, deskripsi):
        self.id = id
        self.judul = judul
        self.deskripsi = deskripsi
        self.status = "belum selesai"

    def to_dict(self):
        return {
            'id': self.id,
            'judul': self.judul,
            'deskripsi': self.deskripsi,
            'status': self.status
        }

class ManajemenTugas:
    def _init_(self):
        self.daftar_tugas = []
        self.load_from_file()

    def tambah_tugas(self, judul, deskripsi):
        id_tugas = len(self.daftar_tugas) + 1
        tugas = Tugas(id_tugas, judul, deskripsi)
        self.daftar_tugas.append(tugas)
        self.simpan_ke_file()

    def simpan_ke_file(self):
        with open('tugas.json', 'w') as file:
            json.dump([tugas.to_dict() for tugas in self.daftar_tugas], file)

    def load_from_file(self):
        try:
            with open('tugas.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    tugas = Tugas(item['id'], item['judul'], item['deskripsi'])
                    tugas.status = item['status']
                    self.daftar_tugas.append(tugas)
        except FileNotFoundError:
            pass

class App(QWidget):
    def _init_(self):
        super()._init_()
        self.manajemen_tugas = ManajemenTugas()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sistem Manajemen Tugas')

        layout = QVBoxLayout()

        # Input Tugas
        self.judul_input = QLineEdit(self)
        self.judul_input.setPlaceholderText('Judul Tugas')
        layout.addWidget(self.judul_input)

        self.deskripsi_input = QLineEdit(self)
        self.deskripsi_input.setPlaceholderText('Deskripsi Tugas')
        layout.addWidget(self.deskripsi_input)

        # Tombol Tambah Tugas
        self.tambah_button = QPushButton('Tambah Tugas', self)
        self.tambah_button.clicked.connect(self.tambah_tugas)
        layout.addWidget(self.tambah_button)

        # Tabel Tugas
        self.tabel = QTableWidget(self)
        self.tabel.setColumnCount(4)
        self.tabel.setHorizontalHeaderLabels(['ID', 'Judul', 'Deskripsi', 'Status'])
        layout.addWidget(self.tabel)

        # Tombol Hapus Tugas
        self.hapus_button = QPushButton('Hapus Tugas', self)
        self.hapus_button.clicked.connect(self.hapus_tugas)
        layout.addWidget(self.hapus_button)

        self.setLayout(layout)
        self.load_tugas()

    def load_tugas(self):
        self.tabel.setRowCount(0)
        for tugas in self.manajemen_tugas.daftar_tugas:
            row_position = self.tabel.rowCount()
            self.tabel.insertRow(row_position)
            self.tabel.setItem(row_position, 0, QTableWidgetItem(str(tugas.id)))
            self.tabel.setItem(row_position, 1, QTableWidgetItem(tugas.judul))
            self.tabel.setItem(row_position, 2, QTableWidgetItem(tugas.deskripsi))
            self.tabel.setItem(row_position, 3, QTableWidgetItem(tugas.status))

    def tambah_tugas(self):
        judul = self.judul_input.text()
        deskripsi = self.deskripsi_input.text()
        if judul and deskripsi:
            self.manajemen_tugas.tambah_tugas(judul, deskripsi)
            self.load_tugas()
            self.judul_input.clear()
            self.deskripsi_input.clear()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Judul dan Deskripsi tidak boleh kosong!')

    def hapus_tugas(self):
        selected_row = self.tabel.currentRow()
        if selected_row >= 0:
            del self.manajemen_tugas.daftar_tugas[selected_row]
            self.manajemen_tugas.simpan_ke_file()
            self.load_tugas()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Silakan pilih tugas yang ingin dihapus!')

if __name__ == '_main_':
    app = QApplication(sys.argv)
    window = App()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())