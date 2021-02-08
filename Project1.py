if __name__ == '__main__':
    N = 10
    grid = []
    lamp_info = {
        "is_on": 0,
        "illuminatinginstances": 0,
        "locations": []
    }
    for i in range(N):
        row = [] 
        for j in range(N):
            row.append(lamp_info.copy())
        grid.append(row())