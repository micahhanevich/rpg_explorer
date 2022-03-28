import cmd
import sys
import os


class Game:

    def __init__(self):

        self.debug: bool = False

        self.basepath: str = os.getcwd() + '/world'
        self.curpath: str = ''
        self.formatpath: str = self.updateformatpath()

    def updateformatpath(self) -> str:
        self.formatpath: str = self.basepath[self.basepath.rfind('/', 0, len(self.basepath) - 1):] + self.curpath
        return self.basepath[self.basepath.rfind('/', 0, len(self.basepath) - 1):] + self.curpath


game = Game()


class GameFramework(cmd.Cmd):

    intro = 'RPG Explorer Test'
    prompt = f"""\n({game.formatpath})->"""

    def do_cd(self, arg):
        """Change active directories: cd world/continent/city/'potion shop'"""

        arg = '/' + arg

        if os.path.exists(game.basepath + game.curpath + arg):
            if game.debug: print(f"""{game.basepath + game.curpath + arg} exists""")
            if len(arg) > 1:
                game.curpath = game.curpath + arg
            else:
                game.curpath = ''
        else:
            print(f"""Cannot find {game.basepath + game.curpath + arg}; doesn't exist""")

    def do_dir(self, arg):
        print(f'{game.formatpath}:')
        print(os.listdir(game.basepath + game.curpath))

    def do_get(self, arg):
        if game.debug is False: print(f'*** Unknown syntax: get {arg}')
        else: print(str(getattr(game, str(arg))))

    def do_set(self, arg):
        if arg[0:5] != 'debug' and not game.debug: print(f'*** Unknown syntax: set {arg}')
        else:
            arg = arg.split(' ')
            setattr(game, str(arg[0]), arg[1])

    def postcmd(self, stop: bool, line: str) -> bool:
        game.updateformatpath()
        self.prompt = f"""({game.formatpath})->"""


gameframe = GameFramework()


gameframe.cmdloop()
