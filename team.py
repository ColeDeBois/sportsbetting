from abc import abstractmethod


class Player:
    def __init__(self,stats,name) -> None:
        self.stats=stats
        self.name=name
    def __str__(self) -> str:
        return self.name
    @abstractmethod
    def bench(self):
        pass

class Pitcher(Player):
    def __init__(self) -> None:
        self.pthrown=0
        pass
    def __repr__(self) -> str:
        pass

class Batter(Player):
    def __init__(self) -> None:
        pass
    def __repr__(self) -> str:
        pass
    @property
    def bavg(self) -> float:
        pass
    @property
    def rbi(self) -> float:
        pass


class Team:
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        return self.__str__()
    @property
    def batting_order(self) -> list:
        pass
    @property
    def pitcher(self) -> Pitcher:
        pass
    @property
    def at_bat(self) -> Batter:
        pass

