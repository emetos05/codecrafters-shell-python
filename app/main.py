import sys


def main() -> None:
    # TODO: Uncomment the code below to pass the first stage
    # sys.stdout.write("$ ")
    # print("$ ", end="")
    shell_builtin: list[str] = ["echo", "exit", "type"]
    while True:
        print("$ ", end="")
        user_input: str = input()
        input_args: list[str] = user_input.split(" ")

        if user_input.startswith("type "):
            if input_args[1] in shell_builtin:
                print(f"{input_args[1]} is a shell builtin")
            else:
                print(f"{input_args[1]}: not found")
                continue

        elif user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input == "exit":
            break
        else:
            print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
