from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John", "Sena") == "Sena; John"
    assert make_full_name("Bobby-Mic-bum", "Suzy") == "Suzy; Bobby-Mic-bum"
    
def test_extract_family_name():
    assert extract_family_name("Cricket; Jiminey") == "Cricket"
    assert extract_family_name("Lady-eats-Bugs; Freep") == "Lady-eats-Bugs"

def test_extract_given_name():
    assert extract_given_name("Ross; Bob") == "Bob"
    assert extract_given_name("Jackson-has-lice; Percy") == "Percy"


    # Alternate form in case you need the result of the function later...
    name = extract_given_name("Ross; Bob")
    assert name == "Bob"

    print(name)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])