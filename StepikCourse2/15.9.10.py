def in_ball_check(coordinates):
    is_in_ball = all(map(lambda coords: coords[0]**2 + coords[1]**2 + coords[2]**2 <= 4, coordinates))

    return is_in_ball


abscissas, ordinates, appliques = [map(float, input().split()) for i in range(3)]
coordinates = zip(abscissas, ordinates, appliques)

print(in_ball_check(coordinates))