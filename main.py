
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_new_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def add_existing_task(self, task):
        new_task = task
        self.tasks.append(new_task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def print_info(self):
        print(f"Название магазина: {self.name}")
        print(f"Адрес магазина: {self.address}")
        print("Товары, имеющиеся в магазине:")
        for item in self.items:
            print(f"{item}: {self.items[item]}")



print()
print("Пример использования класса Task:")
task1 = Task("Пойти в кино", "2024-3-8")
task2 = Task("Приготовить обед", "2024-6-1")
task3 = Task("Полить цветы", "2024-8-15")

print()
print(task1.__str__())
print(task2.__str__())
print(task3.__str__())

task1.mark_as_completed()
task2.mark_as_completed()
task3.mark_as_completed()

print()
print("Поставленные задачи выполнены!")
print(task1.__str__())
print(task2.__str__())
print(task3.__str__())

print()
print("=============================================================================")

print()
print("Пример использования класса TaskManager:")
task_manager = TaskManager()
task_manager.add_existing_task(task1)
task_manager.add_existing_task(task2)
task_manager.add_existing_task(task3)
task_manager.add_new_task("Сделать домашнее задание", "2023-10-01")
task_manager.add_new_task("Купить продукты", "2023-10-02")

print()
print("Все имеющиеся задачи:")
for task in task_manager.tasks:
    print(task)

print()
print("Текущие задачи:")
for task in task_manager.get_current_tasks():
    print(task)

print()
print("Выполняем текущие задачи!")
task_manager.mark_task_completed(3)
task_manager.mark_task_completed(4)

print()
print("Все имеющиеся задачи:")
for task in task_manager.tasks:
    print(task)

print()
print("Текущие задачи имеются?")
if len(task_manager.get_current_tasks()) == 0:
    print("Текущие задачи отсутствуют!")
    print("Все поставленные задачи выполнены!!")
    print("Урааа!!!")
else:
    for task in task_manager.get_current_tasks():
        print(task)

print()
print("=============================================================================")

print()
print("Пример использования класса Store:")
store1 = Store("Магазин 'Аврора'", "Улица Рассветная")
store1.add_item("Яблоки", 20)
store1.add_item("Бананы", 15)

store2 = Store("Магазин 'Пятерочка'", "Улица Содружества")
store2.add_item("Хлеб", 10)

store3 = Store("Магазин 'Магнит'", "Улица Металлургическая")
store3.add_item("Молоко", 25)

print()
print("Магазин 1:")
store1.print_info()

print()
print("Магазин 2:")
store2.print_info()

print()
print("Магазин 3:")
store3.print_info()

print()
print("Тестирование методов магазина:")
print(f"{store1.name}: Цена яблок {store1.get_item_price('Яблоки')}")
store1.update_item_price("Яблоки", 50)
print(f"{store1.name}: Новая цена яблок {store1.get_item_price('Яблоки')}")
store1.remove_item("Яблоки")
print(f"{store1.name}: Цена яблок после удаления: {store1.get_item_price('Яблоки')}")