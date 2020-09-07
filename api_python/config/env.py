import os
from dotenv import load_dotenv

load_dotenv()

env = {
    'auth': {
    'key': os.getenv('AUTH_KEY'),
  },
}