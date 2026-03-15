import logging 
import os
from datetime import datetime

LOG_FILE = os.path.join(os.getcwd(), "logs", f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"

)

if __name__ == "__main__":
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")