import argon2
import os
from config import *
from warnings import filterwarnings
import string
import random

filterwarnings("ignore", category=DeprecationWarning) 

def salt_generator(salt_lenght=16):
    return os.urandom(salt_lenght)

def hash_generator(password=None, salt_lenght=10, time=2, memory_c=65536):
    salt = salt_generator(salt_lenght)
    hashed_password = argon2.hash_password(password.encode("utf-8"),salt=salt,time_cost=time,memory_cost=memory_c)
    return hashed_password
    
def hash_verify(hashed_password,password):
    return argon2.verify_password(hashed_password,password.encode("utf-8"))

def rdm_str_generator(lenght):
    characters = string.ascii_letters + string.digits
    random_sequence = ''.join(random.choice(characters) for _ in range(lenght))
    return random_sequence
