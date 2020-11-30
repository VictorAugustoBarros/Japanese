local:
	docker-compose -f local.yml up --build

localb:
	docker-compose -f local.yml up --build -d

stop:
	docker-compose down

black:
	black --line-length 110 --target-version py37 config/

isort:
	isort -rc config/

pydocstyle:
	pydocstyle config/
