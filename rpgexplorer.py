import cmd
import sys


def parse_file_path(path: str) -> list[str]:
    return path.split('/')


class GameFramework(cmd.Cmd):
    intro = 'RPG Explorer Test'
    prompt = '->'

    def do_cd(self, arg):
        """Change active directories: cd world/continent/city/'potion shop'"""
        arg = parse_file_path(arg)


game = GameFramework()


game.cmdloop()