IMAGE_NAME=sentiment-app
CONTAINER_NAME=sentiment-container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -p 8501:8501 --name $(CONTAINER_NAME) $(IMAGE_NAME)

clean:
	-docker rm -f $(CONTAINER_NAME)
	-DOCKER rmi -f $(IMAGE_NAME)

