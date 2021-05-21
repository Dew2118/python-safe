import curses
from package.Game import Game
from time import sleep


def main(stdscr):
    curses.echo()
    a = Game(stdscr)
    a.play()
    sleep(3)

if __name__ == '__main__':
    curses.wrapper(main)