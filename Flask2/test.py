import sys
import hashlib

string= sys.argv[1]
encoded=string.encode()
result1 = hashlib.sha256(encoded)


string = sys.argv[2]
encoded = string.encode()
result2 = hashlib.sha256(encoded)

#print(result.hexdigest())


if (result1.hexdigest()=="2c0004247db2e335c34565cdb82bb431da76b68dc409164c2b0dcbc499052892" and result2.hexdigest()=="dfb2f24a6c78f359aa9156a67792d32a25a76451869b22516b309ea6073e06ad"):
    print("tritt ein")
else:
    print("falsche Eingabe")
