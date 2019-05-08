VERSION=$(shell grep __version__ periodo_umbrella_periods_cli/__init__.py)
REQUIREMENTS="requirements.txt"
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

build:
	@echo $(TAG)Building Production Package$(END)
	python setup.py sdist bdist_wheel

clean:
	@echo $(TAG)Cleaning Up Build Resources$(END)
	rm -rf .tox *.egg *.egg-info dist build .coverage ./periodo_umbrella_periods_cli/data/
	find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	@echo

fetch-data:
	@echo $(TAG)Downloading Production PeriodO Definitions$(END)
	curl -L http://n2t.net/ark:/99152/p0d.json > ./periodo_umbrella_periods_cli/data/p0d.json
	@echo "Done"

fetch-data-staging:
	@echo $(TAG)Downloading Staging PeriodO Definitions$(END)
	curl -L https://staging.perio.do/d.jsonld > ./periodo_umbrella_periods_cli/data/p0d.staging.json
	@echo "Done"

fetch-data-test:
	@echo $(TAG)Downloading Test PeriodO Definitions$(END)
	curl -L https://test.perio.do/d.jsonld > ./periodo_umbrella_periods_cli/data/p0d.test.json
	@echo "Done"

init: uninstall install

install:
	@echo $(TAG)Installing production requirements$(END)
	pip install --upgrade -r $(REQUIREMENTS)

	@echo $(TAG)Installing PeriodO Umbrella Periods CLI$(END)
	pip install --upgrade --editable .

	@echo

publish: build push-to-pypi clean

publish-test: build push-to-pypi-test clean

push-to-pypi:
	pip install 'twine>=1.5.0'
	twine upload dist/*

push-to-pypi-test:
	pip install 'twine>=1.5.0'
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

uninstall:
	@echo $(TAG)Uninstalling PeriodO Umbrella Periods CLI$(END)
	- pip uninstall --yes periodo_umbrella_periods_cli &2>/dev/null

	@echo "Verifying…"
	cd .. && ! python -m periodo_umbrella_periods_cli --version &2>/dev/null

	@echo "Done"
	@echo