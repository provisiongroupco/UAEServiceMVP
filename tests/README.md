# Halton KSA Service Reports - Testing Documentation

This document provides comprehensive information about the testing framework for the Halton KSA Service Reports application.

## Table of Contents

1. [Overview](#overview)
2. [Test Structure](#test-structure)
3. [Running Tests](#running-tests)
4. [Test Types](#test-types)
5. [Test Coverage](#test-coverage)
6. [Writing Tests](#writing-tests)
7. [Continuous Integration](#continuous-integration)
8. [Troubleshooting](#troubleshooting)

## Overview

The testing framework ensures the reliability and functionality of the Halton KSA Service Reports application. It includes:

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions and workflows
- **Fixtures**: Reusable test data and mock objects
- **Coverage Reports**: Track code coverage metrics
- **Automated Testing**: CI/CD pipeline integration

## Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Pytest configuration and fixtures
├── test_runner.py           # Custom test runner
├── unit/                    # Unit tests
│   ├── __init__.py
│   ├── test_equipment_config.py
│   ├── test_utils.py
│   ├── test_app_core.py
│   ├── test_equipment_inspection.py
│   └── test_sample_report_generator.py
├── integration/             # Integration tests
│   ├── __init__.py
│   └── test_report_generation.py
└── fixtures/                # Test data and fixtures
    ├── __init__.py
    └── test_data.py
```

## Running Tests

### Prerequisites

1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest coverage
   ```

2. Ensure you're in the project root directory

### Using Make Commands

The project includes a Makefile with convenient test commands:

```bash
# Run all tests
make test

# Run unit tests only
make test-unit

# Run integration tests only
make test-int

# Run tests with coverage
make test-cov

# Run fast tests (exclude slow tests)
make test-fast

# Check test suite health
make test-health

# Run with pytest
make pytest

# Run pytest with coverage
make pytest-cov
```

### Using Custom Test Runner

The custom test runner provides additional features:

```bash
# Run all tests
python tests/test_runner.py

# Run specific test types
python tests/test_runner.py --type unit
python tests/test_runner.py --type integration

# Run with verbose output
python tests/test_runner.py --verbose

# Run with coverage
python tests/test_runner.py --coverage

# Run specific test
python tests/test_runner.py --specific test_equipment_config.TestEquipmentConfig.test_equipment_types_structure

# Check test health
python tests/test_runner.py --health
```

### Using Pytest Directly

```bash
# Run all tests
pytest

# Run specific test directory
pytest tests/unit
pytest tests/integration

# Run with coverage
pytest --cov=. --cov-report=html

# Run with markers
pytest -m "not slow"
pytest -m integration
pytest -m unit

# Run specific test file
pytest tests/unit/test_equipment_config.py

# Run specific test method
pytest tests/unit/test_equipment_config.py::TestEquipmentConfig::test_equipment_types_structure
```

## Test Types

### Unit Tests

Unit tests focus on testing individual components in isolation:

- **test_equipment_config.py**: Tests equipment configuration data structure
- **test_utils.py**: Tests utility functions for document generation
- **test_app_core.py**: Tests core application functions
- **test_equipment_inspection.py**: Tests equipment inspection functionality
- **test_sample_report_generator.py**: Tests sample report generation

### Integration Tests

Integration tests verify component interactions:

- **test_report_generation.py**: Tests complete report generation workflow

### Test Markers

Tests are marked with pytest markers for organization:

- `@pytest.mark.unit`: Unit tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.slow`: Slow tests (performance tests)

## Test Coverage

### Generating Coverage Reports

```bash
# Generate HTML coverage report
pytest --cov=. --cov-report=html

# Generate terminal coverage report
pytest --cov=. --cov-report=term-missing

# Generate XML coverage report (for CI)
pytest --cov=. --cov-report=xml
```

### Coverage Targets

- **Overall Coverage**: Target 80%+
- **Critical Components**: Target 90%+
- **Equipment Config**: Target 95%+
- **Report Generation**: Target 85%+

## Writing Tests

### Test Structure

Follow this structure for new tests:

```python
import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from module_to_test import function_to_test

class TestModuleName(unittest.TestCase):
    """Test cases for module_name"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data = {}
    
    def test_function_name(self):
        """Test function description"""
        # Arrange
        input_data = "test_input"
        expected_output = "expected_output"
        
        # Act
        result = function_to_test(input_data)
        
        # Assert
        self.assertEqual(result, expected_output)
    
    def tearDown(self):
        """Clean up after tests"""
        pass

if __name__ == '__main__':
    unittest.main()
```

### Using Fixtures

Import and use fixtures from `tests/fixtures/`:

```python
from tests.fixtures import BASIC_REPORT_DATA, TEST_EQUIPMENT_KVF

def test_with_fixture(self):
    """Test using fixture data"""
    result = process_report_data(BASIC_REPORT_DATA)
    self.assertIsNotNone(result)
```

### Mocking Streamlit

Use the provided mock fixtures for Streamlit:

```python
@patch('module.st')
def test_streamlit_function(self, mock_st):
    """Test function that uses Streamlit"""
    mock_st.selectbox.return_value = 'Yes'
    mock_st.session_state = {}
    
    result = streamlit_function()
    
    mock_st.selectbox.assert_called_once()
```

### Testing Guidelines

1. **Test Organization**: Group related tests in classes
2. **Test Naming**: Use descriptive test names that explain what is being tested
3. **Test Independence**: Each test should be independent and not rely on others
4. **Mocking**: Mock external dependencies (files, APIs, Streamlit components)
5. **Edge Cases**: Test edge cases and error conditions
6. **Performance**: Mark slow tests with `@pytest.mark.slow`

## Continuous Integration

### GitHub Actions Integration

The project supports CI/CD with these commands:

```bash
# Run tests for CI
make ci-test

# Run linting for CI
make ci-lint
```

### Test Configuration

CI configuration should:
1. Install dependencies
2. Run all tests
3. Generate coverage reports
4. Report results

Example GitHub Actions workflow:

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest coverage
    - name: Run tests
      run: make ci-test
    - name: Upload coverage
      uses: codecov/codecov-action@v1
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure you're in the project root directory
   - Check that all required dependencies are installed
   - Verify Python path configuration

2. **Mock Issues**
   - Ensure proper patching of external dependencies
   - Use `MagicMock` for complex objects
   - Reset mocks between tests

3. **Streamlit Testing**
   - Mock all Streamlit components
   - Use session state fixtures
   - Mock file operations

4. **Coverage Issues**
   - Ensure all source files are included in coverage
   - Check for missing test cases
   - Review coverage reports regularly

### Test Debugging

1. **Run Single Test**
   ```bash
   pytest tests/unit/test_equipment_config.py::TestEquipmentConfig::test_equipment_types_structure -v
   ```

2. **Debug with Print Statements**
   ```python
   def test_debug_example(self):
       result = function_to_test()
       print(f"Debug: result = {result}")
       self.assertIsNotNone(result)
   ```

3. **Use Debugger**
   ```python
   import pdb
   
   def test_with_debugger(self):
       pdb.set_trace()
       result = function_to_test()
       self.assertIsNotNone(result)
   ```

### Performance Testing

For performance-critical tests:

```bash
# Run performance tests
pytest -m slow --durations=10

# Profile test execution
pytest --profile
```

## Best Practices

1. **Test Early and Often**: Write tests as you develop features
2. **Keep Tests Simple**: Each test should verify one specific behavior
3. **Use Descriptive Names**: Test names should clearly indicate what is being tested
4. **Mock External Dependencies**: Don't rely on external services or files
5. **Test Edge Cases**: Include tests for boundary conditions and error scenarios
6. **Maintain Test Data**: Keep test fixtures up to date with code changes
7. **Review Coverage**: Regularly check coverage reports and improve test coverage
8. **Document Complex Tests**: Add comments explaining complex test scenarios

## Contributing

When adding new features or fixing bugs:

1. Write tests for new functionality
2. Ensure all existing tests pass
3. Maintain or improve test coverage
4. Update test documentation as needed
5. Follow the established testing patterns and conventions

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [coverage.py documentation](https://coverage.readthedocs.io/)
- [Python mocking guide](https://docs.python.org/3/library/unittest.mock.html)