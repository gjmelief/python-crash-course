from ch11_ex03_employee import Employee

def test_give_default_raise():
    """Test that the default raise is given properly"""
    worker_0 = Employee('gert-jan', 'melief', 50000)
    worker_0.give_raise()
    assert worker_0.salary == 55000

def test_give_custom_raise():
    """Test that the default raise is given properly"""
    worker_0 = Employee('gert-jan', 'melief', 50000)
    worker_0.give_raise(10000)
    assert worker_0.salary == 60000