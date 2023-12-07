DEV_SERVICE=dev
CMD_RUNNER=docker compose run $(DEV_SERVICE)

all: build tests

build:
	docker compose build $(DEV_SERVICE)

sh:
	$(CMD_RUNNER) /bin/sh

tests:
	$(CMD_RUNNER) python -m unittest discover -vs tests -p \*_test.py -t .

time-serial:
	$(CMD_RUNNER) python serial.py

time-async:
	$(CMD_RUNNER) python async.py


.PHONY: build tests tests-par \
	sh \
	time-serial time-async
