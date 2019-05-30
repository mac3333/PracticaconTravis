def resolver(matrix, start, end):
    visited = set()
    solution_path = []

    def solve(matrix, start, end):

        visited.add(start)

        x, y = start
        a, b = end 

        if start == end:
            return True
        
        possible_next = []

        for dx in [-1, 0, 1]:

            for dy in [-1, 0, 1]:

                not_self_cell = (dx, dy) != (0, 0)
                horizontal_vertical = dx == 0 or dy == 0
                positivity = x + dx >= 0 and y + dy >= 0

                if not_self_cell and horizontal_vertical and positivity:
                    possible_next.append((x + dx, y + dy))

        possible = []
        for x, y in possible_next:

            inside_bounds = x < len(matrix[0]) and y < len(matrix) and matrix[x][y] is False
            is_visited = not (x, y) in visited

            if inside_bounds and is_visited :
                possible.append((x, y))

        for next_cell in possible:
            if solve(matrix, next_cell, end):
                solution_path.append(next_cell)
                return True       
        
        return False
    
    if solve(matrix, start, end):
        return [start] + solution_path[::-1]
    else:
        return "No tiene Solución"

