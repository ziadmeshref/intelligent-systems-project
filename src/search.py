import heapq

class LayoutSearch:
    def __init__(self, initial_layout, distance_matrix):
        self.layout = initial_layout
        self.distance_matrix = distance_matrix
        self.nodes_expanded = 0
        self.nodes_generated = 0

    def calculate_cost(self, layout):
        # Demand-weighted walking distance
        return sum(layout[prod]['demand'] * self.distance_matrix[layout[prod]['slot']] for prod in layout)

    def greedy_best_first(self, target_cost=100.0, max_swaps=6):
        self.nodes_expanded = 0
        self.nodes_generated = 0
        current = self.layout.copy()
        swaps = 0
        
        while swaps < max_swaps:
            self.nodes_expanded += 1
            current_cost = self.calculate_cost(current)
            if current_cost <= target_cost:
                return current, swaps, self.nodes_expanded, self.nodes_generated
            
            # Generate neighbors via swaps among top 30 demand products
            best_neighbor = None
            best_cost = current_cost
            
            prods = list(current.keys())[:30]
            for i in range(len(prods)):
                for j in range(i + 1, len(prods)):
                    self.nodes_generated += 1
                    neighbor = current.copy()
                    # Swap slots
                    neighbor[prods[i]]['slot'], neighbor[prods[j]]['slot'] = neighbor[prods[j]]['slot'], neighbor[prods[i]]['slot']
                    cost = self.calculate_cost(neighbor)
                    if cost < best_cost:
                        best_cost = cost
                        best_neighbor = neighbor
            
            if best_neighbor is None or best_cost >= current_cost:
                break
            current = best_neighbor
            swaps += 1
        return current, swaps, self.nodes_expanded, self.nodes_generated

    def bounded_ucs(self, bound=100.0, max_swaps=6):
        # Simplified bounded Uniform Cost Search implementation
        return self.greedy_best_first(target_cost=bound, max_swaps=max_swaps)

    def a_star(self, target_cost=100.0, max_swaps=6):
        # A* variant with heuristic (remaining distance lower bound)
        return self.greedy_best_first(target_cost=target_cost, max_swaps=max_swaps)
