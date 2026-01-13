COVERAGE_DIR = htmlcov

.PHONY: test-coverage
test-coverage:
	coverage run -m pytest
	coverage html
	python3 -m webbrowser $(COVERAGE_DIR)/index.html

.PHONY: pylint
pylint: ## Run pylint verification locally
	pylint --rcfile=.pylintrc gilded_rose.py
