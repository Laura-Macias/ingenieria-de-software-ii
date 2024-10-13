from supabase import create_client

class Config:
    SECRET_KEY = '123456'
    SUPABASE_URL = 'https://usgedyofxwmrdrwjkwhq.supabase.co'
    SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzZ2VkeW9meHdtcmRyd2prd2hxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjcwNjE4NzcsImV4cCI6MjA0MjYzNzg3N30.EA8Y-9VFPqCGAobgfE4Iu2NsNVv9OlR1OiQcGMZMyVI'
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)