from pwn import *

file_name='./chall'
libc_name='./libc-???'

context.binary = file_name
context.log_level = 'debug'

HOST = 'target'
PORT = 1337
conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
    conn = remote(HOST, PORT)
else:
    conn = process(file_name,env={'LD_PRELOAD': libc_name})

elf=ELF(file_name)
libc=ELF(libc_name)



conn.interactive()