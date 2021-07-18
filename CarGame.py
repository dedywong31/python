command = ""
is_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if is_started:
            print("Car already started...")
        else:
            is_started = True
            print("Car started...")
    elif command == "stop":
        if not is_started:
            print("Car already stopped...")
        else:
            is_started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("I don't understand that")