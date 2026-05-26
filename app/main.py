import subprocess
import sys, os


def main() -> None:
    # TODO: Uncomment the code below to pass the first stage
    # sys.stdout.write("$ ")
    # print("$ ", end="")
    shell_builtin: list[str] = ["echo", "exit", "type", "pwd"]
    sys_path: str | None = os.environ.get("PATH")
    path_list = []
    executed: bool = False

    while True:
        print("$ ", end="")
        user_input: str = input()
        input_args: list[str] = user_input.split(" ")
        if sys_path:
            path_list: list[str] = sys_path.split(os.pathsep)

        if user_input:
            if input_args[0] not in shell_builtin:
                for path in path_list:
                    exec_path: str = os.path.join(path, input_args[0])
                    if os.path.exists(exec_path) and os.access(exec_path, os.X_OK):
                        subprocess.run(input_args)
                        executed = True
                        break

        if user_input.startswith("type "):
            if input_args[1] in shell_builtin:
                print(f"{input_args[1]} is a shell builtin")
            elif input_args[1] not in shell_builtin:
                for path in path_list:
                    full_path: str = os.path.join(path, input_args[1])
                    if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                        print(f"{input_args[1]} is {full_path}")
                        break
                else:
                    print(f"{input_args[1]}: not found")

        elif user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input == "exit":
            break
        elif user_input == "pwd":
            print(os.getcwd())
        else:
            if executed is False:
                print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
