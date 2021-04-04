
from cryptography.fernet import Fernet
  
# we will be encryting the below string.
message = "hellogeekssdbsdvsdvgvsrsbdsbs"
  
# generate a key for encryptio and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key
  
# key = Fernet.generate_key()

# key = b'HkLYcD5m5zH9VYNEQt9GpWzxq87SHHbhpxvFR9LgF9Q=' # this is bytes

# fernet = Fernet(key)

# encMessage = fernet.encrypt(message.encode())

# print("original string: ", message)
# print("encrypted string: ", encMessage)
# print("encrypted length: ", len(encMessage))


  
# decMessage = fernet.decrypt(encMessage).decode()
  
# print("decrypted string: ", decMessage)

# bytes(some_string, encoding)

my_str = "hello world"
my_str_as_bytes = str.encode(my_str)
print(my_str_as_bytes)
print(type(my_str_as_bytes)) # ensure it is byte representation
my_decoded_str = my_str_as_bytes.decode()
print(my_decoded_str)
print(type(my_decoded_str)) # ensure it is string representation