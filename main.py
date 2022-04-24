from classes.searchAgent import *
from classes.searchProblem import *
from classes.searchStrategies import *

if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.shuffle(40)
    print(puzzle.initial_state)

    # print('DFS solution.....')
    # DFS_sol = SearchAgent(puzzle, DFS()).solve()
    # for i in DFS_sol:
    #     print(i, DFS_sol[i])

    print('\nBFS solution.....')
    BFS_sol = SearchAgent(puzzle, BFS()).solve()
    for i in BFS_sol:
        print(i, BFS_sol[i])

    print('\nUCS solution.....')
    UCS_sol = SearchAgent(puzzle, UCS()).solve()
    for i in UCS_sol:
        print(i, UCS_sol[i])

    print('\nGreedy solution.....')
    Greedy_sol = SearchAgent(puzzle, Greedy()).solve()
    for i in Greedy_sol:
        print(i, Greedy_sol[i])

    print('\nAstar solution.....')
    Astar_sol = SearchAgent(puzzle, Astar()).solve()
    for i in Astar_sol:
        print(i, Astar_sol[i])
