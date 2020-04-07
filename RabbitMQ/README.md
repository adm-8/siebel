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

Для этого надо включить плагин системы управления:
```
rabbitmq-plugins enable rabbitmq_management
```
Затем созать пользователя и дать ему права:
```
rabbitmqctl add_user radmin radmin

rabbitmqctl set_user_tags radmin administrator

rabbitmqctl set_permissions -p / radmin ".*" ".*" ".*"

```
После того как включили rabbitmq_management и создали пользователя с нужными првами можем ходить в интерфейс: http://localhost:15672

![rabbit_mq_homepage.JPG](https://github.com/adm-8/siebel/blob/master/RabbitMQ/img/rabbit_mq_homepage.JPG?raw=true)

## Создаем очереди:
На вход:
```
Adapter.CRM.Oppty
```
На выход:
```
CRM.Adapter.Oppty
```
![rabbit_mq_add_queue.JPG](https://github.com/adm-8/siebel/blob/master/RabbitMQ/img/rabbit_mq_add_queue.JPG?raw=true)