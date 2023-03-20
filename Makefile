DEV_SERVICE=dev
CMD_RUNNER=docker compose run $(DEV_SERVICE)

all: build test

.PHONY : build
build:
	docker compose build $(DEV_SERVICE)

.PHONY : sh
sh:
	$(CMD_RUNNER) /bin/sh

#
# overrides from common to run commands in dev container
#

.PHONY : %
d-%:
	$(MAKE) CMD_RUNNER="$(CMD_RUNNER)" -f Makefile.common $*
