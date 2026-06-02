import subprocess
import sys, os


def main() -> None:
    # TODO: Uncomment the code below to pass the first stage
    # sys.stdout.write("$ ")
    # print("$ ", end="")
    shell_builtin: list[str] = ["echo", "exit", "type", "pwd", "cd"]
    sys_path: str | None = os.environ.get("PATH")
    path_list = []

    while True:
        print("$ ", end="")
        user_input: str = input()
        input_args: list[str] = user_input.split(" ")
        if sys_path:
            path_list: list[str] = sys_path.split(os.pathsep)

        if user_input == "exit":
            break
        elif user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input.startswith("cd "):
            my_path = input_args[1]
            try:
                if my_path == "~":
                    home_dir = os.path.expanduser(my_path)
                    if home_dir:
                        os.chdir(home_dir)
                else:
                    os.chdir(my_path)
            except OSError:
                print(f"cd: {my_path}: No such file or directory")
        elif user_input == "pwd":
            print(os.getcwd())
        elif user_input.startswith("type "):
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
        elif input_args[0] not in shell_builtin:
            for path in path_list:
                exec_path: str = os.path.join(path, input_args[0])
                if os.path.exists(exec_path) and os.access(exec_path, os.X_OK):
                    subprocess.run(input_args)
                    break
            else:
                print(f"{input_args[0]}: command not found")


if __name__ == "__main__":
    main()
