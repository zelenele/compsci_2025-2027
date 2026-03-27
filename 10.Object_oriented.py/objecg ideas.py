class Chess_player:
    def __init__(self, age , elo , name):
        self.__age = age
        self.elo = elo
        self._name = name
    def GetAge(self):
        return self.__age 
    def SetAge(self, age):
        self.__age = age
        return age
player_1 = Chess_player(29, 2800, "magnus")
print(player_1._name)
print(player_1.GetAge())
print(player_1.SetAge(20))