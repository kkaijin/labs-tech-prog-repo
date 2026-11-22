from abc import ABC, abstractmethod
from typing import Optional


class Pet(ABC):
    @abstractmethod
    def express(self) -> None:

        pass

    @abstractmethod
    def getName(self) -> str:

        pass

    @abstractmethod
    def getAge(self) -> int:

        pass

    @abstractmethod
    def getAgeInHumanYears(self) -> int:

        pass


class Animal(Pet):
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def happyBirthday(self) -> None:
        self.__age += 1

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    @abstractmethod
    def express(self) -> None:
        pass

    @abstractmethod
    def getAgeInHumanYears(self) -> int:
        pass


class Parrot(Animal):
    def getAgeInHumanYears(self) -> int:
        return self.getAge() * 5

    def express(self) -> None:
        print(f'{self.getName()}: "Hello!"')
        print('   \\')
        print('   (o>')
        print('\\\\_//)')
        print(' \\_/_)')
        print('  _|_')


class Turtle(Animal):
    def getAgeInHumanYears(self) -> int:
        if self.getAge() <= 0:
            return 0
        return 15 + (self.getAge() - 1) * 2

    def express(self) -> None:
        print('  _____     ____')
        print(' /      \\  |  o |')
        print('|        |/ ___\\|')
        print('|_________/')
        print('|_|_| |_|_|')


class Person:
    def __init__(self, name: str, pet: Optional[Pet] = None) -> None:
        self.__name = name
        self.__pet = pet

    def setPet(self, pet: Optional[Pet]) -> None:
        self.__pet = pet

    def getPetInfo(self) -> None:
        print('--------------------')
        if self.__pet is None:
            print(f'{self.__name} has no pet yet')
            print('--------------------')
            return

        print(f'Pet for {self.__name} is named {self.__pet.getName()}')
        print(
            f'Age: {self.__pet.getAge()} year(s), '
            f'about {self.__pet.getAgeInHumanYears()} human years'
        )
        print('And it expresses itself like this:')
        self.__pet.express()
        print('--------------------')


def main() -> None:
    kesha = Parrot('Kesha', 2)
    zavala = Turtle('Zavala', 4)

    kesha.happyBirthday()

    jack = Person('Jack', kesha)
    john = Person('John')

    jack.getPetInfo()
    john.getPetInfo()

    john.setPet(zavala)
    john.getPetInfo()


if __name__ == '__main__':
    main()
