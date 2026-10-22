#!/usr/bin/env python3
"""
Flappy Bird on the Raspberry Pi Sense HAT (8x8 LED matrix).

Controls: BREATH. Blow on the Sense HAT to raise the humidity reading and
the bird rises. Stop blowing and it sinks.

There is no game over. If the bird is inside a pipe, it turns red, and
"whoops" prints in the terminal. When it gets out of the pipe, it goes
back to yellow and the game keeps going.

Game speed (pipe scroll rate) comes from the temperature sensor:
warmer board = faster game.
"""

import time
import random
from collections import deque
from sense_hat import SenseHat

BLACK = (0, 0, 0)
BIRD_COLOR = (255, 255, 0)   # yellow
HIT_COLOR = (255, 0, 0)      # red, shown while the bird is inside a pipe
PIPE_COLOR = (0, 200, 0)     # green
BIRD_X = 1
GAP_SIZE = 3

# Temperature -> tick interval (seconds). Warmer = faster.
TEMP_MIN, TEMP_MAX = 30.0, 34.0
TICK_MIN, TICK_MAX = 0.15, 0.5

# Humidity control
RISE_THRESHOLD = 1.5     # %RH above baseline needed to count as blowing
FALL_RATE = -0.3         # %RH per second; trend below this = stopped blowing
TREND_WINDOW = 0.8       # seconds of history used to measure the trend
SMOOTHING = 0.4          # 0..1, higher = less smoothing of raw readings
BASELINE_ALPHA = 0.01    # how fast the baseline follows the room
BIRD_SPEED = 0.5         # rows moved per game tick (up or down)
SAMPLE_INTERVAL = 0.1    # seconds between humidity readings


class FlappyBird:
    def __init__(self):
        self.hat = SenseHat()
        self.hat.clear()
        first = self.hat.get_humidity()
        self.baseline = first
        self.smoothed = first
        self.history = deque()   # (timestamp, smoothed humidity)
        self.blowing = False

        self.bird_y = 3.5
        self.pipes = [{"x": 7, "gap_y": 3}]
        self.frame = 0
        self.in_pipe = False
        self.was_in_pipe = False

    def tick_interval(self):
        temp = self.hat.get_temperature()
        clamped = max(TEMP_MIN, min(TEMP_MAX, temp))
        t = (clamped - TEMP_MIN) / (TEMP_MAX - TEMP_MIN)
        return TICK_MAX - t * (TICK_MAX - TICK_MIN)

    def sample_humidity(self):
        """Read the sensor and decide whether the player is blowing."""
        now = time.time()
        raw = self.hat.get_humidity()
        self.smoothed += SMOOTHING * (raw - self.smoothed)

        self.history.append((now, self.smoothed))
        while self.history and now - self.history[0][0] > TREND_WINDOW:
            self.history.popleft()

        # Trend in %RH per second over the recent window
        t0, h0 = self.history[0]
        elapsed = now - t0
        trend = (self.smoothed - h0) / elapsed if elapsed >= 0.3 else 0.0

        above = self.smoothed - self.baseline
        self.blowing = above >= RISE_THRESHOLD and trend > FALL_RATE

        # The baseline follows the room, but only very slowly while the
        # humidity is elevated so a breath doesn't get absorbed into it.
        alpha = BASELINE_ALPHA if above < RISE_THRESHOLD else BASELINE_ALPHA / 10
        self.baseline += alpha * (self.smoothed - self.baseline)

    def update_bird(self):
        if self.blowing:
            self.bird_y -= BIRD_SPEED      # up (row 0 is the top)
        else:
            self.bird_y += BIRD_SPEED      # down
        self.bird_y = max(0.0, min(7.0, self.bird_y))

    def bird_is_in_pipe(self):
        bird_row = round(self.bird_y)
        for pipe in self.pipes:
            if pipe["x"] == BIRD_X:
                if bird_row < pipe["gap_y"] or bird_row >= pipe["gap_y"] + GAP_SIZE:
                    return True
        return False

    def step(self):
        self.update_bird()
        self.frame += 1

        if self.frame % 6 == 0:
            for pipe in self.pipes:
                pipe["x"] -= 1
            if not self.pipes or self.pipes[-1]["x"] <= 3:
                self.pipes.append({
                    "x": 7,
                    "gap_y": random.randint(0, 8 - GAP_SIZE),
                })
            self.pipes = [p for p in self.pipes if p["x"] >= 0]

        self.in_pipe = self.bird_is_in_pipe()
        if self.in_pipe and not self.was_in_pipe:
            print("whoops")                # once each time the bird hits a pipe
        self.was_in_pipe = self.in_pipe

        self.draw()

    def draw(self):
        pixels = [BLACK] * 64

        for pipe in self.pipes:
            for y in range(8):
                in_gap = pipe["gap_y"] <= y < pipe["gap_y"] + GAP_SIZE
                if not in_gap and 0 <= pipe["x"] < 8:
                    pixels[y * 8 + pipe["x"]] = PIPE_COLOR

        by = max(0, min(7, round(self.bird_y)))
        pixels[by * 8 + BIRD_X] = HIT_COLOR if self.in_pipe else BIRD_COLOR

        self.hat.set_pixels(pixels)

    def run(self):
        # The sensor is sampled every SAMPLE_INTERVAL, independently of the
        # game tick, so the game reacts to a breath (or its end) sooner.
        try:
            next_step = time.time()
            while True:
                self.sample_humidity()
                if time.time() >= next_step:
                    self.step()
                    next_step = time.time() + self.tick_interval()
                time.sleep(SAMPLE_INTERVAL)
        except KeyboardInterrupt:
            self.hat.clear()


if __name__ == "__main__":
    FlappyBird().run()
