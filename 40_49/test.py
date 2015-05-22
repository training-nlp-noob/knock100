import os
script_dir = os.path.abspath(os.path.dirname(__file__))

print(script_dir)

#hoge = script_dir.replace("40_49", "data")
print(script_dir + "/../data")

with open( script_dir + "/../data/neko.txt" , "r" ) as text:
    print("suc")
