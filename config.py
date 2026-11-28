import math
# Game
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
FPS = 60

# Player
PLAYER_RADIUS = 10
PLAYER_COLOR = (0, 255, 0)

PLAYER_MAX_VELOCITY = 700
PLAYER_RESPONSIVENESS = 15

# Map
MAP_COLOR = (60, 97, 122)
GRID_SIZE = 100
g = math.gcd(SCREEN_WIDTH, SCREEN_HEIGHT)

divisors = []
for i in range(1, math.isqrt(g) + 1):
    if g % i == 0:
        divisors += [i, g // i]

GRID_SIZE = min(divisors, key=lambda d: (abs(d - GRID_SIZE), d))
LINE_COLOR = (127, 127, 127)
LINE_WIDTH = 3