import os
import re


def to_kebab_case(name):
    """
    Convert a string to kebab-case, removing long hexadecimal identifiers.

    Args:
        name (str): Original file or folder name

    Returns:
        str: Kebab-case formatted name
    """
    # Remove file extension for processing
    name_without_ext, ext = os.path.splitext(name)

    # Remove long hexadecimal identifiers (32-character hex strings)
    cleaned_name = re.sub(
        r'\s+[0-9a-f]{32}$', '', name_without_ext, flags=re.IGNORECASE)

    # Convert to lowercase
    kebab_name = cleaned_name.lower()

    # Replace spaces and underscores with hyphens
    kebab_name = re.sub(r'[\s_]+', '-', kebab_name)

    # Remove any non-alphanumeric characters except hyphens
    kebab_name = re.sub(r'[^a-z0-9-]', '', kebab_name)

    # Trim consecutive hyphens
    kebab_name = re.sub(r'-+', '-', kebab_name)

    # Trim leading and trailing hyphens
    kebab_name = kebab_name.strip('-')

    # Special handling for index.md
    if name == 'index.md':
        return '_index.md'

    # Reattach extension for non-image files
    image_extensions = {'.jpg', '.jpeg', '.png',
                        '.gif', '.bmp', '.webp', '.tiff'}
    if ext and ext.lower() not in image_extensions:
        return f"{kebab_name}{ext}"
    elif ext:
        return f"{kebab_name}{ext}"

    return kebab_name


def rename_files_and_folders(root_dir):
    """
    Recursively rename files and folders in the given directory to kebab-case.

    Args:
        root_dir (str): Root directory to start renaming
    """
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # Rename files
        for name in files:
            old_path = os.path.join(root, name)
            new_name = to_kebab_case(name)
            new_path = os.path.join(root, new_name)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed file: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"Error renaming file {old_path}: {e}")

        # Rename directories
        for name in dirs:
            old_path = os.path.join(root, name)
            new_name = to_kebab_case(name)
            new_path = os.path.join(root, new_name)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed directory: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"Error renaming directory {old_path}: {e}")


def main():
    content_dir = "/Users/wkf/wkf-repos/wahidyankf/ayokoding/apps-standalone/ayokoding-web/content"
    rename_files_and_folders(content_dir)
    print("Renaming process completed.")


if __name__ == "__main__":
    main()
