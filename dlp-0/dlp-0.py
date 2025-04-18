# Forked from beta-bet challenge
import secrets
from flag import flag

alphabet = "abcdefghijklmnopqrstuvwxyz"

def random_key(m):
    key_len = secrets.randbelow(len(m) ** 2)

    if key_len < len(m):
        key_len = key_len + len(m)

    key = ''.join(secrets.choice(alphabet) for i in range(key_len))
    return key

def encrypt(m):
  key = random_key(m)[0:len(m)]
  ct = []

  for i in range(len(m)):
      c = ord(m[i]) - 97
      key_val = ord(key[i])
      x =  (3**c + 7**key_val * 4**key_val) % 29 
      x += ord("a")
      ct.append(chr(x))

  return("".join(ct))

if __name__ == "__main__":
  pt = flag()
  for i in range(0, 113):
    print("CWW{", encrypt(pt), "}", sep="")
