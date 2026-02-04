from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("3046 Cottonwood Lane, Marion, VA 77890") == "Marion"

def test_extract_stat():
    assert extract_state(" 525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("3046 Cottonwood Lane, Marion, VA 77890") == "VA"

def test_extract_zipcode():
    assert extract_zipcode(" 525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("3046 Cottonwood Lane, Marion, VA 77890") == "77890"

pytest.main(["-v", "--tb=line", "-rN", __file__])