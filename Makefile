DEV_SERVICE=dev
CMD_RUNNER=docker compose run $(DEV_SERVICE)

all: build tests

build:
	docker compose build $(DEV_SERVICE)

sh:
	$(CMD_RUNNER) /bin/sh

tests:
	$(CMD_RUNNER) unittest-parallel -vs tests -p \*_test.py -t .

serial:
	$(CMD_RUNNER) python serial.py

async:
	$(CMD_RUNNER) python async.py


.PHONY: build sh tests serial async
