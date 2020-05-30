import os

class Config:
    """
    General configuration parent class
    """
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=fc0dd4871fc54be18c1ae26a02ba8a53'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=fc0dd4871fc54be18c1ae26a02ba8a53'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    """
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}