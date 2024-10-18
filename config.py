import os
import dotenv

dotenv.load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
SSL_MODE = os.getenv("SSL_MODE") 
