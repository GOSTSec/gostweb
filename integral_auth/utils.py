import random
import string

def rand_string(length):
    """Generate lame random hexdigest string"""
    return "".join([random.choice(string.hexdigits) for _ in range(length)])

