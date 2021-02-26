import docker

docker_client = docker.from_env()
containers = docker_client.containers.list()
container = docker_client.containers.get(container_name)
container.kill()
docker_client.containers.prune()