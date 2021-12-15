
class Animals:
    def __init__(self,race,pred_prey,color,habits,size):
        self.race = race
        self.pred_prey = pred_prey
        self.color = color
        self.habits = habits
        self.size = size

class Dog(Animals):

    def __init__(self,color, race) -> None:
        super(Animals).__init__(color, race)

    def see_race(self):
        print(self.race)


Tom = Dog(1,2)

Tom.see_race()

