from datetime import datetime

from termcolor import colored


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = colored(name,'red')
        self.salutation = colored(salutation,'red')
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self , message , sent_by_me):
        self.message =colored( message,'green')
        self.time =datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Thakur', 'Mr.', 20, 4.2)

friend_one = Spy('Raja', 'Mr.', 24,4.5)
friend_two = Spy('Mata Hari', 'Ms.', 29, 4.3)
friend_three = Spy('No', 'Dr.', 23, 4.7)


friends = [friend_one, friend_two, friend_three]
