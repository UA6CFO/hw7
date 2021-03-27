# Проект "Пицерия" - ООП


import os


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"  # не буду комментировать...


class Product(): # описание продукта.

    def __init__(self, title, calorific, cost):
        if Product.value_empty(title):
            self.title = title  # название. Обязательный атрибут. Не может быть пустым
        else:
            raise ValueError
        if (Product.check_zero(calorific) and Product.check_zero(cost)):
            self.calorific = calorific  # калорийность на 100 грамм. Обязательный. Только положительное число
            self.cost = cost  # себестоимость: цена за 100 грамм продукта. Обязательный. только положительное число
        else:
            raise ValueError    

    @staticmethod
    def value_empty(zstr):
        return zstr != ''

    @staticmethod
    def check_zero(value):
        return value >= 0  # потому, что: вода - калории=0, цена=0...

    def __str__(self):
        return f'Наименование: {self.title}\t калорий (на 100 гр.): {self.calorific}\t цена (за 100 гр.): {self.cost}'


class Ingredient(Product): # описание ингредиента. 
    
    def __init__(self, title, calorific, cost, weight):
        Product.__init__(self, title, calorific, cost)  # вызов конструктора для базового класса Product
        if Ingredient.check_zero(weight):
            self.weight = weight  # вес. Обязательный атрибут. Только положительное число.
            self.__list_ing = {}
        else: 
            raise ValueError 
        self.calc() 

    @staticmethod
    def check_zero(value):
        return value > 0   

    def calc(self):
        self.__list_ing['name'] = self.title
        self.__list_ing['weight'] = self.weight
        self.__list_ing['calor'] = self.weight / 100 * self.calorific  # Калорийность ингредиента: вес_ингредиента / 100 * калорийность_продукта 
        self.__list_ing['price'] = self.weight / 100 * self.cost  # Себестоимость: вес_ингредиента / 100 * себестоимость_продукта

    def get_items(self):
        return self.__list_ing    

    def __str__(self):   
        return f'Название: {self.name}\t вес: {self.weight}\t калорий: {toFixed(self.calor, 0)}\t стоимость: {toFixed(self.price, 2)}'
         

class Pizza():  # пицца...
    
    def __init__(self, title, ingredients=[]):  # ingredients - ингредиенты. Список значений класса Ingredient.
        if Product.value_empty(title):
            self.title = title  # название пицы. Обязательный атрибут. Не может быть пустым
            self.__ingred = ingredients
        else:
            raise ValueError
        self.__title = title
        self.__calor = 0.0
        self.__price = 0.0
        self.__ingred = ingredients
        self.calc()

    @staticmethod
    def value_empty(zstr):
        return zstr != ''

    def calc(self):
        for i in self.__ingred:
            self.__calor = self.__calor + i['calor']
            self.__price = self.__price + i['price']
        
    def get_sostav(self):
        self.__sostav = ''
        self.__sostav = 'Состав: '
        for i in self.__ingred:
            self.__sostav = self.__sostav + i['name'] + '; '
        return self.__sostav

    def __str__(self):
        return f'{self.__title} ({toFixed(self.__calor, 1)} kkal) - {toFixed(self.__price, 2)} руб.'


os.system('cls')
list_pizza_1 = []
list_pizza_2 = []
list_pizza_3 = []

# калории - ккал, цена - рублях, вес - граммы
list_pizza_1.append(Ingredient('Соль поваренная пищевая', 0, 2, 6).get_items())
list_pizza_1.append(Ingredient('Мука пшеничная', 342, 5, 200).get_items())
list_pizza_1.append(Ingredient('Вода', 0, 0, 70).get_items())
list_pizza_1.append(Ingredient('Дрожжи Саф-Момент', 370, 12, 20).get_items())
list_pizza_1.append(Ingredient('Масло подсолнечное с оливковым', 899, 11, 50).get_items())
list_pizza_1.append(Ingredient('Сыр Гауда', 356, 48, 100).get_items())
list_pizza_1.append(Ingredient('Томатная паста', 54, 52, 80).get_items())
list_pizza_1.append(Ingredient('Перец молотый', 263, 40, 1).get_items())
list_pizza_1.append(Ingredient('Колбаса салями', 345, 115, 150).get_items())

list_pizza_2.append(Ingredient('Соль поваренная пищевая', 0, 2, 6).get_items())
list_pizza_2.append(Ingredient('Мука пшеничная', 342, 5, 200).get_items())
list_pizza_2.append(Ingredient('Вода', 0, 0, 70).get_items())
list_pizza_2.append(Ingredient('Дрожжи Саф-Момент', 370, 12, 20).get_items())
list_pizza_2.append(Ingredient('Масло подсолнечное с оливковым', 899, 11, 50).get_items())
list_pizza_2.append(Ingredient('Сыр Гауда', 356, 48, 100).get_items())
list_pizza_2.append(Ingredient('Томатная паста', 54, 52, 80).get_items())
list_pizza_2.append(Ingredient('Перец молотый', 263, 40, 1).get_items())
list_pizza_2.append(Ingredient('Ветчина', 279, 130, 170).get_items())

list_pizza_3.append(Ingredient('Соль поваренная пищевая', 0, 2, 6).get_items())
list_pizza_3.append(Ingredient('Мука пшеничная', 342, 5, 200).get_items())
list_pizza_3.append(Ingredient('Вода', 0, 0, 70).get_items())
list_pizza_3.append(Ingredient('Дрожжи Саф-Момент', 370, 12, 20).get_items())
list_pizza_3.append(Ingredient('Масло подсолнечное с оливковым', 899, 11, 50).get_items())
list_pizza_3.append(Ingredient('Сыр Гауда', 356, 48, 100).get_items())
list_pizza_3.append(Ingredient('Томатная паста', 54, 52, 80).get_items())
list_pizza_3.append(Ingredient('Перец молотый', 263, 40, 1).get_items())
list_pizza_3.append(Ingredient('Оливки', 296, 72, 100).get_items())

print(Pizza('Пицца с колбасой', list_pizza_1))
print(Pizza('Пицца с колбасой', list_pizza_1).get_sostav())
print()
print(Pizza('Пицца с ветчиной', list_pizza_2))
print(Pizza('Пицца с колбасой', list_pizza_2).get_sostav())
print()
print(Pizza('Пицца оливками', list_pizza_3))
print(Pizza('Пицца с колбасой', list_pizza_3).get_sostav())
print()
