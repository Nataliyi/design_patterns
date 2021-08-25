"""В продолжение рассмотрим непростой пример использования шаблона Цепочка Обязанностей"""

# 1) event broker
# 2) command-query separation (cqs)
# 3) observer
from abc import ABC
from enum import Enum

# Какое либо Событие
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


# класс параметров
class WhatToQuery(Enum):
    ATTACK:int = 1
    DEFENSE:int = 2
    
    
 # Персонаж
class Creature:
    def __init__(self, game:object, name:str, attack:int, defense:int):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        # устанавливаем свойство атака
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        # и свойство защита
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        # теперь установлено значение self.initial_defense
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'
       

# запрос на изменение параметров
class Query:
    def __init__(self, creature_name:object, what_to_query:str, default_value:int):
        self.value = default_value  # bidirectional
        self.what_to_query = what_to_query
        self.creature_name = creature_name

# игра
class Game:
    def __init__(self):
        # инициализируем Событие
        self.queries = Event()

    def perform_query(self, sender:object, query:object):
        # выполняем запрос, принимаем на вход отправителя и сам запрос
        # добавляем в запрос
        self.queries(sender, query)


# абстрактный класс как родительский класс улучшения персонажа
class CreatureModifier(ABC):
    def __init__(self, game:object, creature:object):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender:object, query:object):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)

# создаем наследника, удваивающего параметр атаки
class DoubleAttackModifier(CreatureModifier):

    def handle(self, sender:object, query:object):
        # вручаем бонус по соответствию имени и атаки
        if (sender.name == self.creature.name and
                query.what_to_query == WhatToQuery.ATTACK):
            query.value *= 2

# аналогично создаем бонус защиты
class IncreaseDefenseModifier(CreatureModifier):

    def handle(self, sender:object, query:object):
        if (sender.name == self.creature.name and
                query.what_to_query == WhatToQuery.DEFENSE):
            query.value += 3


if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'Strong Goblin', 2, 2)
    print(goblin)

    # бонусы действуют только во время События))
    with DoubleAttackModifier(game, goblin):
        print(goblin)
        with IncreaseDefenseModifier(game, goblin):
            print(goblin)

    print(goblin)
