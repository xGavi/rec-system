class DataBase:
    def __init__(self, name: str) -> None:
        self.name = name
        self.games = []

    def __repr__(self) -> str:
        return str(self.games)

    def add(self, game):
        self.games.append(game)

    def searchT(self, tagFragment: str, tagPool=None) -> list:
        gamePool = []
        if tagPool is not None:
            for game in self.games:
                for tag in tagPool:
                    if tag in game.tags and game not in gamePool:
                        gamePool.append(game)
        else:
            gamePool = self.games
        tagList = []
        for game in gamePool:
            for tag in game.tags:
                if tagFragment.lower() in tag.lower() and tag not in tagList:
                    tagList.append(tag)
        return tagList

    def searchG(self, tagTarget: list, gamePool=None) -> list:
        if gamePool is None:
            gamePool = self.games
        gameList = []
        for game in gamePool:
            for tag in game.tags:
                for t in tagTarget:
                    if t.lower() in tag.lower() and game not in gameList:
                        gameList.append(game)
        return gameList

    def search(self, tagFragment: str, gamePool=None) -> list:
        return self.searchG(self.searchT(tagFragment, gamePool), gamePool)