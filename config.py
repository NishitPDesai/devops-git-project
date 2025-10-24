import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration management class"""
    
    @staticmethod
    def get_database_url():
        return os.getenv('DATABASE_URL', 'sqlite:///default.db')
    
    @staticmethod
    def get_log_level():
        return os.getenv('LOG_LEVEL', 'INFO')