def copy_file(config: str) -> None:
    try:
        command, fn_in, fn_out = config.split(" ")
        if fn_in == fn_out or command != "cp" or fn_out is None:
            return

        try:
            with (
                open(fn_in, "r") as file_in,
                open(fn_out, "w") as file_out,
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {fn_in} not found")
    except ValueError:
        print("Invalid config")
