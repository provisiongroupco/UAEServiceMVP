# Makefile for Halton KSA Service Reports

# Variables
PYTHON = python
PIP = pip
VENV = venv
PYTEST = pytest
COVERAGE = coverage

# Default target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  setup       - Set up virtual environment and install dependencies"
	@echo "  test        - Run all tests"
	@echo "  test-unit   - Run unit tests only"
	@echo "  test-int    - Run integration tests only"
	@echo "  test-cov    - Run tests with coverage"
	@echo "  test-fast   - Run fast tests (exclude slow tests)"
	@echo "  test-health - Check test suite health"
	@echo "  lint        - Run code linting"
	@echo "  format      - Format code"
	@echo "  clean       - Clean up generated files"
	@echo "  install     - Install dependencies"
	@echo "  run         - Run the application"
	@echo "  sample      - Generate sample report"

# Setup
.PHONY: setup
setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
	$(VENV)/bin/pip install pytest coverage flake8 black mypy

# Install dependencies
.PHONY: install
install:
	$(PIP) install -r requirements.txt

# Testing
.PHONY: test
test:
	$(PYTHON) tests/test_runner.py --type all --verbose

.PHONY: test-unit
test-unit:
	$(PYTHON) tests/test_runner.py --type unit --verbose

.PHONY: test-int
test-int:
	$(PYTHON) tests/test_runner.py --type integration --verbose

.PHONY: test-cov
test-cov:
	$(PYTHON) tests/test_runner.py --type all --coverage

.PHONY: test-fast
test-fast:
	$(PYTEST) -m "not slow" -v

.PHONY: test-health
test-health:
	$(PYTHON) tests/test_runner.py --health

# Pytest targets
.PHONY: pytest
pytest:
	$(PYTEST) -v

.PHONY: pytest-unit
pytest-unit:
	$(PYTEST) tests/unit -v

.PHONY: pytest-int
pytest-int:
	$(PYTEST) tests/integration -v

.PHONY: pytest-cov
pytest-cov:
	$(PYTEST) --cov=. --cov-report=html --cov-report=term-missing

# Code quality
.PHONY: lint
lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

.PHONY: format
format:
	black . --line-length=100
	isort . --profile=black

.PHONY: typecheck
typecheck:
	mypy . --ignore-missing-imports

# Application
.PHONY: run
run:
	streamlit run app.py

.PHONY: sample
sample:
	$(PYTHON) sample_report_generator.py

# Cleanup
.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf tests/__pycache__
	rm -rf tests/unit/__pycache__
	rm -rf tests/integration/__pycache__
	rm -rf tests/fixtures/__pycache__
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf tests/coverage_html
	rm -rf .mypy_cache
	rm -f Sample_Technical_Report_*.docx
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# Development
.PHONY: dev-setup
dev-setup: setup
	$(VENV)/bin/pip install -e .

.PHONY: dev-install
dev-install:
	$(PIP) install pytest coverage flake8 black mypy isort

# Documentation
.PHONY: docs
docs:
	@echo "Generating documentation..."
	@echo "Test coverage report available at: tests/coverage_html/index.html"
	@echo "Run 'make test-cov' to generate coverage report"

# CI/CD helpers
.PHONY: ci-test
ci-test:
	$(PYTEST) --junitxml=test-results.xml --cov=. --cov-report=xml

.PHONY: ci-lint
ci-lint:
	flake8 . --format=junit-xml --output-file=lint-results.xml

# Database/File operations
.PHONY: clean-reports
clean-reports:
	rm -f *.docx
	rm -f Technical_Report_*.docx
	rm -f Sample_Technical_Report_*.docx

# Backup
.PHONY: backup
backup:
	tar -czf backup_$(shell date +%Y%m%d_%H%M%S).tar.gz \
		--exclude='$(VENV)' \
		--exclude='__pycache__' \
		--exclude='.pytest_cache' \
		--exclude='htmlcov' \
		--exclude='*.pyc' \
		--exclude='*.pyo' \
		.

# Performance testing
.PHONY: perf-test
perf-test:
	$(PYTEST) -m slow -v --durations=0