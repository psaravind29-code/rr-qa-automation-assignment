import logging
import os

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('reports/execution.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)