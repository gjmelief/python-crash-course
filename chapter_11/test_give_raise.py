import pytest
from ch11_ex03_employee import Employee

@pytest.fixture
def employee():
    """A worker that can be used for all test functions."""
    employee = Employee('gert-jan', 'melief', 50000)
    return employee

def test_give_default_raise(employee):
    """Test that the default raise is given properly."""
    employee.give_raise()
    assert employee.salary == 55000

def test_give_custom_raise(employee):
    """Test that the custom raise is given properly."""
    employee.give_raise(10000)
    assert employee.salary == 60000