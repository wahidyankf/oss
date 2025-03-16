#!/usr/bin/env python3

"""
Update Date Script for Ayokoding Website

This script updates the 'date' field in the frontmatter of all Markdown files
within the content directory. It's particularly useful for maintaining consistent
timestamps across documentation pages.

The script:
1. Recursively finds all Markdown files in the content directory
2. Updates or adds a 'date' field in the YAML frontmatter
3. Preserves all other content and formatting

Usage:
    ./update-date.py

Note: This script assumes Markdown files use YAML frontmatter delimited by '---'
"""

import os
import re

# Configuration constants
CONTENT_DIR = "../content"  # Root directory containing Markdown files
TARGET_DATE = "2025-03-16T07:20:00+07:00"  # Target date in ISO 8601 format


def update_frontmatter_date(content, new_date):
    """
    Update or add the date field in a Markdown file's frontmatter.

    Args:
        content (str): The full content of the Markdown file
        new_date (str): The new date to set in ISO 8601 format

    Returns:
        str: Updated content with the new date in frontmatter

    The function handles three cases:
    1. Files without frontmatter - returns unchanged
    2. Files with frontmatter but no date - adds date field
    3. Files with existing date - updates the date
    """
    # Skip files without frontmatter
    if not content.startswith('---\n'):
        return content

    # Split content into frontmatter and body
    # The split should result in: ['', frontmatter, body]
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return content

    frontmatter, body = parts[1], parts[2]

    # Regular expression to match the date field in frontmatter
    date_pattern = re.compile(r'^date:\s*.*$', re.MULTILINE)
    
    # Update existing date or add new date field
    if re.search(date_pattern, frontmatter):
        # Replace existing date
        new_frontmatter = date_pattern.sub(f'date: {new_date}', frontmatter)
    else:
        # Add new date field, ensuring proper spacing
        new_frontmatter = frontmatter.rstrip() + f'\ndate: {new_date}\n'

    # Reconstruct the document preserving the original structure
    return f'---\n{new_frontmatter}---\n{body}'


def process_markdown_files():
    """
    Recursively process all Markdown files in the content directory.
    
    Walks through the content directory tree, identifies Markdown files,
    and updates their frontmatter dates using update_frontmatter_date().
    
    Side effects:
        - Prints processing status for each file
        - Modifies Markdown files in place
    """
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")

                # Read file content with UTF-8 encoding
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Update the frontmatter date
                updated_content = update_frontmatter_date(content, TARGET_DATE)

                # Write the updated content back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)


if __name__ == '__main__':
    process_markdown_files()
