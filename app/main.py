def copy_file(command: str) -> None:
    try:
        copy_command, file_name_in, file_name_out = command.split(" ")
        if (
            file_name_in == file_name_out
            or copy_command != "cp"
            or file_name_out is None
        ):
            return

        try:
            with (
                open(file_name_in, "r") as file_in,
                open(file_name_out, "w") as file_out,
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            # спеціально для тебе упирюга
            pass
    except ValueError:
        # спеціально для тебе упирюга
        pass
