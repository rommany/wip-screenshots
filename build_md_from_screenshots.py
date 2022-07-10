import sys, os, re

dir="2022"

file = open(f"{dir}.md",'w')
text=""
for f in os.listdir(dir):
    name = re.sub(r'\s','%20',f)
    mdlink = f'![]({dir}/{name})'
    text += mdlink+'\n'


file.write(text)
file.close()