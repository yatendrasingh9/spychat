from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from termcolor import colored

STATUS_MESSAGES = ['My name is Prashant, Prashant Thakur', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

print colored("\n* * * * * -- Welcome to Volatile spychat -- * * * * *\n" , 'magenta')
print colored("Hello! Let\'s get started",'cyan')

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)


# method for add the status

def add_status():

    updated_status_message = None

    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)

    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

        else:
            print 'The option you chose is not valid! Press either y or n.'

        if updated_status_message:
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print 'You current don\'t have a status update'

        return updated_status_message

# method for add friend

def add_friend():

    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


# method for choose a friend


def select_a_friend():
    item_number = 0


    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


# method for send message

def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "image.jpg"
    text = raw_input("What do you want to say? ")
    if(len(text)>0):
        Steganography.encode(original_image, output_path, text)

        new_chat = ChatMessage(text,True)

        friends[friend_choice].chats.append(new_chat)

        print "Your secret message image is ready!"
    else:
        print("there is no messgae. Please try again")


# method for read messgae

def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


# method for read chat history

def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (colored(chat.time.strftime("%d %B %Y"),'blue'), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

# method for start the chat

def start_chat(spy):

    spy.name =colored(spy.salutation + " " + spy.name,'red')

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. \nWelcome " + spy.name + "    Age: " + str(spy.age) + "   and Rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = colored("What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n",'magenta')
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0 and len(menu_choice)<7:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)

                elif menu_choice == 3:
                    send_message()

                elif menu_choice == 4:
                    read_message()

                elif menu_choice == 5:
                    read_chat_history()

                else:
                    show_menu = False
                    print colored("Invalid choice", 'red')
                    print colored("Thank You.", 'cyan')
    else:
        print colored('Sorry you are not of the correct age to be a spy', 'red')




# if user wants to use default user.
if existing == "Y" or existing == "y":
    start_chat(spy)

# if user wants to create new one then enter the name, salutation, age and rating.
else:

# first initialize the spy name, salutation, age and rating as null or zero before user enter.
    spy = Spy('','',0,0.0)

    spy.name =raw_input("\nWelcome to spy chat\t You must tell me your spy name first: ")

# if user enter name then if statement execute otherwise else statement execute
    if len(spy.name) > 0 :
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print colored("\nPlease add a valid spy name",'red')