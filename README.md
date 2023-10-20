_**Важная информация**_
=======================
-----------------------

1) В репозитории присутствует как 1, так и 2 задание (task_1 и task_2)
2) Для запуска второго задания необходимо выполнить команды:
```bash
docker-compose build
docker-compose up
```
3) Url для второго задания:
- http://127.0.0.1:8080/api/keyvalue/<string:key> - GET API endpoint, в <string:key> подается ключ для записи в базе данных.
- http://127.0.0.1:8080/api/keyvalue - POST API endpoint, отправляется json вида: {"key":"","value":""} для добавления запси в БД
- http://127.0.0.1:8080//api/keyvalue/<string:key> - PUT API endpoint, в <string:key> отправляется ключ от записи в БД, а с помощью json вида {"value":""} устанавливается значение ключа.

