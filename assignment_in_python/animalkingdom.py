from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def eat(self):
        ...

    @staticmethod
    def speak():
        print("I am a animal")


class Dog(Animal):
    def eat(self):
        print("I am a dog")


class Cat(Animal):
    def eat(self):
        print("I am a cat")
