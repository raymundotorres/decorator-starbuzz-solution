import pytest
from starbuzz.dark_roast import DarkRoast
from starbuzz.espresso import Espresso
from starbuzz.mocha import Mocha
from starbuzz.soy import Soy
from starbuzz.whip import Whip

def test_base():
    d=Espresso(); assert d.description()=="Espresso"; assert d.cost()==pytest.approx(1.99)

def test_stack():
    d=Whip(Mocha(DarkRoast()))
    assert d.description()=="Dark Roast, Mocha, Whip"
    assert d.cost()==pytest.approx(1.29)

def test_runtime_combination():
    d=Mocha(Soy(Espresso()))
    assert d.description()=="Espresso, Soy, Mocha"
    assert d.cost()==pytest.approx(2.34)
