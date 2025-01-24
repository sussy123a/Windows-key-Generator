import random
import string
import time

def generate_random_key():
    # Generate random parts for each section
    key_parts = []
    for _ in range(5):  # 5 sections
        part = ''.join(random.choices(string.ascii_uppercase, k=5))  # 5 characters long
        key_parts.append(part)
    
    # Join the parts with hyphens
    return '-'.join(key_parts)

# Generate and print the key
random_key = generate_random_key()
print(random_key)
time.sleep(5)
