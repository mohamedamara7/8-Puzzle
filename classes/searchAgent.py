class SearchAgent:
    def __init__(self, search_problem, search_strategy):
        self.search_problem = search_problem
        self.search_strategy = search_strategy

    def solve(self):
        fringe = []
        visited = []
        initial_node = self.search_strategy.init_node(self.search_problem.initial_state,
                                                      self.search_problem.compute_heuristic)
        fringe.append(initial_node)
        while len(fringe) > 0:
            current_node = fringe.pop(self.search_strategy.select_node(fringe))
            if current_node['state'] in visited: continue
            visited.append(current_node['state'])
            if self.search_problem.check_goal(current_node['state']):
                return self.search_strategy.get_solution(current_node, len(visited))
            possible_actions = self.search_problem.possible_actions(current_node['state'])
            for action in possible_actions:
                next_state = self.search_problem.new_state(action, current_node['state'])
                next_node = self.search_strategy.add_node(current_node, action, next_state,
                                                          self.search_problem.compute_cost,
                                                          self.search_problem.compute_heuristic)
                fringe.append(next_node)
        return None
