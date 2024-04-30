.PHONY: all lint test install dev clean distclean

PYTHON ?= python

all: ;

lint:
	q2lint
	flake8

test: all
	py.test && \
	Rscript -e "library(testthat); test_dir('q2_r_example/tests/R')"

install: all
	pip install .

dev: all
	pip install -e .

clean: distclean

distclean: ;
