import logging

# Configure logging
logging.basicConfig(
    filename="app/logging/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(message):
    logging.error(message)

def log_info(message):
    logging.info(message)
