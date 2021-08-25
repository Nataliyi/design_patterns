"""Прокси защиты. Для защиты от молодых водителей, мы создаем прокси Carproxy, 
в котором контролируется возраст водителя. Таким образом мы не нарушаем принцип Open_closed 
и не изменяем уже существующий класс Car"""

class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')

class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print('Driver too young')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    car = CarProxy(Driver('John', 12))
    car.drive()