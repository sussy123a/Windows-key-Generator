import random
import string

def generate_random_key():
    # Generate key for Windows 10 sigma rizz edition  
    key_parts = []
    for _ in range(5):  # 5 sections
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # 5 characters long
        key_parts.append(part)
    
    # Join the parts  
    return '-'.join(key_parts)

# Generate  
random_key = generate_random_key()
print(random_key)
