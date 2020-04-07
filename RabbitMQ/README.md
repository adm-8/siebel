# Установака RabbitMQ и настройка Siebel для общения с ним

## Установака \ настройка RabbitMQ
Смотрим какая версия на текущий момент актуальна: 
https://www.rabbitmq.com/install-windows.html#installer

### Качаем и устанавливаем Erlang/OTP 
* Идём на https://www.rabbitmq.com/which-erlang.html и смотрим с какой версией Erlang/OTP совместима версия RabbitMQ которую хотим поставить.
* Идём на https://www.erlang.org/downloads и качаем нужную вверсию
* Запускаем установщик Erlang/OTP под админимстратором, иначе могут быть проблемы

### Качаем и устанавливаем RabbitMQ
После того как кролик всстал, надо пйоти и проверить, работает ли он. Для это запускаем коммандную строку и идём в папку sbin где был установлен кролик. В моей случае
```
cd C:\Program Files\RabbitMQ Server\rabbitmq_server-3.8.3\sbin
```
И проверяем его статус:
```
rabbitmqctl status
```
Подробнее про утилиту rabbitmqctl можно почитать тут: https://www.rabbitmq.com/rabbitmqctl.8.html

Кроме того, можно управлять кроликом через  интерфейс, подробнее тут: https://www.rabbitmq.com/management.html
```
rabbitmq-plugins enable rabbitmq_management

rabbitmqctl add_user radmin radmin

rabbitmqctl set_user_tags radmin administrator

```
После того как включили rabbitmq_management и создали пользователя с нужными првами можем ходить в интерфейс: http://localhost:15672

