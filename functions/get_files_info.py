import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        if not valid_target_dir:
            raise ValueError(
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
        if not os.path.isdir(target_dir):
            raise ValueError(f'Error: Directory "{directory}" does not exist')

        contents = os.listdir(target_dir)
        for item in contents:
            f = os.path.join(target_dir, item)
            file_size = os.path.getsize(f)
            is_dir = os.path.isdir(f)
            print(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        print(f"Error: {e}")
