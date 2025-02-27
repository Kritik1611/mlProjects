import sys
import logging
from src.logger import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s"
)

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # Correct super() usage
        self.error_message = error_message_details(error, error_detail)

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.error(f"An error occurred: {e}")  # Log the actual error
#         raise CustomException(e, sys)
