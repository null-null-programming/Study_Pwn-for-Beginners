from pwn import *
import os
import magic

class Pwn:

	def __init__(self,host_port=None,conn=None,elf=None,libc=None,logs={}):
		elf_name=None
		context.log_level='DEBUG'

		for cnt in range(2):
			for file in os.listdir(os.getcwd()):
				if 'ELF' in magic.from_file(file):
					if cnt==0 and not 'libc' in file and file!='core':
						elf_name=file
						elf=ELF('./'+file)
						context.binary=file
						conn=process(file)
					elif cnt==1 and 'libc' in file:
						libc=ELF('./'+file)
						conn=process(elf_name,env={'LD_PRELOAD':file})

				if len(sys.argv)>1 and sys.argv[1]=='r':
					context.log_level='INFO'
					conn=remote(host_port.split(' ')[0],host_port.split(' ')[1])

		if libc==None:
			self.solver(conn,logs,elf)
		else:
			self.solver(conn,logs,elf,libc)

		self.interactive(conn,logs)

	def interactive(self,conn,logs):
		for key,value in logs.items():
			log.info('{}'.format(key).ljust(15,' ')+':{}'.format(hex(value)))

		conn.interactive()

	def solver(self,conn,logs,elf,libc=None):
		return

if __name__=='__main__':
	pwn=Pwn('HOST_PORT')

{
	"pwn template": {
	"prefix": "temp",
	  "body": [
		"from pwn import *",
		"import os",
		"import magic",
		"",
		"class Pwn:",
		"",
			"\tdef __init__(self,host_port=None,conn=None,elf=None,libc=None,logs={}):",
				"\t\telf_name=None",
				"\t\tcontext.log_level='DEBUG'",
		"",
				"\t\tfor cnt in range(2):",
					"\t\t\tfor file in os.listdir(os.getcwd()):",
						"\t\t\t\tif 'ELF' in magic.from_file(file):",
							"\t\t\t\t\tif cnt==0 and not 'libc' in file and file!='core':",
								"\t\t\t\t\t\telf_name=file",
								"\t\t\t\t\t\telf=ELF('./'+file)",
								"\t\t\t\t\t\tcontext.binary=file",
								"\t\t\t\t\t\tconn=process(file)",
							"\t\t\t\t\telif cnt==1 and 'libc' in file:",
								"\t\t\t\t\t\tlibc=ELF('./'+file)",
								"\t\t\t\t\t\tconn=process(elf_name,env={'LD_PRELOAD':file})",
				"",		
				"\t\t\t\tif len(sys.argv)>1 and sys.argv[1]=='r':",
					"\t\t\t\t\tcontext.log_level='INFO'",
					"\t\t\t\t\tconn=remote(host_port.split(' ')[0],host_port.split(' ')[1])",
				"",
				"\t\tif libc==None:",
					"\t\t\tself.solver(conn,logs,elf)",
				"\t\telse:",
					"\t\t\tself.solver(conn,logs,elf,libc)",
				"",
				"\t\tself.interactive(conn,logs)",
				"",
			"\tdef interactive(self,conn,logs):",
				"\t\tfor key,value in logs.items():",
					"\t\t\tlog.info('{}'.format(key).ljust(15,' ')+':{}'.format(hex(value)))",
			"",
				"\t\tconn.interactive()",
			"",
			"\tdef solver(self,conn,logs,elf,libc=None):",
			"\t\treturn",
			"",
		"if __name__=='__main__':",
			"\tpwn=Pwn('HOST_PORT')",
	  ],
     "description": "template for pwn"
    }
}