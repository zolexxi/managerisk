import os
basedir = os.path.abspath(os.path.dirname(__file__))

#List of (environment) variables used for setup

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MANAGERISK_MAIL_SUBJECT_PREFIX = '[Managerisk]'
    MANAGERISK_MAIL_SENDER = 'Managerisk Admin <dennis@iliaens.eu>'
    MANAGERISK_ADMIN = os.environ.get('MANAGERISK_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

# Production config class

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# Docker config class
        
class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

# Dictionary with all available configs. Add new entry if you add another config class

config = {
    'production': ProductionConfig,
    'docker': DockerConfig,
}