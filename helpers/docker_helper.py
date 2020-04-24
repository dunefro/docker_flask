import docker

#Initialising the docker client here
client = docker.from_env()

# For listing the containers
def list_containers():
    list_of_containers = client.containers.list()
    return list_of_containers

# For listing the volumes 
def list_volumes():
    list_of_volumes = client.volumes.list()
    return list_of_volumes

# For listing the images
def list_images():
    list_of_images = [ img for img in client.images.list() if img.tags ]
    return list_of_images

if __name__=='__main__':
    list_containers()
