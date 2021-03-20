from pwn import *

class Pwn:
    conn=None
    elf=None
    libc=None
    data={}
    logs=[]

    def __init__(self,file_name,libc_name=None,HOST,PORT):
        context.binary=file_name

        if len(sys.argv)>1 and sys.argv[1] == 'r':
            context.log_level="INFO"
            self.conn=remote(HOST, PORT)
            if libc_name!=None:
                libc=ELF(libc_name)
        else:
            context.log_level="DEBUG"
            if libc_name!=None:
                self.conn=process(file_name,env={'LD_PRELOAD':libc_name})
                libc=ELF(libc_name)
            else:
                self.conn=process(file_name)
        
        self.solver()
        self.interactive()
    
    def interactive(self):
        for log in logs:
            for key,value in log.items():
                log.info("{} : {}".format(key,value))

        self.conn.interactive()
    
    def solver(self):
        
if __name__=="__main__":
    pwn=Pwn("chall","libc_name",HOST",2718)
