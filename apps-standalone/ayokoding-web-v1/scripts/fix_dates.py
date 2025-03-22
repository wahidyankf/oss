#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_date_format(content):
    # Pattern to match the invalid date format with double colons
    date_pattern = r'date:\s*(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}):(:)(\d{2})'
    
    # Replace double colons with single colon
    fixed_content = re.sub(date_pattern, r'date: \1T\2:\4', content)
    
    return fixed_content

def process_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    fixed_content = fix_date_format(content)
                    
                    if content != fixed_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(fixed_content)
                        print(f'Fixed date format in: {file_path}')
                except Exception as e:
                    print(f'Error processing {file_path}: {str(e)}')

if __name__ == '__main__':
    content_dir = Path('/Users/wkf/wkf-repos/wahidyankf/ayokoding/apps-standalone/ayokoding-web/content')
    process_markdown_files(content_dir)
