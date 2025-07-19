import sys
import os
import logging

# Add root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from airport_parking_toolkit.logger import setup_logger

def test_setup_logger(tmp_path):
    log_file = tmp_path / "test.log"
    logger = setup_logger(str(log_file))
    
    assert isinstance(logger, logging.Logger)
    logger.info("This is a test log message.")
    
    # Check if log file is written
    assert log_file.exists()
    content = log_file.read_text()
    assert "This is a test log message." in content
