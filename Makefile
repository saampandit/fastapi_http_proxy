help:
	    @echo "Makefile arguments:"
	    @echo ""
	    @echo ""
	    @echo "Makefile commands:"
	    @echo "build"
	    @echo "run"

.DEFAULT_GOAL := all

build:
	    @docker-compose build

run:
	    @docker-compose up

all: build run
