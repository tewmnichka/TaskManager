from datetime import datetime


class Task:
    """Класс, представляющий задачу"""

    def __init__(self, title: str, description: str = "", priority: str = "средний"):
        """
        Конструктор класса Task

        Args:
            title: Название задачи
            description: Описание задачи
            priority: Приоритет (низкий, средний, высокий)
        """
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__completed = False
        self.__created_at = datetime.now()
        self.__completed_at = None

    # Геттеры и сеттеры для title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title.strip()) > 0:
            self.__title = new_title
        else:
            raise ValueError("Название задачи не может быть пустым")

    # Геттеры и сеттеры для description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            self.__description = new_description
        else:
            raise ValueError("Описание должно быть строкой")

    # Геттеры и сеттеры для priority
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, new_priority):
        valid_priorities = ["низкий", "средний", "высокий"]
        if new_priority in valid_priorities:
            self.__priority = new_priority
        else:
            raise ValueError(f"Приоритет должен быть одним из: {valid_priorities}")

    # Геттер для completed (только чтение)
    @property
    def completed(self):
        return self.__completed

    # Геттеры для дат
    @property
    def created_at(self):
        return self.__created_at

    @property
    def completed_at(self):
        return self.__completed_at

    def mark_completed(self):
        """Отметить задачу как выполненную"""
        if not self.__completed:
            self.__completed = True
            self.__completed_at = datetime.now()
            print(f"Задача '{self.__title}' отмечена как выполненная")
        else:
            print(f"Задача '{self.__title}' уже была выполнена")

    def __str__(self):
        """Магический метод для строкового представления задачи"""
        status = "✓" if self.__completed else "○"
        priority_symbol = {
            "низкий": "⬇️",
            "средний": "➡️",
            "высокий": "⬆️"
        }.get(self.__priority, "")

        return f"{status} [{priority_symbol}] {self.__title} - {self.__description[:30]}..."

    def get_info(self):
        """Полная информация о задаче"""
        info = f"Задача: {self.__title}\n"
        info += f"Описание: {self.__description}\n"
        info += f"Приоритет: {self.__priority}\n"
        info += f"Создана: {self.__created_at.strftime('%d.%m.%Y %H:%M')}\n"

        if self.__completed:
            info += f"Выполнена: {self.__completed_at.strftime('%d.%m.%Y %H:%M')}"
        else:
            info += "Статус: Не выполнена"
        from datetime import datetime

        class Task:
            """Класс, представляющий задачу"""

            # Список допустимых приоритетов (константа класса)
            VALID_PRIORITIES = ["низкий", "средний", "высокий"]

            # Соответствие приоритетов и эмодзи
            PRIORITY_EMOJIS = {
                "низкий": "⬇️",
                "средний": "➡️",
                "высокий": "⬆️"
            }

            def __init__(self, title: str, description: str = "", priority: str = "средний"):
                """
                Конструктор класса Task

                Args:
                    title: Название задачи
                    description: Описание задачи
                    priority: Приоритет (низкий, средний, высокий)
                """
                self.__title = title
                self.__description = description
                self.__priority = priority if self.validate_priority(priority) else "средний"
                self.__completed = False
                self.__created_at = datetime.now()
                self.__completed_at = None

            # Геттеры и сеттеры для title
            @property
            def title(self):
                return self.__title

            @title.setter
            def title(self, new_title):
                if isinstance(new_title, str) and len(new_title.strip()) > 0:
                    self.__title = new_title
                else:
                    raise ValueError("Название задачи не может быть пустым")

            # Геттеры и сеттеры для description
            @property
            def description(self):
                return self.__description

            @description.setter
            def description(self, new_description):
                if isinstance(new_description, str):
                    self.__description = new_description
                else:
                    raise ValueError("Описание должно быть строкой")

            # Геттеры и сеттеры для priority
            @property
            def priority(self):
                return self.__priority

            @priority.setter
            def priority(self, new_priority):
                if self.validate_priority(new_priority):
                    self.__priority = new_priority
                else:
                    raise ValueError(f"Приоритет должен быть одним из: {self.VALID_PRIORITIES}")

            # Геттер для completed (только чтение)
            @property
            def completed(self):
                return self.__completed

            # Геттеры для дат
            @property
            def created_at(self):
                return self.__created_at

            @property
            def completed_at(self):
                return self.__completed_at

            @staticmethod
            def validate_priority(priority):
                """Проверяет корректность приоритета"""
                return priority in Task.VALID_PRIORITIES

            @staticmethod
            def get_priority_emoji(priority):
                """Возвращает эмодзи для приоритета"""
                return Task.PRIORITY_EMOJIS.get(priority, "❓")

            @classmethod
            def create_from_string(cls, task_string: str):
                """
                Создает задачу из строки формата: "Название | Описание | Приоритет"

                Args:
                    task_string: Строка с данными задачи, разделенными символом '|'

                Returns:
                    Task: Объект задачи или None в случае ошибки
                """
                try:
                    if not isinstance(task_string, str) or not task_string.strip():
                        raise ValueError("Строка не может быть пустой")

                    parts = task_string.split('|')
                    title = parts[0].strip()

                    if not title:
                        raise ValueError("Название задачи не может быть пустым")

                    description = parts[1].strip() if len(parts) > 1 else ""
                    priority = parts[2].strip() if len(parts) > 2 else "средний"

                    # Проверяем и корректируем приоритет
                    if not cls.validate_priority(priority):
                        print(f"Предупреждение: приоритет '{priority}' недопустим, установлен 'средний'")
                        priority = "средний"

                    return cls(title, description, priority)

                except IndexError:
                    print("✗ Ошибка: недостаточно данных в строке. Формат: Название | Описание | Приоритет")
                    return None
                except ValueError as e:
                    print(f"✗ Ошибка: {e}")
                    return None
                except Exception as e:
                    print(f"✗ Непредвиденная ошибка при создании задачи из строки: {e}")
                    return None

            def mark_completed(self):
                """Отметить задачу как выполненную"""
                if not self.__completed:
                    self.__completed = True
                    self.__completed_at = datetime.now()
                    print(f"✓ Задача '{self.__title}' отмечена как выполненная")
                else:
                    print(f"ℹ Задача '{self.__title}' уже была выполнена")

            def __str__(self):
                """Магический метод для строкового представления задачи"""
                status = "✓" if self.__completed else "○"
                priority_symbol = self.get_priority_emoji(self.__priority)

                return f"{status} [{priority_symbol}] {self.__title} - {self.__description[:30]}..."

            def get_info(self):
                """Полная информация о задаче"""
                info = f"Задача: {self.__title}\n"
                info += f"Описание: {self.__description}\n"
                info += f"Приоритет: {self.__priority} {self.get_priority_emoji(self.__priority)}\n"
                info += f"Создана: {self.__created_at.strftime('%d.%m.%Y %H:%M')}\n"

                if self.__completed:
                    info += f"Выполнена: {self.__completed_at.strftime('%d.%m.%Y %H:%M')}"
                else:
                    info += "Статус: Не выполнена"

                return info

            def to_dict(self):
                """Преобразует задачу в словарь для сохранения"""
                return {
                    'title': self.__title,
                    'description': self.__description,
                    'priority': self.__priority,
                    'completed': self.__completed,
                    'created_at': self.__created_at.isoformat() if self.__created_at else None,
                    'completed_at': self.__completed_at.isoformat() if self.__completed_at else None
                }

            @classmethod
            def from_dict(cls, data):
                """Создает задачу из словаря"""
                task = cls(
                    data['title'],
                    data['description'],
                    data['priority']
                )

                # Восстанавливаем состояние
                if data['completed']:
                    task._Task__completed = True
                    if data['completed_at']:
                        task._Task__completed_at = datetime.fromisoformat(data['completed_at'])

                if data['created_at']:
                    task._Task__created_at = datetime.fromisoformat(data['created_at'])

                return task


        return info


# Пример использования:
if __name__ == "__main__":
    # Создаем задачу
    task = Task("Купить продукты", "Молоко, хлеб, яйца", "высокий")

    # Выводим информацию
    print(task)
    print("\n" + task.get_info())

    # Отмечаем как выполненную
    task.mark_completed()
    print("\n" + task.get_info())

from task import Task


class ImportantTask(Task):
    """Класс для важных задач (наследник Task)"""

    def __init__(self, title: str, description: str = "", deadline: str = "сегодня"):
        """
        Конструктор важной задачи

        Args:
            title: Название задачи
            description: Описание
            deadline: Дедлайн
        """
        # Вызываем конструктор родителя с приоритетом "высокий"
        super().__init__(title, description, priority="высокий")
        self.__deadline = deadline
        self.__reminder_set = False

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, new_deadline):
        if isinstance(new_deadline, str) and len(new_deadline.strip()) > 0:
            self.__deadline = new_deadline
        else:
            raise ValueError("Дедлайн не может быть пустым")

    def set_reminder(self):
        """Установить напоминание"""
        self.__reminder_set = True
        print(f"🔔 Напоминание установлено для задачи '{self.title}'")

    # Переопределяем метод __str__
    def __str__(self):
        """Переопределенный метод для важных задач"""
        base_str = super().__str__()
        reminder = "🔔" if self.__reminder_set else "⏰"
        return f"{base_str} [Дедлайн: {self.__deadline}] {reminder}"

    # Переопределяем метод get_info
    def get_info(self):
        """Расширенная информация для важной задачи"""
        base_info = super().get_info()
        base_info += f"\nДедлайн: {self.__deadline}"
        base_info += f"\nНапоминание: {'установлено' if self.__reminder_set else 'не установлено'}"
        return base_info
