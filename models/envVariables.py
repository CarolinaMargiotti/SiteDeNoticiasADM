import os
from dotenv import load_dotenv

load_dotenv()

serviceUrl = os.getenv('serviceUrl')
projectUrl = os.getenv('projectUrl')
host = os.getenv('host')
port = os.getenv('port')