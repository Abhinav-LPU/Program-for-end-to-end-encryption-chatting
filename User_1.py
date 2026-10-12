#User 1 can send message to chat.txt file and read messages from chat.txt file which was sent by User 2. 
import os
import random
import string

def decoding(lines):
    receive=lines[8:].split()
    mssg=list()
    for word in receive:
        if len(word)<3:
           mssg.append(word[-1:-len(word)-1:-1])
        elif len(word)>=3:
            word=word[3:-3]
            word=word[-1] + word
            word=word[:len(word)-1] 
            mssg.append(word)
    return f"User 2: {' '.join(map(str,mssg))}"


with open("chat.txt", "r") as f:
    lines = f.readlines()
# ignore blank lines at the very end of the file
while lines and lines[-1].strip() == "":
    lines.pop()
block = []
for line in reversed(lines):
    if line.strip() == "":          # skip blank lines between same user messages (use only for strict consecutive same user message behaviour)
        continue
    if line.startswith("User 2: "):
        block.append(line.strip())
    else:
        break          # sequence broken, stop
block.reverse()        # restore the original order
for line in block:
    print(decoding(line))


send=input("You: ").split()
mssg=list()
for element in send:
    word=element
    if len(word)<3:
        mssg.append(word[-1:-len(word)-1:-1])
    elif len(word)>=3:
        word=word+word[0]
        word=word[1:]
        random_chars=string.ascii_letters + string.digits
        prefix=''.join(random.choices(random_chars,k=3))
        suffix=''.join(random.choices(random_chars,k=3))
        word=f"[{prefix}{word}{suffix}"
        mssg.append(word[1:])
with open("chat.txt","a") as f:
    final_mssg=' '.join(map(str,mssg))
    f.write(f"User 1: {final_mssg}\n")
