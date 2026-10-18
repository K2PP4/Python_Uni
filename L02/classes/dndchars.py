from random import randint as rnd

class fighter:
    def __init__(self, name: str):
        self._hp = rnd(15, 30)
        self._name = name

    def __str__(self):
        return f"{self._name} : \
    \n   HP: {self._hp} \
    \n   Is Alive?: {self.alive()}"

    def hit(self, damage: int) -> None:
        self._hp = max(self._hp - damage, 0)

    def heal(self, amt: int) -> None:
        if self.alive():
            self._hp = min(self._hp + amt, 30)

    def alive(self) -> bool:
        return self._hp > 0

def main():
    newFighter = fighter("hero")

    print(newFighter)

if __name__ == "__main__": main()
