"""
It loads the enviroment variables in a dictionary named env
"""

import os
from dotenv import load_dotenv

load_dotenv()

env = {
    'auth': {
    'key': os.getenv('AUTH_KEY'),
  },
}