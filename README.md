# Яндекс.Практикум
## курс Python-разработчик плюс

### Учебный проект api_yatube.:computer:
![api](https://trafopedia.ru/storage/app/uploads/public/5f7/07d/ff7/5f707dff7011b583558647.jpg)

#### Задачи проекта:

В проекте api_yatube есть приложение posts с описанием моделей Yatube. Нужно реализовать API для всех моделей приложения.

Обязательное условие: работать с моделью Post через ModelViewSet.
_________
## **Инструкция:**:point_down:

+ ~~Копировать~~ *Клонировать репозиторий и перейти в его папку в командной строке:*

`*https://github.com/AliaBis/api_yatube*`

`cd api_yatube`

+ __Cоздать и активировать виртуальное окружение:__

    + `python3 -m venv venv`

Для *nix-систем и MacOS:

    `source venv/bin/activate`

Для windows-систем:

    `source venv/Scripts/activate`

- ___Установить зависимости из файла requirements.txt:___

`python3 -m pip install --upgrade pip`

`pip install -r requirements.txt`

- *Выполнить миграции:*

`cd yatube_api`

`python3 manage.py migrate`

+ Запустить проект:

`python3 manage.py runserver`

- Создать суперпользователя Django:

`python3 manage.py createsuperuser`

Сам проект и админ-панель по адресам:

[сам проект](http://127.0.0.1:8000)

http://127.0.0.1:8000/admin



________
Пример вставки кода в readme:
```python
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```
