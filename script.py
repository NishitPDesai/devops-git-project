import logging
from logger import setup_logging

def hello_world():
    """Simple hello world function"""
    return "Hello, DevOps World!"

def calculate_sum(a, b):
    """Calculate sum of two numbers"""
    return a + b

if __name__ == "__main__":
    # Setup logging
    logger = setup_logging()
    
    print(hello_world())
    print(f"Sum of 5 and 3: {calculate_sum(5, 3)}")
    
    logger.info("Script execution completed")