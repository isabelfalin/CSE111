from tracker import load_players, calculate_UTR
import pytest
from pytest import approx

def test_load_players():
    players_list = load_players("players.csv")
    assert len(players_list) == 24
    assert players_list[0][1] == "boye"

def test_calculate_UTR():
    players_list = load_players("players.csv")
    average_utr = calculate_UTR(players_list) 
    assert average_utr == approx(11.0, abs=0.1)

def test_get_qualifying_players():
    pass

pytest.main(["-v", "--tb=line", "-rN", __file__])