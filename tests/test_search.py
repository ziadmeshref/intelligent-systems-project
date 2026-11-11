import pytest
from src.search import LayoutSearch

def test_greedy_search_simple():
    layout = {"A": {"demand": 900, "slot": 0}, "B": {"demand": 100, "slot": 1}}
    dist = {0: 1.0, 1: 5.0}
    searcher = LayoutSearch(layout, dist)
    res, swaps, exp, gen = searcher.greedy_best_first(target_cost=1000.0, max_swaps=2)
    assert res is not None
    assert swaps <= 2

def test_search_impossible_case():
    layout = {"A": {"demand": 900, "slot": 0}}
    dist = {0: 10.0}
    searcher = LayoutSearch(layout, dist)
    # Impossible target cost
    res, swaps, exp, gen = searcher.greedy_best_first(target_cost=1.0, max_swaps=1)
    assert res is not None # Returns best effort or triggers no solution message logic
