pip:
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install -e .
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install pytest pytest-cov black importanize pre-commit

install: pip 
	pre-commit install

run:
	MLOD_SETTINGS=$(PWD)/configs/local.ini FLASK_APP=mainapp \
	FLASK_DEBUG=1 \
	flask run

gunicorn:
	MLOD_SETTINGS=$(PWD)/configs/local.ini \
	$(PWD)/bin/mlod gunicorn