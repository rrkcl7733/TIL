for _ in range(int(input())):
    command = input()
    if command.startswith("Simon says"):
        print(command[len("Simon says"):])
