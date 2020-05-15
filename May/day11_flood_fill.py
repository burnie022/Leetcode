def floodFill(image, sr: int, sc: int, newColor: int):
    color_to_change = image[sr][sc]
    if color_to_change == newColor:
        return image

    def pixelChanger(y,x):
        if (y >= 0 and y < len(image) and
                x >= 0 and x < len(image[0])):
            if image[y][x] == color_to_change:
                image[y][x] = newColor

                r = [[-1, 0],[1, 0],[0, -1],[0, 1]]
                for a, b in r:
                    pixelChanger(y + a, x + b)

    pixelChanger(sr, sc)

    return image

# For testing
im = [[0,0,0],[0,1,1]]
    [[1, 0, 0, 0, 0, 0, 1, 1],
      [1, 1, 0, 0, 0, 1, 0, 1],
      [1, 0, 0, 1, 0, 0, 0, 1],
      [1, 2, 2, 2, 2, 0, 1, 1],
      [1, 1, 1, 2, 2, 0, 0, 1],
      [1, 0, 1, 0, 2, 0, 2, 1],
      [1, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1]]

    # [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 0, 0],[1, 0, 0, 1, 1, 0, 1, 1],[1, 2, 2, 2, 2, 0, 1, 0],
    #   [1, 1, 1, 2, 2, 0, 1, 0],[1, 1, 1, 2, 2, 2, 2, 0],[1, 1, 1, 1, 1, 2, 1, 1],[1, 1, 1, 1, 1, 2, 2, 1]]
sr = 1
sc = 1
new_c = 1

nm = floodFill(im, sr, sc, new_c)
for line in nm:
    print(line)
