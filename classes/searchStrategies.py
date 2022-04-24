class SearchStrategy:  # interface-abstract class
    def init_node(self, intial_state, compute_heuristic):
        pass

    def select_node(self, fringe):
        pass

    def add_node(self, current_node, action, next_state, compute_cost, compute_heuristic):
        pass

    def get_solution(self, current_node, complexity):
        pass

    def get_min(self, key, fringe):
        idx_min = 0
        for i in range(1, len(fringe)):
            if fringe[i][key] < fringe[idx_min][key]:
                idx_min = i
        return idx_min

    def get_path_rec(self, list):  # Stack overflows if we use it with DFS
        if len(list) == 0:
            return []
        else:
            return self.get_path_rec(list[0]) + [list[1]]

    def get_path(self, list):
        path = []
        while len(list) > 0:
            path.insert(0, list[1])
            list = list[0]
        return path


class DFS(SearchStrategy):
    def init_node(self, intial_state, compute_heuristic):
        initial_node = {}
        initial_node['state'] = intial_state
        initial_node['path'] = []
        return initial_node

    def select_node(self, fringe):
        return -1

    def add_node(self, current_node, action, next_state, compute_cost, compute_heuristic):
        next_node = {}
        next_node['state'] = next_state
        # next_node['path'] = current_node['path'][:]
        # next_node['path'].append(action)
        next_node['path'] = [current_node['path'], action]
        return next_node

    def get_solution(self, current_node, complexity):
        solution = {}
        # solution['solution'] = current_node['path']
        solution['solution'] = self.get_path(current_node['path'])
        solution['complexity'] = complexity
        return solution


class BFS(SearchStrategy):
    def init_node(self, intial_state, compute_heuristic):
        initial_node = {}
        initial_node['state'] = intial_state
        initial_node['path'] = []
        return initial_node

    def select_node(self, fringe):
        return 0

    def add_node(self, current_node, action, next_state, compute_cost, compute_heuristic):
        next_node = {}
        next_node['state'] = next_state
        # next_node['path'] = current_node['path'][:]
        # next_node['path'].append(action)
        next_node['path'] = [current_node['path'], action]
        return next_node

    def get_solution(self, current_node, complexity):
        solution = {}
        # solution['solution'] = current_node['path']
        solution['solution'] = self.get_path(current_node['path'])
        solution['complexity'] = complexity
        return solution


class UCS(SearchStrategy):
    def init_node(self, intial_state, compute_heuristic):
        initial_node = {}
        initial_node['state'] = intial_state
        initial_node['path'] = []
        initial_node['cost'] = 0
        return initial_node

    def select_node(self, fringe):
        return self.get_min('cost', fringe)

    def add_node(self, current_node, action, next_state, compute_cost, compute_heuristic):
        next_node = {}
        next_node['state'] = next_state
        # next_node['path'] = current_node['path'][:]
        # next_node['path'].append(action)
        next_node['path'] = [current_node['path'], action]
        next_node['cost'] = current_node['cost'] + compute_cost(action, current_node['state'])
        return next_node

    def get_solution(self, current_node, complexity):
        solution = {}
        # solution['solution'] = current_node['path']
        solution['solution'] = self.get_path(current_node['path'])
        solution['complexity'] = complexity
        solution['cost'] = current_node['cost']
        return solution


class Greedy(SearchStrategy):
    def init_node(self, intial_state, compute_heuristic):
        initial_node = {}
        initial_node['state'] = intial_state
        initial_node['path'] = []
        initial_node['heuristic'] = compute_heuristic(intial_state)
        return initial_node

    def select_node(self, fringe):
        return self.get_min('heuristic', fringe)

    def add_node(self, current_node, action, next_state, compute_cost, compute_heuristic):
        next_node = {}
        next_node['state'] = next_state
        # next_node['path'] = current_node['path'][:]
        # next_node['path'].append(action)
        next_node['path'] = [current_node['path'], action]
        next_node['heuristic'] = compute_heuristic(next_node['state'])
        return next_node

    def get_solution(self, current_node, complexity):
        solution = {}
        # solution['solution'] = current_node['path']
        solution['solution'] = self.get_path(current_node['path'])
        solution['complexity'] = complexity
        return solution


class Astar(SearchStrategy):
    def init_node(self, intial_state, compute_heuristic):
        initial_node = {}
        initial_node['state'] = intial_state
        initial_node['path'] = []
        initial_node['cost'] = 0
        initial_node['f'] = compute_heuristic(initial_node['state'])
        return initial_node

    def select_node(self, fringe):
        return self.get_min('f', fringe)

    def add_node(self, current_node, action, next_state, compute_cost, compute_heuristic):
        next_node = {}
        next_node['state'] = next_state
        # next_node['path'] = current_node['path'][:]
        # next_node['path'].append(action)
        next_node['path'] = [current_node['path'], action]
        next_node['cost'] = current_node['cost'] + compute_cost(action, current_node['state'])
        next_node['f'] = next_node['cost'] + compute_heuristic(next_node['state'])
        return next_node

    def get_solution(self, current_node, complexity):
        solution = {}
        # solution['solution'] = current_node['path']
        solution['solution'] = self.get_path(current_node['path'])
        solution['complexity'] = complexity
        solution['cost'] = current_node['cost']
        return solution
