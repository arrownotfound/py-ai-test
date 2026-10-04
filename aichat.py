import json
import requests

from pyexpat.errors import messages

URL = "http://127.0.0.1:11434/api/chat"
text=input("请输入你想说的话：")
data ={"model":"qwen3:8b","messages":[{"role":"user","content":text}],"stream": True}
print("Bot:",end="")
with requests.post(URL,json=data,stream=True) as r:
    for line in r.iter_lines():
        if line:
            chunk =json.loads(line)
            print(chunk["message"]["content"],end="",flush=True)
print("")
