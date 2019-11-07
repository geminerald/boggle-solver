def make_grid(width,height):
    """
    Make boggle grid that will hold all tiles for a game
    """
    return {(row,col): ' ' for row in range(height)
        for col in range(width)
    }