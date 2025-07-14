"""
Test runner for Halton KSA Service Reports application
"""

import unittest
import sys
import os
from pathlib import Path
import argparse
import time

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestRunner:
    """Test runner for the application"""
    
    def __init__(self):
        self.test_dir = Path(__file__).parent
        self.unit_test_dir = self.test_dir / 'unit'
        self.integration_test_dir = self.test_dir / 'integration'
        
    def discover_tests(self, test_type='all'):
        """Discover tests based on type"""
        if test_type == 'unit':
            return unittest.TestLoader().discover(str(self.unit_test_dir), pattern='test_*.py')
        elif test_type == 'integration':
            return unittest.TestLoader().discover(str(self.integration_test_dir), pattern='test_*.py')
        else:
            return unittest.TestLoader().discover(str(self.test_dir), pattern='test_*.py')
    
    def run_tests(self, test_type='all', verbose=False):
        """Run tests and return results"""
        print(f"Running {test_type} tests...")
        print("=" * 60)
        
        # Discover tests
        test_suite = self.discover_tests(test_type)
        
        # Configure test runner
        verbosity = 2 if verbose else 1
        runner = unittest.TextTestRunner(verbosity=verbosity, stream=sys.stdout)
        
        # Run tests
        start_time = time.time()
        result = runner.run(test_suite)
        end_time = time.time()
        
        # Print summary
        print("\n" + "=" * 60)
        print(f"Test run completed in {end_time - start_time:.2f} seconds")
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
        
        return result
    
    def run_specific_test(self, test_module, test_class=None, test_method=None):
        """Run a specific test"""
        if test_class and test_method:
            test_name = f"{test_module}.{test_class}.{test_method}"
        elif test_class:
            test_name = f"{test_module}.{test_class}"
        else:
            test_name = test_module
        
        print(f"Running specific test: {test_name}")
        print("=" * 60)
        
        # Load and run the specific test
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(test_name)
        
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        return result
    
    def run_with_coverage(self, test_type='all'):
        """Run tests with coverage reporting"""
        try:
            import coverage
        except ImportError:
            print("Coverage package not found. Install with: pip install coverage")
            return False
        
        print(f"Running {test_type} tests with coverage...")
        print("=" * 60)
        
        # Start coverage
        cov = coverage.Coverage(source=['.'])
        cov.start()
        
        # Run tests
        result = self.run_tests(test_type)
        
        # Stop coverage and generate report
        cov.stop()
        cov.save()
        
        print("\nCoverage Report:")
        print("=" * 60)
        cov.report()
        
        # Generate HTML report
        cov.html_report(directory='tests/coverage_html')
        print("\nHTML coverage report generated in tests/coverage_html/")
        
        return result.wasSuccessful()
    
    def check_test_health(self):
        """Check the health of the test suite"""
        print("Checking test suite health...")
        print("=" * 60)
        
        issues = []
        
        # Check if test directories exist
        if not self.unit_test_dir.exists():
            issues.append("Unit test directory not found")
        
        if not self.integration_test_dir.exists():
            issues.append("Integration test directory not found")
        
        # Check for test files
        unit_tests = list(self.unit_test_dir.glob('test_*.py'))
        integration_tests = list(self.integration_test_dir.glob('test_*.py'))
        
        if not unit_tests:
            issues.append("No unit test files found")
        
        if not integration_tests:
            issues.append("No integration test files found")
        
        # Check for __init__.py files
        if not (self.test_dir / '__init__.py').exists():
            issues.append("Missing __init__.py in tests directory")
        
        if not (self.unit_test_dir / '__init__.py').exists():
            issues.append("Missing __init__.py in unit tests directory")
        
        if not (self.integration_test_dir / '__init__.py').exists():
            issues.append("Missing __init__.py in integration tests directory")
        
        # Check for fixtures
        fixtures_dir = self.test_dir / 'fixtures'
        if not fixtures_dir.exists():
            issues.append("Fixtures directory not found")
        
        # Report findings
        if issues:
            print("Issues found:")
            for issue in issues:
                print(f"  - {issue}")
            return False
        else:
            print("Test suite health check passed!")
            print(f"Found {len(unit_tests)} unit test files")
            print(f"Found {len(integration_tests)} integration test files")
            return True


def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(description='Run tests for Halton KSA Service Reports')
    parser.add_argument('--type', choices=['unit', 'integration', 'all'], 
                       default='all', help='Type of tests to run')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Verbose output')
    parser.add_argument('--coverage', action='store_true',
                       help='Run with coverage reporting')
    parser.add_argument('--health', action='store_true',
                       help='Check test suite health')
    parser.add_argument('--specific', help='Run specific test (module.class.method)')
    
    args = parser.parse_args()
    
    runner = TestRunner()
    
    if args.health:
        success = runner.check_test_health()
        sys.exit(0 if success else 1)
    
    if args.specific:
        parts = args.specific.split('.')
        if len(parts) == 1:
            result = runner.run_specific_test(parts[0])
        elif len(parts) == 2:
            result = runner.run_specific_test(parts[0], parts[1])
        elif len(parts) == 3:
            result = runner.run_specific_test(parts[0], parts[1], parts[2])
        else:
            print("Invalid test specification. Use: module.class.method")
            sys.exit(1)
    elif args.coverage:
        success = runner.run_with_coverage(args.type)
        sys.exit(0 if success else 1)
    else:
        result = runner.run_tests(args.type, args.verbose)
        sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    main()