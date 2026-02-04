from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Isabel", "Falin") == "Falin; Isabel"
    assert make_full_name("Robert", "Jo-Mama") == "Jo-Mama; Robert"

def test_extract_family_name():
    assert extract_family_name("Falin; Isabel") == "Falin"
    assert extract_family_name("Hippy-Hoppy; Robbie") == "Hippy-Hoppy"

def test_extract_given_name():
    assert extract_given_name("Falin; Isabel") == "Isabel"
    assert extract_given_name("Smith; Happy-Moe") == "Happy-Moe"




pytest.main(["-v", "--tb=line", "-rN", __file__])