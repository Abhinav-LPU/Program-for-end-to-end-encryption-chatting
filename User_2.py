# User 2 can send messages to chat.txt file and read messages from it which was sent by User 1. Just run the code to read and write anything.
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
    return f"User 1: {' '.join(map(str,mssg))}"

with open("chat.txt", "r") as f:
    lines = f.readlines()
# ignore blank lines at the very end of the file
while lines and lines[-1].strip() == "":
    lines.pop()
block = []
for line in reversed(lines):
    if line.strip() == "":          # skip blank lines between same user messages (use only for strict consecutive same user message behaviour)
        continue
    if line.startswith("User 1: "):
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
    f.write(f"User 2: {final_mssg}\n")




# import os
# filename = "messages.txt"                     WRONG DECODING METHOD(only print firt line)
# with open(filename, "rb") as file:  # "rb" mode is required to seek from the end
#     # 1. Move the cursor to the absolute end of the file
#     file.seek(0, os.SEEK_END)
#     position = file.tell()
#     # 2. Walk backwards byte-by-byte to find the newline character
#     # We skip the very last byte in case the file ends with a trailing newline
#     if position > 0:
#         position -= 1 
#     while position > 0:
#         file.seek(position)
#         current_char = file.read(1)
#         # If we find a newline, the next byte is the start of the last line
#         if current_char == b"\n":
#             file.seek(position + 1)
#             break
#         position -= 1
#     else:
#         # If no newline was found, the whole file is just one line
#         file.seek(0)
#     # 3. Read the last line safely now that the cursor is positioned at its start
#     # Decode it back to text since we opened it in binary mode
#     read_current_last_line=file.readline().decode('utf-8')
#     if read_current_last_line.startswith("User 1: "):
#         print(decoding(read_current_last_line))


# def read_lines_reversed(path, chunk_size=8192):                       RIGHT DECODING METHOD(good for large txt file)
#     """Yield lines of the file from last to first, reading small chunks from the end."""
#     with open(path, "rb") as f:
#         f.seek(0, 2)                # go to the end of the file
#         pos = f.tell()
#         buffer = b""
#         while pos > 0:
#             read_size = min(chunk_size, pos)
#             pos -= read_size
#             f.seek(pos)             # jump back one chunk
#             buffer = f.read(read_size) + buffer
#             parts = buffer.split(b"\n")
#             buffer = parts[0]       # first part may be incomplete, keep for next round
#             for raw in reversed(parts[1:]):
#                 yield raw.decode("utf-8").rstrip("\r")
#         yield buffer.decode("utf-8").rstrip("\r")   # the very first line of the file
# block = []
# for line in reversed(lines):
#     if line.startswith("User 1: "):
#         block.append(line.strip())
#     else:
#         break          # sequence broken, stop
# block.reverse()        # restore the original order
# for line in block:
#     print(decoding(line))
