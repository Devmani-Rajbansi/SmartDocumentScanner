from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from app.backend.ocr_processor import OCRProcessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Document Scanner")
        self.setGeometry(100, 100, 800, 600)

        # Main Layout
        layout = QVBoxLayout()

        # Upload Button
        self.upload_button = QPushButton("Upload Document")
        self.upload_button.clicked.connect(self.upload_document)

        # Image Display
        self.image_label = QLabel("No Image Uploaded")
        self.image_label.setAlignment(Qt.AlignCenter)

        # Text Area for OCR Result
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setPlaceholderText("Extracted text will appear here...")

        # Add Widgets to Layout
        layout.addWidget(self.upload_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.text_area)

        # Set Layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def upload_document(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

            # Perform OCR and display result
            ocr_text = OCRProcessor.extract_text(file_path)
            self.text_area.setText(ocr_text)
