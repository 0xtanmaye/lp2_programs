import heapq  # For priority queue (min-heap)

# ─────────────────────────────────────────
#  GOAL STATE (what we want to reach)
# ─────────────────────────────────────────
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)   # 0 = blank tile

# ─────────────────────────────────────────
#  HEURISTIC: Misplaced Tiles
#  Count how many tiles are NOT in their
#  goal position (ignore blank tile = 0)
# ─────────────────────────────────────────
def heuristic(state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != GOAL[i])

# ─────────────────────────────────────────
#  GET NEIGHBOURS
#  Slide blank tile (0) Up/Down/Left/Right
# ─────────────────────────────────────────
def get_neighbours(state):
    neighbours = []
    state = list(state)
    i = state.index(0)        # find blank tile position
    row, col = divmod(i, 3)   # convert index to (row, col)

    # (direction_name, row_change, col_change)
    moves = [("Up", -1, 0), ("Down", 1, 0),
             ("Left", 0, -1), ("Right", 0, 1)]

    for _, dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:   # within grid?
            j = new_row * 3 + new_col                # new blank position
            new_state = state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]  # swap
            neighbours.append(tuple(new_state))

    return neighbours

# ─────────────────────────────────────────
#  A* SEARCH
#  f(n) = g(n) + h(n)
#  g = steps taken so far
#  h = heuristic (misplaced tiles)
# ─────────────────────────────────────────
def a_star(start):
    # Each heap entry: (f, g, state, path)
    h = heuristic(start)
    heap = [(h, 0, start, [start])]   # initial node
    visited = set()                   # closed list

    while heap:
        f, g, state, path = heapq.heappop(heap)  # pop node with lowest f

        if state == GOAL:
            return path   # Found solution!

        if state in visited:
            continue
        visited.add(state)

        # Expand neighbours
        for neighbour in get_neighbours(state):
            if neighbour not in visited:
                new_g = g + 1                    # one more step
                new_h = heuristic(neighbour)
                new_f = new_g + new_h            # f = g + h
                heapq.heappush(heap, (new_f, new_g, neighbour, path + [neighbour]))

    return None  # No solution found

# ─────────────────────────────────────────
#  PRINT HELPER
# ─────────────────────────────────────────
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# ─────────────────────────────────────────
#  MAIN — Run it!
# ─────────────────────────────────────────
start = (1, 3, 2,
         4, 0, 5,
         7, 6, 8)

solution = a_star(start)

if solution:
    print(f"Solution found in {len(solution)-1} moves:\n")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        print_state(state)
else:
    print("No solution exists.")
