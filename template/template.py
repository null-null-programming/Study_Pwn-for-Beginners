from pwn import *

class Pwn:
    conn=None
    elf=None
    libc=None
    data={}
    
    def __init__(self,file_name,libc_name=None,host_port=None):
        context.binary=file_name
    
        if len(sys.argv)>1 and sys.argv[1] == 'r':
            context.log_level='INFO'
            self.conn=remote(host_port.split(' ')[0],host_port.split(' ')[1])
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
        for key,value in self.data.items():
            log.info('{} : {}'.format(key,hex(value)))
    
        self.conn.interactive()
    
    def solver(self):
    
if __name__=='__main__':
    pwn=Pwn('chall','libc_name','host_port')
    pwn.solver()
    pwn.interactive()


{
	"pwn template": {
	"prefix": "temp",
	  "body": [
		"from pwn import *",
		"",
		"class Pwn:",
    		"\tconn=None",
    		"\telf=None",
    		"\tlibc=None",
    		"\tdata={}",
			"\t",
    		"\tdef __init__(self,file_name,libc_name=None,host_port=None):",
        		"\t\tcontext.binary=file_name",
			"\t",
        		"\t\tif len(sys.argv)>1 and sys.argv[1] == 'r':",
            		"\t\t\tcontext.log_level='INFO'",
            		"\t\t\tself.conn=remote(host_port.split(' ')[0],host_port.split(' ')[1])",
         		"\t\t\tif libc_name!=None:",
                	"\t\t\t\tlibc=ELF(libc_name)",
        	"\t\telse:",
            	"\t\t\tcontext.log_level='DEBUG'",
            	"\t\t\tif libc_name!=None:",
                	"\t\t\t\tself.conn=process(file_name,env={'LD_PRELOAD':libc_name})",
                	"\t\t\t\tlibc=ELF(libc_name)",
            	"\t\t\telse:",
                	"\t\t\t\tself.conn=process(file_name)",
			"\t",
    		"\tdef interactive(self):",
            		"\t\tfor key,value in self.data.items():",
                		"\t\t\tlog.info('{} : {}'.format(key,hex(value)))",
			"\t",
					"\t\tself.conn.interactive()",
			"\t",
    		"\tdef solver(self):",
			"\t",
		"if __name__=='__main__':",
    		"\tpwn=Pwn('chall','libc_name','host_port')",
			"\tpwn.solver()",
			"\tpwn.interactive()",
	  ],
     "description": "template for pwn"
    }
}