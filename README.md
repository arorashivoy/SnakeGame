# Snake Game

The classic snake game, written in Python with pygame.

> A short gameplay GIF belongs here — it is what turns an unopened `.py` file into
> something a visitor can judge in two seconds.

## Running it

```sh
pip install pygame
python3 SnakeGame.py
```

## Controls

| Key | Action |
|---|---|
| Arrow keys, or `W` `A` `S` `D` | steer |
| `Space` | pause and resume |
| `Q` | quit |

The snake cannot be steered back into itself: a direction opposite to the current
one is ignored unless the snake is still a single segment long.
