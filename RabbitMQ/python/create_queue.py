#!/usr/bin/env python
import pika

host = '10.31.97.216'
credentials = pika.PlainCredentials('radmin', 'radmin')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials))
channel = connection.channel()

print("Connected!")