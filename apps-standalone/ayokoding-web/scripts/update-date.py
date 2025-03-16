#!/usr/bin/env python3

import os
import re
from datetime import datetime

CONTENT_DIR = "../content"
TARGET_DATE = "2025-03-16T07:20:00+07:00"

def update_frontmatter_date(content, new_date):
    # Check if content has frontmatter
    if not content.startswith('---\n'):
        return content

    # Split content into frontmatter and body
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return content

    frontmatter, body = parts[1], parts[2]
    
    # Update or add date in frontmatter
    date_pattern = re.compile(r'^date:\s*.*$', re.MULTILINE)
    if re.search(date_pattern, frontmatter):
        new_frontmatter = date_pattern.sub(f'date: {new_date}', frontmatter)
    else:
        new_frontmatter = frontmatter.rstrip() + f'\ndate: {new_date}\n'

    # Reconstruct the document
    return f'---\n{new_frontmatter}---\n{body}'

def process_markdown_files():
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                
                # Read file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update content
                updated_content = update_frontmatter_date(content, TARGET_DATE)
                
                # Write back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

if __name__ == '__main__':
    process_markdown_files()
