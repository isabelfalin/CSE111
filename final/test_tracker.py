from tracker import load_players, calculate_UTR, does_player_qualify_for_tournament
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

    player_fake = ("manny", "loot", 0, "Male")
    average_utr = calculate_UTR([player_fake])
    assert average_utr == 0

def test_does_player_qualify_for_tournament():
    player = ["alex","boye",13.5,"Male"]
    tournament = ["Italian Open",12.5,"Male","May 7 2026"] 

    player2 = ["alex","boye",3,"Male"]
    tournament2 = ["Italian Open",12.5, "Female","May 72026 "] 

    #should not qualify cause of gender
    does_qualify = does_player_qualify_for_tournament(player, tournament2)
    assert does_qualify == False

    #shoudl qualify because of UTR and gender
    does_qualify = does_player_qualify_for_tournament(player, tournament)
    assert does_qualify == True

    #should not qualify cause UTR is too low
    does_qualify = does_player_qualify_for_tournament(player2, tournament2)
    assert does_qualify == False
    
pytest.main(["-v", "--tb=line", "-rN", __file__])