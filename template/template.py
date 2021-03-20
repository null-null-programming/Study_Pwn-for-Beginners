from pwn import *

file_name='./chall'

context.binary = file_name
context.log_level = 'debug'

    def interactive(self):
        for log in logs:
            for key,value in log.items():
                log.info("{} : {}".format(key,value))

if len(sys.argv) > 1 and sys.argv[1] == 'r':
    conn = remote(HOST, PORT)
else:
    conn = process(file_name,)

elf=ELF(file_name)



conn.interactive()