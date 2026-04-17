import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: Directory "{directory}" does not exist'
        files_info = []
        files = os.listdir(target_dir)
        for item in files:
            f = os.path.join(target_dir, item)
            file_size = os.path.getsize(f)
            is_dir = os.path.isdir(f)
            files_info.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"
