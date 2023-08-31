from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog, QVBoxLayout,QLabel
from PyQt5.QtWidgets import QApplication
import threading
from os import path, getcwd
from random import randint
import traceback
import clipboard
import math
from PyQt5.QtCore import QTimer, QDateTime

class What_to_code(QDialog):
    my_signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(What_to_code, self).__init__()
        self.setWindowTitle('Текст или файл?')
        self.resize(400, 30)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 380, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText("Выберите, что надо шифровать")

        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Текст")
        self.comboBox.addItem("Файл")
        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Выбрать")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.choice_type)

    def choice_type(self):
        self.my_signal.emit(self.comboBox.currentText())
        self.accept()

class Bin_Hex(QDialog):
    def __init__(self):
        super(Bin_Hex, self).__init__()
        self.setWindowTitle('Binary <-> Hexadecimal')
        self.resize(400, 120)

        self.input = QtWidgets.QLineEdit(self)
        self.input.setGeometry(QtCore.QRect(0, 0, 400, 30))
        self.input.setReadOnly(False)
        self.input.setObjectName("input")

        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 30, 200, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setText("Hex to bin")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 30, 200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Bin to hex")

        self.output = QtWidgets.QLineEdit(self)
        self.output.setGeometry(QtCore.QRect(0, 60, 400, 30))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 90, 400, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Скопировать")

        self.pushButton_1.clicked.connect(self.hex_to_bin)
        self.pushButton_2.clicked.connect(self.bin_to_hex)
        self.pushButton_3.clicked.connect(self.copier)

    def hex_to_bin(self):
        hex = self.input.text()
        h_b = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'a': '1010',
            'b': '1011',
            'c': '1100',
            'd': '1101',
            'e': '1110',
            'f': '1111'
        }

        binary_num = ""
        for digit in hex:
            binary_num += h_b[digit]
        self.output.setText(binary_num)

    def bin_to_hex(self):
        bin = self.input.text()
        bytes_grouped = [bin[i:i + 4] for i in range(0, len(bin), 4)]
        final = ""
        for i in range(len(bytes_grouped)):
            final += str(hex(int(bytes_grouped[i], 2)))[2:]
        self.output.setText(final)

    def copier(self):
        clipboard.copy(self.output.text())

class What_mode(QDialog):
    my_signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(What_mode, self).__init__()
        self.setWindowTitle('Режим шифрования')
        self.resize(600, 30)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 580, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText("Выберите режим шифрования")

        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Режим электронной кодовой книги")
        self.comboBox.addItem("Режим сцепления блоков шифротекста")
        self.comboBox.addItem("Режим обратной связи по шифротексту")
        self.comboBox.addItem("Режим обратной связи по выходу")
        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Выбрать")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.choice_mode)

    def choice_mode(self):
        self.my_signal.emit(self.comboBox.currentText())
        self.accept()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.temp_encoding = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸ0123456789"
        self.key = ""
        self.vector = ""
        self.crypt_file_name = ""
        self.text_from_file = ""
        self.type = ""
        self.mode = ""
        self.extra_bytes = 0
        self.stop = False
        self.progress = 0
        self.progress_item = "🟩"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 0, 380, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.key_state = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.key_state.setReadOnly(True)
        self.key_state.setObjectName("key_state")
        self.key_state.setText("Загрузите или сгенерируйте ключ")
        self.verticalLayout.addWidget(self.key_state)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.key_gen_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.key_gen_button.setObjectName("key_gen_button")
        self.horizontalLayout.addWidget(self.key_gen_button)
        self.key_load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.key_load_button.setObjectName("key_load_button")
        self.horizontalLayout.addWidget(self.key_load_button)
        self.key_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.key_save_button.setObjectName("key_save_button")
        self.horizontalLayout.addWidget(self.key_save_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(560, 80, 380, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vector_state = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.vector_state.setReadOnly(True)
        self.vector_state.setText("Загрузите или сгенерируйте вектор инициализации")
        self.vector_state.setObjectName("vector_state")
        self.verticalLayout_2.addWidget(self.vector_state)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vector_gen_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.vector_gen_button.setObjectName("vector_gen_button")
        self.horizontalLayout_2.addWidget(self.vector_gen_button)
        self.vector_load_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.vector_load_button.setObjectName("vector_load_button")
        self.horizontalLayout_2.addWidget(self.vector_load_button)
        self.vector_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.vector_save_button.setObjectName("vector_save_button")
        self.horizontalLayout_2.addWidget(self.vector_save_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.input_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(0, 0, 551, 161))
        self.input_text.setReadOnly(False)
        self.input_text.setObjectName("input_text")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(560, 160, 380, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input_file_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.input_file_button.setObjectName("input_file_button")
        self.horizontalLayout_3.addWidget(self.input_file_button)
        self.input_file_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.input_file_name.setReadOnly(True)
        self.input_file_name.setObjectName("input_file_name")
        self.horizontalLayout_3.addWidget(self.input_file_name)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 160, 551, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.encode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.encode_button.setObjectName("encode_button")
        self.horizontalLayout_4.addWidget(self.encode_button)
        self.decode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.decode_button.setObjectName("decode_button")
        self.horizontalLayout_4.addWidget(self.decode_button)
        self.changer_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.changer_button.setObjectName("changer_button")
        self.changer_button.setText("Bin/Hex")
        self.horizontalLayout_4.addWidget(self.changer_button)
        self.up_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.up_button.setObjectName("up_button")
        self.horizontalLayout_4.addWidget(self.up_button)
        self.clear_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_4.addWidget(self.clear_button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(770, 197, 150, 30))
        self.time_label.setText("Время выполнения:")

        self.time_label = QLabel("00:00:00", self.centralwidget)
        self.time_label.move(890, 205)

        self.process_label = QtWidgets.QLabel(self.centralwidget)
        self.process_label.setGeometry(QtCore.QRect(919, 230, 200, 30))
        self.process_label.setText("0%")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 230, 915, 30))
        self.lineEdit.setText("")

        self.output_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(0, 260, 940, 191))
        self.output_text.setObjectName("output_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.up_button.clicked.connect(self.up)
        self.clear_button.clicked.connect(self.clear)
        self.changer_button.clicked.connect(self.changer)
        self.key_gen_button.clicked.connect(lambda: self.generator(7))
        self.key_save_button.clicked.connect(lambda: self.save(7))
        self.key_load_button.clicked.connect(lambda: self.load(7))

        self.vector_gen_button.clicked.connect(lambda: self.generator(8))
        self.vector_save_button.clicked.connect(lambda: self.save(8))
        self.vector_load_button.clicked.connect(lambda: self.load(8))

        self.encode_button.clicked.connect(lambda: self.code("encode"))
        self.decode_button.clicked.connect(lambda: self.code("decode"))
        self.input_file_button.clicked.connect(self.select_file)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changer(self):
        self.w3 = Bin_Hex()
        self.w3.show()

    def update_time(self):
        current_time = QDateTime.currentDateTime()
        elapsed_time = self.start_time.secsTo(current_time)
        time_string = QDateTime.fromTime_t(elapsed_time).toUTC().toString('hh:mm:ss')

        self.time_label.setText(time_string)

    def code(self, param):
        try:
            self.progress = 0
            self.progress_item = "🟩"
            if param == "encode":
                self.extra_bytes = 0
            if (self.input_text.toPlainText() == "" and self.text_from_file == ""):
                self.error_input("Введите текст или выберите файл")
                return

            if (self.input_text.toPlainText() != "" and self.text_from_file != ""):
                self.what_to_code()

            if (self.input_text.toPlainText() == "" and self.text_from_file != ""):
                self.type = "Файл"

            if (self.input_text.toPlainText() != "" and self.text_from_file == ""):
                self.type = "Текст"

            if self.key == "":
                self.error_input("Введите ключ")
                return

            self.what_mode()
            self.bytes_input = ""
            if self.type == "Текст":
                text = self.input_text.toPlainText()
                if param == "encode":
                    decimal_list = self.utf8_to_decimal(text)
                    for i in range(len(decimal_list)):
                        self.bytes_input += self.dec_to_bin(decimal_list[i])

                else:
                    decimal_list = self.temp_encoding_to_decimal(text)
                    for i in range(len(decimal_list)):
                        self.bytes_input += self.dec_to_bin(decimal_list[i])
                print(decimal_list)
                print(self.bytes_input)
            else:
                self.bytes_input = "".join(list(map(lambda x: bin(int(x))[2:].zfill(8), self.text_from_file)))

            bytes_grouped = [self.bytes_input[i:i+64] for i in range(0, len(self.bytes_input), 64)]
            print(len(bytes_grouped))
            print(bytes_grouped)
            self.stop = False
            self.final_bytes = []

            self.start_time = QDateTime.currentDateTime()
            self.timer.start(1000)

            if self.mode == "Режим электронной кодовой книги":
                self.thread = threading.Thread(target=self.ecb, args=(bytes_grouped, param))
                self.thread.start()
                while self.thread.is_alive():
                    QApplication.processEvents(QEventLoop.AllEvents, 100)

            else:
                if len(self.vector) == 0:
                    self.error_input("Сначала введите вектор инициализации")
                    return

            if self.mode == "Режим сцепления блоков шифротекста":
                self.thread = threading.Thread(target=self.cbc, args=(bytes_grouped, param))
                self.thread.start()
                while self.thread.is_alive():
                    QApplication.processEvents(QEventLoop.AllEvents, 100)

            if self.mode == "Режим обратной связи по шифротексту":
                self.thread = threading.Thread(target=self.cfb, args=(bytes_grouped, param))
                self.thread.start()
                while self.thread.is_alive():
                    QApplication.processEvents(QEventLoop.AllEvents, 100)

            if self.mode == "Режим обратной связи по выходу":
                self.thread = threading.Thread(target=self.ofb, args=(bytes_grouped, param))
                self.thread.start()
                while self.thread.is_alive():
                    QApplication.processEvents(QEventLoop.AllEvents, 100)

            if self.stop == True:
                self.error_input("Длина сообщения в битах должна быть кратна 64")
                return

            self.timer.stop()

            bytes_str = ''.join(self.final_bytes)

            bytes_grouped = [bytes_str[i:i + 8] for i in range(0, len(bytes_str), 8)]
            decimal_list = []
            texter = ""
            for i in range(len(bytes_grouped)):
                decimal_list.append(int(bytes_grouped[i], 2))

            if self.type == "Текст":
                if param == "encode":
                    texter = self.decimal_to_temp_encoding(decimal_list)
                else:
                    texter = self.decimal_to_utf8(decimal_list)

                self.output_text.setText(texter)
            else:
                temp_bytes = bytes(decimal_list)

                file_type = "зашифрованный"
                if param == "decode":
                    file_type = "расшифрованный"

                file_name = ""
                file_extension = ""
                dot_pos = 0
                check = False
                for i in range(len(self.crypt_file_name) - 1, 0, - 1):
                    if check == False:
                        if self.crypt_file_name[i] == ".":
                            dot_pos = i
                            file_extension = self.crypt_file_name[i:]
                            check = True
                    if check == True:
                        if self.crypt_file_name[i] == "/":
                            file_name = self.crypt_file_name[i:dot_pos]
                            break

                file_name = file_name.replace(" (зашифрованный)", "")
                file_name = file_name.replace(" (расшифрованный)", "")
                if param == "encode":
                    file_name += " (зашифрованный)"
                else:
                    file_name += " (расшифрованный)"
                cwd = getcwd()[2:].replace('\\', '/')
                file = QFileDialog.getSaveFileName(None, f"Сохранить {file_type} файл",
                                                   f"{cwd}/файлы/{file_name}",
                                                   f"(*{file_extension});;Все файлы (*)")[0]
                if file:
                    with open(file, 'wb') as f:
                        f.write(temp_bytes)
        except:
            traceback.print_exc()


    def xor_methods(self, bytes_prev, bytes_curr):
        output = ''.join(map(lambda x, y: str(int(x) ^ int(y)), bytes_prev, bytes_curr))
        return output

    def reverse(self, bytes_temp):
        final_bytes = list(reversed(bytes_temp))
        return final_bytes

    def cfb(self, bytes_grouped, param):
        if param == "encode":
            while len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.extra_bytes += 1
                bytes_grouped[len(bytes_grouped) - 1] += '0'

        else:
            if len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.stop = True
                return

        self.final_bytes = []
        keys = []
        keys.append(self.des(self.vector, "encode"))
        for i in range(len(bytes_grouped)):
            self.final_bytes.append(self.xor_methods(bytes_grouped[i], keys[i]))

            if i % math.floor((len(bytes_grouped) / 100)) == 0 and self.progress < 100:
                self.progress += 1
                self.process_label.setText(str(self.progress) + "%")
            if i % math.floor((len(bytes_grouped) // 50)) == 0 and self.progress < 100:
                self.progress_item += "🟩"
                self.lineEdit.setText(self.progress_item)

            if param == "encode":
                keys.append(self.des(self.final_bytes[i], "encode"))
            else:
                keys.append(self.des(bytes_grouped[i], "encode"))

        if param == "decode":
            if self.extra_bytes != 0:
                self.final_bytes[len(self.final_bytes) - 1] = self.final_bytes[len(self.final_bytes) - 1][:-self.extra_bytes]
        return self.final_bytes

    def ofb(self, bytes_grouped, param):
        if param == "encode":
            while len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.extra_bytes += 1
                bytes_grouped[len(bytes_grouped) - 1] += '0'

        else:
            if len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.stop = True
                return

        self.final_bytes = []
        keys = []
        keys.append(self.des(self.vector, "encode"))
        for i in range(len(bytes_grouped)):
            self.final_bytes.append(self.xor_methods(bytes_grouped[i], keys[i]))
            keys.append(self.des(keys[i], "encode"))
            if i % math.floor((len(bytes_grouped) / 100)) == 0 and self.progress < 100:
                self.progress += 1
                self.process_label.setText(str(self.progress) + "%")
            if i % math.floor((len(bytes_grouped) // 50)) == 0 and self.progress < 100:
                self.progress_item += "🟩"
                self.lineEdit.setText(self.progress_item)

        if param == "decode":
            if self.extra_bytes != 0:
                self.final_bytes[len(self.final_bytes) - 1] = self.final_bytes[len(self.final_bytes) - 1][:-self.extra_bytes]
        return self.final_bytes

    def cbc(self, bytes_grouped, param):
        if param == "encode":
            while len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.extra_bytes += 1
                bytes_grouped[len(bytes_grouped) - 1] += '0'

        else:
            if len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.stop = True
                return

        self.final_bytes = []
        if param == "encode":
            bytes_grouped[0] = self.xor_methods(bytes_grouped[0], self.vector)
            self.final_bytes.append(self.des(bytes_grouped[0], param))
            for i in range(1, len(bytes_grouped)):
                bytes_grouped[i] = self.xor_methods(bytes_grouped[i], self.final_bytes[i-1])
                self.final_bytes.append(self.des(bytes_grouped[i], param))
                if i % math.floor((len(bytes_grouped) / 100)) == 0 and self.progress < 100:
                    self.progress += 1
                    self.process_label.setText(str(self.progress) + "%")
                if i % math.floor((len(bytes_grouped) // 50)) == 0 and self.progress < 100:
                    self.progress_item += "🟩"
                    self.lineEdit.setText(self.progress_item)

        else:
            for i in range(len(bytes_grouped)-1, 0, -1):
                self.final_bytes.append(self.xor_methods(self.des(bytes_grouped[i], param), bytes_grouped[i - 1]))
                if i % math.floor((len(bytes_grouped) / 100)) == 0 and self.progress < 100:
                    self.progress += 1
                    self.process_label.setText(str(self.progress) + "%")
                if i % math.floor((len(bytes_grouped) // 50)) == 0 and self.progress < 100:
                    self.progress_item += "🟩"
                    self.lineEdit.setText(self.progress_item)

            self.final_bytes.append(self.xor_methods(self.des(bytes_grouped[0], param), self.vector))

        if param == "decode":
            self.final_bytes = self.reverse(self.final_bytes)
            if self.extra_bytes != 0:
                self.final_bytes[len(self.final_bytes) - 1] = self.final_bytes[len(self.final_bytes) - 1][:-self.extra_bytes]
        return self.final_bytes

    def ecb(self, bytes_grouped, param):
        if param == "encode":
            while len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.extra_bytes += 1
                bytes_grouped[len(bytes_grouped) - 1] += '0'

        else:
            if len(bytes_grouped[len(bytes_grouped) - 1]) != 64:
                self.stop = True
                return
        print(bytes_grouped)
        self.final_bytes = []
        for i in range(len(bytes_grouped)):
            self.final_bytes.append(self.des(bytes_grouped[i], param))
            if (len(bytes_grouped) >= 100):
                if i % math.floor((len(bytes_grouped) / 100)) == 0 and self.progress < 100:
                    self.progress += 1
                    self.process_label.setText(str(self.progress) + "%")
                if i % math.floor((len(bytes_grouped) // 50)) == 0 and self.progress < 100:
                    self.progress_item += "🟩"
                    self.lineEdit.setText(self.progress_item)

        if param == "decode":
            if self.extra_bytes != 0:
                self.final_bytes[len(self.final_bytes) - 1] = self.final_bytes[len(self.final_bytes) - 1][:-self.extra_bytes]
        return self.final_bytes

    def des(self, bytes_input, param):
        IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
              62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
              57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
              61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

        bytes_after_ip = ""
        for i in IP:
            bytes_after_ip += bytes_input[i - 1]

        if param == "encode":
            for j in range(16):
                key = self.keys_generator(self.key, j)
                bytes_after_ip = self.cycle(bytes_after_ip, key)
        else:
            for j in range(15, -1, -1):
                key = self.keys_generator(self.key, j)
                bytes_after_ip = self.cycle(bytes_after_ip, key)
        bytes_after_ip = bytes_after_ip[32:] + bytes_after_ip[:32]
        bytes_after_encryption = bytes_after_ip

        IP_inv = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]

        final_bytes = ""
        for j in IP_inv:
            final_bytes += bytes_after_encryption[j - 1]
        return final_bytes

    def cycle(self, bytes_input, key):
        left_part = bytes_input[:32]
        right_part = bytes_input[32:]
        right_part_new = self.Feistel_func(right_part, key)
        left_part = self.xor_parts(left_part, right_part_new)
        bytes_output = right_part + left_part
        return bytes_output

    def xor_parts(self, left_part, right_part):
        output = ''.join(map(lambda x, y: str(int(x) ^ int(y)), left_part, right_part))
        return output

    def Feistel_func(self,right_part, key):
        right_part = self.E_extension(right_part)
        right_part = self.xor(right_part, key)
        right_part = self.transformations(right_part)
        right_part = self.P(right_part)
        return right_part

    def E_extension(self, right_part):
        e_table = [32, 1, 2, 3, 4, 5,
                   4, 5, 6, 7, 8, 9,
                   8, 9, 10, 11, 12, 13,
                   12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21,
                   20, 21, 22, 23, 24, 25,
                   24, 25, 26, 27, 28, 29,
                   28, 29, 30, 31, 32, 1]

        output = ''.join(map(lambda i: right_part[i - 1], e_table))
        return output

    def xor(self, right_part, key):
        output = ''.join(map(lambda x, y: str(int(x) ^ int(y)), right_part, key))
        return output

    def transformations(self, right_part):
        S = [
            [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        ]

        B = [right_part[i:i+6] for i in range(0, len(right_part), 6)]
        B_after = ""
        for i in range(len(B)):
            a = int(B[i][::5], 2)
            b = int(B[i][1:5], 2)
            get_binary = lambda x: format(x, 'b').zfill(4)
            number = S[i][a][b]
            B_after += get_binary(number)
        return B_after

    def P(self, right_part):
        P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22,
             11, 4, 25]

        bytes_temp = ''.join(map(lambda j: right_part[j - 1], P))
        return bytes_temp

    def left_rotate(self, key, step):
        return key[step:] + key[:step]

    def keys_generator(self, key, shift_step):
        key_permutation = [
            57, 49, 41, 33, 25, 17, 9, 1,
            58, 50, 42, 34, 26, 18, 10, 2,
            59, 51, 43, 35, 27, 19, 11, 3,
            60, 52, 44, 36, 63, 55, 47, 39,
            31, 23, 15, 7, 62, 54, 46, 38,
            30, 22, 14, 6, 61, 53, 45, 37,
            29, 21, 13, 5, 28, 20, 12, 4
        ]
        shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

        step = sum(map(lambda i: shift[i], range(shift_step + 1)))

        key_after_perm = ''.join(map(lambda i: key[i - 1], key_permutation))

        key_after_rotate = self.left_rotate(key_after_perm[:28], step) + self.left_rotate(key_after_perm[28:], step)

        key_perm_after_creating = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]

        final_key = ''.join(map(lambda i: key_after_rotate[i - 1], key_perm_after_creating))
        return final_key

    def load(self, param):
        file_type = "ключа"
        file_name = "ключ"
        if param == 8:
            file_type = "вектора инициализации"
            file_name = "вектор"
        cwd = getcwd()[2:].replace('\\', '/')
        file = QFileDialog.getOpenFileName(None, f"Загрузить файл {file_type}",
                                           f"{cwd}/параметры/{file_name}_1.txt", "(*.txt)")[0]

        if file == "":
            return

        file_in = open(file, 'r')
        if param == 7:
            temp = file_in.read()
            if len(temp) != 64:
                self.error_input("Загружен неправильный ключ")
                return

            for i in range(8):
                count = 0
                for j in range(8):
                    if int(temp[8 * i + j]) == 1:
                        count += 1

                if count % 2 == 0:
                    self.error_input("Ключ, вероятно, поврежден при передаче")
                    return

            for i in range(len(temp)):
                if temp[i] not in ["0", "1"]:
                    self.error_input("Загружен неправильный ключ")
                    return

            self.key = temp
            self.key_state.setText("Ключ введен")
        else:
            temp = file_in.read()
            if len(temp) != 64:
                self.error_input("Загружен неправильный вектор инициализации")
                return

            for i in range(len(temp)):
                if temp[i] not in ["0", "1"]:
                    self.error_input("Загружен неправильный вектор инициализации")
                    return

            self.vector = temp
            self.vector_state.setText("Вектор инициализации введен")
        file_in.close()

    def save(self, param):
        file_type = "ключа"
        file_name = "ключ"
        if param == 8:
            file_type = "вектора инициализации"
            file_name = "вектор"
            if self.vector == "":
                self.error_input("Сначала определите вектор инициализации")
                return
        else:
            if self.key == "":
                self.error_input("Сначала определите ключ")
                return
        cwd = getcwd()[2:].replace('\\', '/')
        file = \
        QFileDialog.getSaveFileName(None, f"Сохранить файл {file_type}",
                                    f"{cwd}/параметры/{file_name}_1",
                                    "(*.txt)")[0]
        if file:
            with open(file, 'w') as f:
                if param == 7:
                    f.write(self.key)
                else:
                    f.write(self.vector)

    def check_odd(self, key):
        what_to_add = []
        for i in range(8):
            count = 0
            for j in range(7):
                if int(key[7 * i + j]) == 1:
                    count += 1
            if count % 2 == 1:
                what_to_add.append('0')
            else:
                what_to_add.append('1')
        return what_to_add

    def generator(self, param):
        generated_code = ""
        for i in range(param):
            generated_code += self.dec_to_bin(randint(0,255))
        if param == 7:
            added_symbols = self.check_odd(generated_code)
            bytes_grouped = [generated_code[i:i + 7] for i in range(0, len(generated_code), 7)]
            for i in range(len(bytes_grouped)):
                bytes_grouped[i] += (added_symbols[i])
            generated_code = ''.join(bytes_grouped)

            self.key = generated_code
            self.key_state.setText("Ключ введен")
        else:
            self.vector = generated_code
            self.vector_state.setText("Вектор инициализации введен")

    def bin_to_dec(self, bin):
        return int(bin, 2)

    def dec_to_bin(self, dec):
        get_binary = lambda x: format(x, 'b').zfill(8)
        return get_binary(dec)

    def what_to_code(self):
        self.w1 = What_to_code()
        self.w1.my_signal.connect(self.get_type)
        self.w1.exec_()

    def get_type(self, type):
        self.type = type

    def what_mode(self):
        self.w2 = What_mode()
        self.w2.my_signal.connect(self.get_mode)
        self.w2.exec_()

    def get_mode(self, mode):
        self.mode = mode

    def select_file(self):
        cwd = getcwd()[2:].replace('\\', '/')
        file = QFileDialog.getOpenFileName(None, f"Загрузить файл",
                                           f"{cwd}/файлы/1.txt")[0]
        if file == "":
            return
        self.input_file_name.setText(path.basename(file))
        file_in = open(file, 'rb')
        self.text_from_file = file_in.read()
        self.crypt_file_name = file
        file_in.close()


    def utf8_to_decimal(self, symbols):
        symbols = symbols.encode('utf-8')  # превращаем юникод в байты
        decimal_list = list(map(int, symbols))  # байты переводим в десятичное число
        return decimal_list

    def decimal_to_utf8(self, decimal_list):
        # print(decimal_list)
        temp_bytes = bytes(decimal_list)  # десятичное число в байты
        symbols = temp_bytes.decode('utf-8')  # байты в юникод
        return symbols

    def temp_encoding_to_decimal(self, symbols):
        decimal_list = []
        for i in range(len(symbols)):
            for j in range(len(self.temp_encoding)):
                if symbols[i] == self.temp_encoding[j]:
                    decimal_list.append(j)
                    break
        return decimal_list

    def decimal_to_temp_encoding(self, decimal_list):
        symbols = ""
        for i in decimal_list:
            symbols += self.temp_encoding[i]
        return symbols

    def up(self):
        self.input_text.setText(self.output_text.toPlainText())
        self.output_text.setText("")

    def clear(self):
        self.input_text.setText("")
        self.output_text.setText("")

    def error_input(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка ввода")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DES"))
        self.key_gen_button.setText(_translate("MainWindow", "Сгенерировать "))
        self.key_load_button.setText(_translate("MainWindow", "Загрузить "))
        self.key_save_button.setText(_translate("MainWindow", "Сохранить "))
        self.vector_gen_button.setText(_translate("MainWindow", "Сгенерировать"))
        self.vector_load_button.setText(_translate("MainWindow", "Загрузить"))
        self.vector_save_button.setText(_translate("MainWindow", "Сохранить"))
        self.input_file_button.setText(_translate("MainWindow", "Выберите файл"))
        self.encode_button.setText(_translate("MainWindow", "Зашифровать"))
        self.decode_button.setText(_translate("MainWindow", "Расшифровать"))
        self.up_button.setText(_translate("MainWindow", "Наверх"))
        self.clear_button.setText(_translate("MainWindow", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
