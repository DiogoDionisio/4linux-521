from docker import DockerClient

dc = DockerClient('tcp://127.0.0.1:2376')

#for i in range(100):
#	porta = 8080 + i
#	novo = dc.containers.run('python:alpine', '/bin/sh', name='for{}'.format(i), detach=True, tty=True, ports={'80':str(porta)})

conteineres = dc.containers.list(all=True)
for c in conteineres:
	print('{0:.<20}{1:.>30}'.format(c.name, c.image.tags[0]))
	if c.name in ['jenkins', 'gitlab']:
		print('Ignorando {0}'.format(c.name))
		continue
	c.remove(force=True)