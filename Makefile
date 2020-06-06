# ==============================================================================
# DECLARING VARIABLES
# ==============================================================================

# CONTAINERS
DOCKER_CONTAINER_LIST:=$(shell docker ps -aq)

# ==============================================================================
# DOCKER
# ==============================================================================

system:
	docker system prune -af

volume:
	docker volume prune -f

network:
	docker network prune -f

stop:
	docker stop ${DOCKER_CONTAINER_LIST}

remove:
	docker rm ${DOCKER_CONTAINER_LIST}

# ==============================================================================
# DOCKER-COMPOSE
# ==============================================================================

compose:
	docker-compose up --build

back:
	docker-compose up --build -d

down:
	docker-compose down
