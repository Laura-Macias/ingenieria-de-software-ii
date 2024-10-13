from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY_APP = os.getenv('SECRET_KEY')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SUPABASE_URL = os.getenv('SUPABASE_URL')

class Config:
    SECRET_KEY = SECRET_KEY_APP
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)