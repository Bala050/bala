import pytest
def test_first():
  assert True
@pytest.mark.xfail
def test_second():
  assert False
