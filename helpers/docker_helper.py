import docker

client = docker.from_env()

def list_containers():
    list_of_containers = client.containers.list()
    return list_of_containers

def list_volumes():
    list_of_volumes = client.volumes.list()
    return list_of_volumes

if __name__=='__main__':
    list_containers()