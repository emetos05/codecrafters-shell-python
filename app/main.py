import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    # print("$ ", end="")
    user_input: str = input()
    if user_input:
        print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
