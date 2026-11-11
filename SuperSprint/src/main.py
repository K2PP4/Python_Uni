from lib.g2d import init_canvas, main_loop
from func.movement import tick
from .enum.arenasize import Arena_size

def main():
    init_canvas(Arena_size.dim.value)
    main_loop(tick())

if __name__ == "__main__":
    print("main file started")
    main()