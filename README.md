# Приложение с M3 рабочим столом

## Установка

0. Установите Python на Linux:
```bash
apt install -y software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt update
apt install -y python3.9
apt install -y python3.9-venv
python3.9 --version
```

1. Перенесите архив m3_project-1.0.0.tar.gz в любую папку
2. Введите команду для распаковки архива
```bash
tar -xzf m3_project-1.0.0.tar.gz
```
3. Перейдите в распакованный архив
```bash
cd m3_project-1.0.0
```
4. Скопируйте переменные окружения в .env:
```bash
cp .env.example .env
```
5. Сгенерируйте секретный ключ для приложения
```bash
sed -i "s|^DJANGO_SECRET_KEY=.*|DJANGO_SECRET_KEY=$(openssl rand -hex 32)|" .env
```
6. Создайте виртуальное окружение
```bash
python3.9 -m venv .venv
```
7. Активируйте виртуальное окружение
```bash
source .venv/bin/activate
```
8. Установите необходимые зависимости
```bash
pip install -r requirements.txt
```
9. Запустите миграции БД
```bash
python manage.py migrate
```
10.   Запустите приложение
```bash
python manage.py runserver 0.0.0.0:8000
```


## Для разработки

Собрать архив проекта:
```bash
python setup.py sdist --formats=gztar --dist-dir ./
```