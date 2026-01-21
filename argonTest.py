
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("correct horse battery staple")

print(len(hash))