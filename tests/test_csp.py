import pytest
from src.csp import LayoutCSP

def test_csp_backtracking():
    vars = ["P1", "P2"]
    domains = {"P1": [0, 1], "P2": [0, 1]}
    csp = LayoutCSP(vars, domains, [])
    res = csp.backtracking_search()
    assert res is not None
    assert res["P1"] != res["P2"]

def test_csp_impossible_constraints():
    vars = ["P1", "P2"]
    domains = {"P1": [0], "P2": [0]} # Collision forced
    csp = LayoutCSP(vars, domains, [])
    res = csp.backtracking_search()
    assert res is None # Clear no solution result
