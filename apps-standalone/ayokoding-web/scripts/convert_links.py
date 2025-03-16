import re
import os


def convert_notion_links_to_hugo(input_text):
    """
    Convert Notion-style links to Hugo-friendly relative links.

    Args:
        input_text (str): The markdown text containing Notion links

    Returns:
        str: Markdown text with converted links
    """
    # Regex pattern to match Notion-style links
    notion_link_pattern = r'\[([^\]]+)\]\(<([^>]+)>\)'

    def replace_link(match):
        link_text = match.group(1)
        notion_link = match.group(2)

        # Remove URL encoding and Notion-specific path segments
        clean_link = notion_link.split('/')[-1].replace('%20', ' ')

        # Convert to lowercase, replace spaces with hyphens
        hugo_link = f'./belajar/' + clean_link.lower().replace(' ', '-') + '/'

        return f'[{link_text}]({hugo_link})'

    # Replace all Notion-style links
    converted_text = re.sub(notion_link_pattern, replace_link, input_text)

    return converted_text


def process_markdown_file(file_path):
    """
    Process a markdown file to convert Notion links.

    Args:
        file_path (str): Path to the markdown file
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    converted_content = convert_notion_links_to_hugo(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

    print(f"Processed: {file_path}")


def main():
    # Specify the content directory
    content_dir = '/Users/wkf/wkf-repos/wahidyankf/ayokoding/apps-standalone/ayokoding-web/content'

    # Walk through all markdown files
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('_index.md'):
                file_path = os.path.join(root, file)
                process_markdown_file(file_path)


if __name__ == '__main__':
    main()
