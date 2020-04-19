import docker

client = docker.from_env()

def list_containers():
    list_of_containers = client.containers.list()
    return list_of_containers

if __name__=='__main__':
    list_containers()