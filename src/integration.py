from src.nn import DemandPredictor
from src.csp import LayoutCSP
from src.search import LayoutSearch
import numpy as np

class WarehousePipeline:
    def __init__(self):
        self.nn_model = DemandPredictor()

    def forecast_demand(self):
        # Simulated demand dictionary for 120 products
        return {f"Prod_{i}": np.random.randint(50, 1000) for i in range(120)}

    def generate_initial_layout(self, demand):
        sorted_prods = sorted(demand.keys(), key=lambda k: demand[k], reverse=True)
        # Map to slots near depot
        layout = {prod: {"demand": demand[prod], "slot": i} for i, prod in enumerate(sorted_prods)}
        return layout

    def optimize_layout_with_search(self, layout):
        distance_matrix = {i: i * 1.5 for i in range(120)}
        searcher = LayoutSearch(layout, distance_matrix)
        final_layout, swaps, nodes_exp, nodes_gen = searcher.greedy_best_first(target_cost=10.0, max_swaps=6)
        return final_layout

    def evaluate_picker_distance(self, layout):
        # Simulate picker travel distance over 10 test weeks
        return [np.random.uniform(500, 1200) for _ in range(10)]
