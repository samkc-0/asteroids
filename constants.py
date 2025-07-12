class Screen:
    WIDTH = 1280
    HEIGHT = 720


class Asteroid:
    MIN_RADIUS = 20
    # spawn rate in seconds:
    SPAWN_RATE = 0.8
    KINDS = 3
    MAX_RADIUS = MIN_RADIUS * KINDS


class Player:
    RADIUS = 20
    SPEED = 200
    TURN_SPEED = 360
    SHOT_RADIUS = 5
    SHOT_SPEED = 500
    SHOT_COOLDOWN = 0.3
