# Создать класс Animal: name, color
# Создать класс Cat(Animal): свойства(get, set) по всем атрибутам, метод выводит мяу
# Создать класс Dog(Animal): свойства(get, set) по всем атрибутам, метод выводит гав


# 1 решение
# class Animal:
#     def init(self, name, color):
#         self.name = name
#         self.color = color
# class Cat(Animal):
#     def init(self, name, color, voice):
#         super().init(name, color)
#         self.voice = voice
#
#     def print_voice(self):
#         print(self.voice)
#
#     def set_name(self, new_name):
#         if new_name != '':
#             self.name = new_name
#
#     def get_name(self):
#         return self.name
#
#     def set_color(self, new_color):
#         if new_color != '':
#             self.color = new_color
#
#     def get_color(self):
#         return self.color
#
#     def str(self):
#         return (f'hello, I  - {self.color} cat {self.name}. {self.voice}')
# class Dog(Animal):
#     def init(self, name, color, voice):
#         super().init(name, color)
#         self.voice = voice
#
#     def print_voice(self):
#         print(self.voice)
#
#     def set_name(self, new_name):
#         if new_name != '':
#             self.name = new_name
#
#     def get_name(self):
#         return self.name
#
#     def set_color(self, new_color):
#         if new_color != '':
#             self.color = new_color
#
#     def get_color(self):
#         return self.color
#
#     def str(self):
#         return (f'hello I- {self.color} dog {self.name}. {self.voice}')
# catName = input('name: ')
# catColor = input('color: ')
# catVoice = 'meow!'
# cat = Cat(catName, catColor, catVoice)
# print()
# print('name: ', cat.get_name())
# print('color: ', cat.get_color())
# print()
# cat.set_name('Tom')
# cat.set_color('black')
# print(cat)
# cat.print_voice()
#
# dogName = input('name: ')
# dogColor = input('color: ')
# dogVoice = 'woof!'
# dog = Dog(dogName, dogColor, dogVoice)
# print()
# print('name: ', dog.get_name())
# print('color: ', dog.get_color())
# dog.set_name('bob')
# dog.set_color('black')
# print(dog)
# dog.print_voice()
#

# 2 Решение


# class Animal():
#     name = ""
#     color = ""
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name, color)
#     def speak (self):
#         return "Meow"
#
# class Dog(Animal):
#     def __init__(self, name, color):
#         super().__init__(name, color)
#     def speak (self):
#         return "Woof"
#
# my_cat = Cat("Tom", "Black")
# my_dog = Dog("Sasha", "White")
# print(my_cat.speak())
# print(my_dog.speak())



# 3 решение


# # Импортируем класс и декоратор.
# from abc import ABC, abstractmethod
#
# # Определяем абстрактный суперкласс.
# class Animal(ABC):
#     # Определяем абстрактный метод.
#     @abstractmethod
#     def make_sound(self):
#         self.s = 'Питомец говорит "{}"!'
#
# # Определяем подкласс кошек.
# class Cat(Animal):
#     # Реализуем абстрактный метод для кошек.
#     def make_sound(self):
#         # Вызываем сперва родительский метод.
#         # Animal.make_sound(self)
#         super().make_sound()
#         return self.s.format('Мяу')
#
# # Определяем подкласс собак.
# class Dog(Animal):
#     # Реализуем абстрактный метод для собак.
#     def make_sound(self):
#         # Полностью переопределяем абстр. метод.
#         s = 'Собаки говорят "{}"!'.format('Гав')
#         return s
#
# # Создаем экземпляр класса кошек.
# cat = Cat()
# # Мяукаем.
# print(cat.make_sound())
#
# # Создаем экземпляр класса собак.
# dog = Dog()
# # Гавкаем.
# print(dog.make_sound())





