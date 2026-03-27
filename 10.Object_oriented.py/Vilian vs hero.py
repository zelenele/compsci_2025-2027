class Character:
    def __init__(self, name, strenght, health):
        self.__strenght = strenght
        self.__health = health
        self.__name = name
    def get_health(self):
        return self.__health
    
    def get_streght(self,):
        return self.__strenght
    def get_name(self,):
        return self.__name
    def set_health(self, health):
        self.__health = health 
        if health <= 0:
            self.__health = 0
        else:
            self.__health = health
    def take_damage(self,damage):
        current_health = self.__health 
        self.set_health(current_health - damage)
    def is_alive(self):
        if self.__health <= 0:
            return False
        else:
            return True
        
hero = Character("Michael", 20 , 100)
vilian = Character("Avarge_Joe", 3, 45)

while hero.is_alive() and vilian.is_alive():
    vilian.take_damage(hero.get_streght())
    print(vilian.get_health())
    if vilian.is_alive() == False:
        print("hero Won")
        break
    else:
        hero.take_damage(vilian.get_streght())
        print(hero.get_health())
        if hero.is_alive == False:
            print("Vilian won")
            break