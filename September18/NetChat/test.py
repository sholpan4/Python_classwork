import hashlib

# username = "Sholpan"
passw = "1234"
salt ="hvgfcdxcf6984w5b67bhejntgb5n6"

# hash = hashlib.md5(passw.encode('utf-8'))
hash = hashlib.md5()
hash = hashlib.sha1()


# hash.update(username.encode)
hash.update(passw.encode)
hash.update(salt.encode)

hash_string = hash.hexdigest()
print(hash_string)