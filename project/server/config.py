import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:test@127.0.0.1:5432/'
database_name = 'diagnostic'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'diagnostic_secret')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'diagnostic_secret'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://lyachyeinkedbd:24cc61f7b19a296d17c3c75e40bb292d312902b2a5fd5442700fa16f69df8775@ec2-52-45-83-163.compute-1.amazonaws.com:5432/d1b1n7i0kso0ch'
