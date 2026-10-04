import json
import requests
URL = "http://127.0.0.1:11434/api/chat"
Model= "qwen3:8b"
history=[]
while True:
    text=input("请输入你想说的话：")
    if text=="exit":
        break
    history.append({"role":"user","content":text})# 我的对话
    data ={"model":Model,"messages":history,"stream": True} #stream=true让文字可以实时输出，messages那边我之前做的时候使用的{"role":"user","content":text}
    print("AI:",end="")
    reply=""
    with requests.post(URL,json=data,stream=True) as r: #实现不间断输出文字
        for line in r.iter_lines():
            if line:
                chunk =json.loads(line)
                piece=chunk["message"]["content"]
                print(piece,end="",flush=True)
                reply+=piece
    print("")
    history.append({"role":"assistant","content":reply}) #模型的对话