default: help

source:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

publish: source wheel
	twine upload dist/*

test:
	tox

clean:
	rm -rf build dist {{ cookiecutter.package_name }}.egg-info

help:
	@egrep '^[a-z]+:' Makefile | awk -F: '{print $$1}' | sort

.PHONY: default source wheel publish test clean help
