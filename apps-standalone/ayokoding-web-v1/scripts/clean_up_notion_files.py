import os
import re
import yaml
from datetime import datetime


def sanitize_frontmatter_value(value):
    """Sanitize values for YAML frontmatter compliance"""
    sanitized = str(value).replace('"', '\\"')
    return f'"{sanitized}"'


def extract_title_from_markdown(file_path):
    """
    Extract the first H1 title from a markdown file.

    Args:
        file_path (str): Path to the markdown file

    Returns:
        str: Title extracted from the first H1, or filename if no H1 found
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Look for H1 markdown title
                if line.strip().startswith('# '):
                    return line.strip()[2:].strip()
    except Exception as e:
        print(f"Error extracting title from {file_path}: {e}")

    # Fallback to filename without extension
    return os.path.splitext(os.path.basename(file_path))[0].replace('-', ' ').title()


def validate_frontmatter(content):
    try:
        yaml.safe_load(content.split('---\n')[1])
        return True
    except Exception as e:
        print(f"Invalid frontmatter: {str(e)}")
        return False


def add_frontmatter_to_markdown(file_path):
    """
    Add frontmatter to markdown files if it doesn't exist.

    Args:
        file_path (str): Path to the markdown file
    """
    try:
        # Read the current content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if frontmatter already exists
        if content.startswith('---\n') and '---\n' in content[4:]:
            return

        # Extract title
        title = extract_title_from_markdown(file_path)

        # Get current datetime in the specified timezone
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%dT%H:%M:%S%z')
        # Adjust timezone format to match Hugo's requirement
        formatted_time = formatted_time[:-2] + ':' + formatted_time[-2:]

        # Create frontmatter
        frontmatter = f"""---
title: {sanitize_frontmatter_value(title)}
date: {formatted_time}
draft: false
---

"""

        # Combine frontmatter with existing content
        updated_content = frontmatter + content.lstrip()

        # Validate frontmatter
        if validate_frontmatter(updated_content):
            # Write back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Added frontmatter to {file_path}")
        else:
            print(f"Skipping invalid frontmatter in {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


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
    # First, process files that need to be moved to sibling folders
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            # Delete .DS_Store files
            if name.lower() == 'ds-store':
                try:
                    os.remove(os.path.join(root, name))
                    print(f"Deleted file: {os.path.join(root, name)}")
                    continue
                except Exception as e:
                    print(
                        f"Error deleting file {os.path.join(root, name)}: {e}")

            # Check if it's a markdown file
            if name.lower().endswith('.md') and name.lower() != '_index.md':
                base_name = os.path.splitext(name)[0]

                # Check if a sibling folder with the same name exists
                # Check in current directory first
                sibling_dir = os.path.join(root, base_name)

                # If not in current directory, check in parent directory
                if not os.path.isdir(sibling_dir):
                    parent_dir = os.path.dirname(root)
                    sibling_dir = os.path.join(parent_dir, base_name)

                if os.path.isdir(sibling_dir):
                    old_path = os.path.join(root, name)
                    new_path = os.path.join(sibling_dir, '_index.md')

                    try:
                        os.rename(old_path, new_path)
                        print(f"Moved and renamed: {old_path} -> {new_path}")
                    except Exception as e:
                        print(f"Error moving file {old_path}: {e}")

    # Then proceed with renaming files and folders
    for root, dirs, files in os.walk(root_dir, topdown=False):
        # Rename files
        for name in files:
            old_path = os.path.join(root, name)
            new_name = to_kebab_case(name)

            # Special handling to ensure index.md becomes _index.md
            if new_name == 'index.md':
                new_name = '_index.md'

            new_path = os.path.join(root, new_name)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed file: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"Error renaming file {old_path}: {e}")

            # Add frontmatter to markdown files
            if new_name.lower().endswith('.md'):
                add_frontmatter_to_markdown(new_path)

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


def delete_ds_store_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file == '.DS_Store':
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")


def main():
    content_dir = os.path.join(os.getcwd(), 'content')
    delete_ds_store_files(content_dir)
    rename_files_and_folders(content_dir)
    print("Cleanup process completed.")


if __name__ == "__main__":
    main()
