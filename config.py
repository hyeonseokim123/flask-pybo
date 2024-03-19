import os

BASE_DIR = os.path.dirname(__file__) # 디렉토리 경로

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR,'pybo.db'))

SQLALCHEMY_TRACK_MODIFICATIONS = False

# os.makedirs("/path/new/directory")