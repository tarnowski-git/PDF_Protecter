import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from PyPDF2 import PdfFileWriter, PdfFileReader


class MainApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # initialize variables
        self.title = "PDF Encrypter/Decrypter"
        self.top = 50
        self.left = 50
        self.width = 400
        self.height = 400
        self.file_name = ""
        # bulding UI
        self.init_UI()
        self.createWidgets()
        self.create_GroupBox_File()
        self.create_GroupBox_Encrypt()
        self.create_GroupBox_Decrypt()
        self.set_ButtonConnections()
        self.setup_layout()

    def init_UI(self):
        """Setting general configurations of the application"""
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

    def createWidgets(self):
        """Creating the widgets of the application"""
        self.btn_file = QtWidgets.QPushButton("Choose PDF file")

        self.txt_filePath = QtWidgets.QLineEdit(self)
        self.txt_filePath.setPlaceholderText("File Path")

        self.txt_password1 = QtWidgets.QLineEdit(self)
        self.txt_password1.setPlaceholderText("Password")

        self.txt_password2 = QtWidgets.QLineEdit(self)
        self.txt_password2.setPlaceholderText("Repeat Password")

        self.btn_encrypt = QtWidgets.QPushButton("Encrypt File")

        self.txt_password3 = QtWidgets.QLineEdit(self)
        self.txt_password3.setPlaceholderText("Password")

        self.btn_decrypt = QtWidgets.QPushButton("Decrypt File")

    # METHODS
    def encrypt(self):
        if (self.txt_password1.text() != "") and (self.txt_password1.text() == self.txt_password2.text()):

            new_file_name = "protected_" + self.file_name
            self.addEncription(self.txt_filePath.text(),
                               new_file_name, self.txt_password1.text())
            # cleaning
            self.txt_filePath.setText("")
            self.txt_password1.setText("")
            self.txt_password2.setText("")

            # information message
            dial_msg = QtWidgets.QMessageBox()
            dial_msg.setIcon(QtWidgets.QMessageBox.Information)
            dial_msg.setWindowTitle("Encrypted successed!")
            dial_msg.setText("The file has a password.")
            dial_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            dial_msg.exec_()

        else:
            # critical message
            errorMessage = QtWidgets.QMessageBox()
            errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
            errorMessage.setWindowTitle("Password Error")
            errorMessage.setText("Password must be the same")
            errorMessage.exec_()

    def decrypt(self):
        if (self.txt_password3.text() != ""):
            new_file_name = "unprotected_" + self.file_name
            try:
                self.removePassword(self.txt_filePath.text(),
                                             new_file_name, self.txt_password3.text())
                # cleaning
                self.txt_filePath.setText("")
                self.txt_password3.setText("")
                # information message
                dial_msg = QtWidgets.QMessageBox()
                dial_msg.setIcon(QtWidgets.QMessageBox.Information)
                dial_msg.setWindowTitle("Decrypted successed!")
                dial_msg.setText("The file already has not a password.")
                dial_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                dial_msg.exec_()
            except:
                # critical message
                errorMessage = QtWidgets.QMessageBox()
                errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
                errorMessage.setWindowTitle("Password Error")
                errorMessage.setText("Password must be uncorrect")
                errorMessage.exec_()
        else:
            # critical message
            errorMessage = QtWidgets.QMessageBox()
            errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
            errorMessage.setWindowTitle("Password Error")
            errorMessage.setText("Please type the password")
            errorMessage.exec_()

    def showFileDialog(self):
        dial_options = QtWidgets.QFileDialog.Options()
        dial_options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select your file", "./", "PDF Files (*.pdf)", options=dial_options)

        if file_path[0]:
            self.txt_filePath.setText(file_path[0])
            self.file_name = os.path.basename(file_path[0])

    def addEncription(self, input_file: str, output_file: str, password: str):
        """
        Function to encrypt PDF files.

        Parameters
        ----------
        `input_file` : string
            name of input PDF file
        `output_file` : string
            name of output PDF file
        `password` : string
        """

        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(input_file)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

        with open(output_file, "wb") as fh:
            pdf_writer.write(fh)

    def removePassword(self, input_file, output_file, password):
        """
        Parameters
        ----------
        `input_file` : string
            name of encrypted PDF file
        `output_file` : string
            name of output PDF file
        `password` : string
            password which encrypted the file
        """
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(input_file)

        # encryption
        if pdf_reader.isEncrypted:
            pdf_reader.decrypt(password)
        else:
            # if File is not encrypted, return flase
            return False

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output_file, "wb") as fh:
            pdf_writer.write(fh)

        return True

    def set_ButtonConnections(self):
        self.btn_file.clicked.connect(self.showFileDialog)
        self.btn_encrypt.clicked.connect(self.encrypt)
        self.btn_decrypt.clicked.connect(self.decrypt)

    def create_GroupBox_File(self):
        self.GroupBox_file = QtWidgets.QGroupBox("Insert file")
        layout = QtWidgets.QFormLayout()
        layout.addRow(self.btn_file, self.txt_filePath)
        self.GroupBox_file.setLayout(layout)

    def create_GroupBox_Encrypt(self):
        self.GroupBox_Encrypt = QtWidgets.QGroupBox("Encrypt File")
        layout = QtWidgets.QFormLayout()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.txt_password1)
        hbox.addWidget(self.txt_password2)
        hbox.addWidget(self.btn_encrypt)
        layout.addRow(hbox)
        self.GroupBox_Encrypt.setLayout(layout)

    def create_GroupBox_Decrypt(self):
        self.GroupBox_Decrypt = QtWidgets.QGroupBox("Decrypt File")
        layout = QtWidgets.QFormLayout()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.txt_password3)
        hbox.addWidget(self.btn_decrypt)
        layout.addRow(hbox)
        self.GroupBox_Decrypt.setLayout(layout)

    def setup_layout(self):
        self.central_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.GroupBox_file)
        self.main_layout.addWidget(self.GroupBox_Encrypt)
        self.main_layout.addWidget(self.GroupBox_Decrypt)
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    # IMPORTANT!!!!! Windows are hidden by default.
    window.show()
    # Start the event loop.
    sys.exit(app.exec_())
    # Your application won't reach here until you exit and the event
    # loop has stopped.
