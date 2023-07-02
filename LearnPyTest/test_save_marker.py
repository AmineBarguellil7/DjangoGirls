import pytest

@pytest.mark.skip
def test_save_marker():
    print("marker added successfully")



@pytest.mark.xfail
def testcalculateur():
    assert 2 + 2 == 5