pipenv-install:
	@echo "******************************************"
	@echo "*    Installing pipenv requirements      *"
	@echo "******************************************"
	export PIPENV_NO_INHERIT=1 && pipenv install --dev

pipenv-shell:
	@echo "******************************************"
	@echo "*             pipenv shell               *"
	@echo "******************************************"
	pipenv shell

dev-init:
	@echo "******************************************"
	@echo "*       Preparing dev environment        *"
	@echo "******************************************"
	cp docker-compose.yml-dist docker-compose.yml
	cp env/env-dist env/.env.dev

build:
	@echo "******************************************"
	@echo "*           Building services            *"
	@echo "******************************************"
	docker-compose build

start:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

timescaledb-tune-quiet:
	@echo "******************************************"
	@echo "*      Tuning timescaledb (quiet)        *"
	@echo "******************************************"
	docker-compose run --rm envio-db timescaledb-tune --quiet --yes

timescaledb-tune:
	@echo "******************************************"
	@echo "*           Tuning timescaledb           *"
	@echo "******************************************"
	docker-compose run --rm envio-db timescaledb-tune

migrate:
	@echo "******************************************"
	@echo "*               Migrating DB             *"
	@echo "******************************************"
	docker-compose run --rm -T envio-api envio_challenge/manage.py migrate

makemigrations:
	@echo "******************************************"
	@echo "*          Making DB migrations          *"
	@echo "******************************************"
	docker-compose run --rm -T envio-api envio_challenge/manage.py makemigrations

createsuperuser:
	@echo "******************************************"
	@echo "*        Creating django superuser       *"
	@echo "******************************************"
	docker-compose run --rm envio-api envio_challenge/manage.py createsuperuser

generate-test-db-data:
	@echo "******************************************"
	@echo "*        Generating test DB data         *"
	@echo "******************************************"
	docker-compose run --rm envio-api envio_challenge/manage.py generate_test_db_data

check-deploy:
	@echo "******************************************"
	@echo "*           Security checking            *"
	@echo "******************************************"
	docker-compose run --rm envio-api envio_challenge/manage.py check --deploy

sleep_5:
	@echo "******************************************"
	@echo "*        Sleeping for 5 sec...           *"
	@echo "******************************************"
	sleep 5

install: pipenv-install dev-init build start sleep_5 stop timescaledb-tune-quiet migrate makemigrations
	@echo "All done."