import docker

client = docker.from_env()
image = client.image.pull('igorf777/gitact', tag='main')
client.containers.run(image, detach=True, ports=('0.0.0.0',5000), name='acts')

#client = docker.from_env()

#client.i
#containers = docker_client.containers.list()
#container = docker_client.containers.get(container_name)
#container.kill()
#docker_client.containers.prune()