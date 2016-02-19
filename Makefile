registry=docker.chem.byu.edu:5000
name=material
ports=-p 80:80

all: build push

build:
	docker build --rm -t $(registry)/$(name) .

push:
	docker push $(registry)/$(name)

no-cache:
	docker build --no-cache --rm -t $(registry)/$(name) .

shell:
	docker build --rm -t $(registry)/$(name) .
	docker run --rm $(ports) --name $(name)_test -t -i $(registry)/$(name) /bin/bash

compose:
	docker-compose run --service-ports djangomaterial bash
