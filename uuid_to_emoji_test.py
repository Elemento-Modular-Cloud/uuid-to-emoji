import uuid
import json
import base64
from textwrap import wrap

with open('emoji_converter.json', 'r') as fp:
    mapping = json.load(fp)

uuid = uuid.uuid1()
print(uuid)
print(uuid.bytes)
base32uuid = wrap(base64.b32hexencode(uuid.bytes).decode(), 2)
print(base32uuid)
j = 0
for i, b32 in enumerate(base32uuid):
    if b32 == "==":
        base32uuid[i] = base32uuid[j]
        j+=1
print(base32uuid)
intuuid = [int(b32, 32) for b32 in base32uuid][0::4]
print(intuuid)
emojiuuid = ''.join([mapping[str(i)] for i in intuuid])
print(emojiuuid)
