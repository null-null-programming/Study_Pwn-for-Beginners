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
						elf_name=os.path.join('.',file)
						elf=ELF(elf_name)
						context.binary=elf_name
						conn=process(elf_name)
					elif cnt==1 and 'libc' in file:
						libc_name=os.path.join('.',file)
						libc=ELF(libc_name)
						conn=process(elf_name,env={'LD_PRELOAD':libc_name})

		if len(sys.argv)>1 and sys.argv[1]=='r':
			context.log_level='INFO'
			conn=remote(host_port.split(' ')[0],host_port.split(' ')[1])
		else:
			gdb.attach(conn,'''
				b *main
			''')

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