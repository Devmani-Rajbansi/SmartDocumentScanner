import cv2
import pytesseract
from app.logging.logger import log_error

class OCRProcessor:
    @staticmethod
    def preprocess_image(image_path):
        """Preprocess the image for better OCR results."""
        # Read the image
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply thresholding
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return thresh

    @staticmethod
    def extract_text(image_path):
        """Extract text from the image using Tesseract OCR."""
        try:
            preprocessed_image = OCRProcessor.preprocess_image(image_path)
            # Use Tesseract to perform OCR
            text = pytesseract.image_to_string(preprocessed_image, lang='eng')
            return text
        except Exception as e:
            log_error(f"OCR failed for {image_path}: {str(e)}")
            return f"Error during OCR: {str(e)}"
