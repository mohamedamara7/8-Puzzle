from random import randrange


class SearchProblem:  # interface-abstract class
    def check_goal(self, state):
        pass

    def possible_actions(self, state):
        pass

    def new_state(self, action, state):
        pass

    def compute_cost(self, action, state):
        pass

    def compute_heuristic(self, state):
        pass


class Puzzle(SearchProblem):
    def __init__(self):
        self.initial_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def check_goal(self, state):
        for idx in range(len(state)):
            if state[idx] != idx:
                return False
        return True

    def finding_empty(self, puzzle):
        for idx in range(len(puzzle)):
            if puzzle[idx] == 0:
                return idx

    def possible_actions(self, state):
        moves = []
        empty_index = self.finding_empty(state)
        if empty_index - 3 >= 0:
            moves.append('^')
        if empty_index + 3 <= 8:
            moves.append('v')
        if empty_index != 2 and empty_index != 5 and empty_index != 8:
            moves.append('>')
        if empty_index != 0 and empty_index != 3 and empty_index != 6:
            moves.append('<')
        return moves

    def new_state(self, action, state):
        puzzle = state[:]
        empty_index = self.finding_empty(puzzle)
        if action == '^':
            puzzle[empty_index], puzzle[empty_index - 3] = puzzle[empty_index - 3], puzzle[empty_index]
        elif action == 'v':
            puzzle[empty_index], puzzle[empty_index + 3] = puzzle[empty_index + 3], puzzle[empty_index]
        elif action == '>':
            puzzle[empty_index], puzzle[empty_index + 1] = puzzle[empty_index + 1], puzzle[empty_index]
        else:
            puzzle[empty_index], puzzle[empty_index - 1] = puzzle[empty_index - 1], puzzle[empty_index]
        return puzzle

    def compute_cost(self, action, state):
        return 1

    def compute_heuristic(self, state):
        cnt = 0
        for i in range(len(state)):
            if state[i] != i:
                cnt += 1
        return cnt

    def compute_heuristic_2(self, state):
        cnt = 0
        for i in range(len(state)):
            cnt += abs(i // 3 - int(state[i] / 3)) + abs(i % 3 - state[i] % 3)
        return cnt

    def shuffle(self, n):
        for _ in range(n):
            actions = self.possible_actions(self.initial_state)
            rand_index = randrange(0, len(actions))
            self.initial_state = self.new_state(actions[rand_index], self.initial_state)
