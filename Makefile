SHELL=/bin/bash

.DEFAULT_GOAL := _help

# NOTE: must put a <TAB> character and two pound "\t##" to show up in this list.  Keep it brief! IGNORE_ME
.PHONY: _help
_help:
	@printf "\nUsage: make <command>, valid commands:\n\n"
	@grep "##" $(MAKEFILE_LIST) | grep -v ^# | grep -v IGNORE_ME | sed -e 's/##//' | column -t -s $$'\t'



# ---------------------------------------
# init & venv
# ---------------------------------------

.PHONY: init
init:	## Set up a Python virtual environment
	# Fetch submodule
	git submodule update --init
	# Re-add virtual environment
	rm -rf .venv
	${PY_SYS_INTERPRETER} -m venv .venv
	# Upgrade dependencies and pip, if NOT running in CI automation
	- if [ -z "${CI}" ]; then ${PY_SYS_INTERPRETER} -m venv --upgrade-deps .venv; fi
	direnv allow
	@echo "Successfully initalized venv, run 'make deps' now!"

# include .env
SKIP_VENV ?=
PYTHON ?= $(shell which python)
PWD ?= $(shell pwd)
.PHONY: _venv
_venv:
	# Test to enforce venv usage across important make targets
	test "${SKIP_VENV}" || test "${PYTHON}" = "${PWD}/.venv/bin/python"



# ---------------------------------------
# Install requirements
# ---------------------------------------

PY_SYS_INTERPRETER ?=
ifeq ($(PY_SYS_INTERPRETER),)
	ifeq ($(OS),Windows_NT)
		PY_SYS_INTERPRETER += python3
	else
		PY_SYS_INTERPRETER += /usr/bin/python3
	endif
endif

PY_VIRTUAL_INTERPRETER ?= python
PIP ?= $(PY_VIRTUAL_INTERPRETER) -m pip

REQ_OPT := requirements-optional.txt
REQ_LINT := requirements-lint.txt
REQ_TEST := requirements-test.txt
REQ_TEST_OLD := requirements-test-old.txt

PIP_OPT_ARGS ?= $(shell if [ "$(SKIP_VENV)" ]; then echo "--user"; fi)

.PHONY: deps
deps: _venv	## Install requirements
	${PIP} install wheel
	- ${PIP} install ${PIP_OPT_ARGS} -r requirements.txt
	- ${PIP} install ${PIP_OPT_ARGS} -r ${REQ_OPT}
	${PIP} install ${PIP_OPT_ARGS} -r ${REQ_LINT}
	- ${PIP} install ${PIP_OPT_ARGS} -r ${REQ_TEST} || ${PIP} install ${PIP_OPT_ARGS} -r ${REQ_TEST_OLD}


# ---------------------------------------
# Format, lint, test
# ---------------------------------------

.PHONY: format
format: _venv	## Format with isort & black
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then isort ${CHANGED_FILES_PY} ; fi
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then black ${CHANGED_FILES_PY} ; fi


LINT_LOCS := ntclient/ tests/ setup.py
CHANGED_FILES_RST ?= $(shell git diff origin/main --name-only --diff-filter=MACRU \*.rst)
CHANGED_FILES_PY ?= $(shell git diff origin/main --name-only --diff-filter=MACRU \*.py)
CHANGED_FILES_PY_FLAG ?= $(shell if [ "$(CHANGED_FILES_PY)" ]; then echo 1; fi)

.PHONY: lint
lint: _venv	## Lint code and documentation
	# lint RST
	if [ "${CHANGED_FILES_RST}" ]; then doc8 --quiet ${CHANGED_FILES_RST}; fi
	# check formatting: Python
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then isort --diff --check ${CHANGED_FILES_PY} ; fi
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then black --check ${CHANGED_FILES_PY} ; fi
	# lint Python
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then pycodestyle --statistics ${CHANGED_FILES_PY}; fi
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then bandit -q -c .banditrc -r ${CHANGED_FILES_PY}; fi
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then flake8 ${CHANGED_FILES_PY}; fi
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then mypy ${CHANGED_FILES_PY}; fi
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then pylint ${CHANGED_FILES_PY}; fi

.PHONY: pylint
pylint:
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then pylint ${CHANGED_FILES_PY}; fi

.PHONY: mypy
mypy:
	if [ "${CHANGED_FILES_PY_FLAG}" ]; then mypy ${CHANGED_FILES_PY}; fi


# .PHONY: test
# test: _venv	## Run CLI unittests
# 	coverage run
# 	coverage report
# 	- grep fail_under setup.cfg



# ---------------------------------------
# Clean
# ---------------------------------------

RECURSIVE_CLEAN_LOCS ?= $(shell find ntclient/ tests/ \
-name __pycache__ \
-o -name .coverage \
-o -name .mypy_cache \
-o -name .pytest_cache)

.PHONY: clean
clean:	## Clean up __pycache__ and leftover bits
	rm -f .coverage
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/ .mypy_cache/
	# Recursively find & remove
	test "${RECURSIVE_CLEAN_LOCS}" && rm -rf ${RECURSIVE_CLEAN_LOCS}



# ---------------------------------------
# Extras
# ---------------------------------------

.PHONY: extras/cloc
extras/cloc:	## Count lines of source code
	- cloc HEAD
