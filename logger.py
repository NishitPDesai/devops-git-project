import logging

def setup_logging():
    """Setup basic logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

# Example usage
if __name__ == "__main__":
    logger = setup_logging()
    logger.info("Logging system initialized")
    logger.warning("This is a warning message")