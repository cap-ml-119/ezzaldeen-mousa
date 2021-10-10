init:
	pip install pep8 flake8 pylint pytest coverage
	pip install -r app/requirements.txt

lint: init
	@echo 'linting....'
	@echo ''
	flake8 app/src

# Reposetory name
REPO = todoapp:v1

docker-build:
	@echo 'building the container'
	@echo ''
	docker build -t $(REPO) .

docker-run: docker-build
	@echo 'running the container'
	@echo ''
	docker run $(REPO)