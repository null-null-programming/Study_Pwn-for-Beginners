from pwn import *

class Pwn:
    conn=None
    elf=None
    libc=None
    data={}
    
    def __init__(self,file_name,libc_name=None,host_port):
        context.binary=file_name
    
        if len(sys.argv)>1 and sys.argv[1] == 'r':
            context.log_level='INFO'
            self.conn=remote(host_port.slice(' ')[0],host_port.slice(' ')[1])
        if libc_name!=None:
            libc=ELF(libc_name)
    else:
        context.log_level='DEBUG'
        if libc_name!=None:
            self.conn=process(file_name,env={'LD_PRELOAD':libc_name})
            libc=ELF(libc_name)
        else:
            self.conn=process(file_name)
    
    def interactive(self):
        for key,value in data.items():
            log.info('{} : {}'.format(key,hex(value)))
    
        self.conn.interactive()
    
    def solver(self):
    
if __name__=='__main__':
    pwn=Pwn('chall','libc_name','host_port')
    pwn.solver()
    pwn.interactive()