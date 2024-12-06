#!/usr/bin/python3
"""Convert Markdown files to HTML format."""
import sys
import os


def convert_headings(markdown_text):
    """Convert markdown headings to HTML format."""
    html_lines = []

    for line in markdown_text.split('\n'):
        heading_lvl = 0
        for char in line:
            if char == '#':
                heading_lvl += 1
            else:
                break

        if 0 < heading_lvl <= 6:
            content = line[heading_lvl:].strip()
            html_lines.append(f'<h{heading_lvl}>{content}</h{heading_lvl}>')
        else:
            html_lines.append(line)

    return '\n'.join(html_lines)


def convert_unordered_lists(markdown_text):
    """Convert markdown unordered lists to HTML format."""
    html_lines = []
    in_list = False

    for line in markdown_text.split('\n'):
        stripped_line = line.strip()
        if stripped_line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            content = stripped_line[2:].strip()
            html_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(line)

    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)


def convert_ordered_lists(markdown_text):
    """Convert markdown ordered lists to HTML format."""
    html_lines = []
    in_list = False

    for line in markdown_text.split('\n'):
        stripped_line = line.strip()
        if stripped_line.startswith('* '):
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            content = stripped_line[2:].strip()
            html_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                html_lines.append('</ol>')
                in_list = False
            html_lines.append(line)

    if in_list:
        html_lines.append('</ol>')

    return '\n'.join(html_lines)


def convert_paragraphs(markdown_text):
    """Convert markdown paragraphs to HTML format."""
    html_lines = []
    current_paragraph = []

    for line in markdown_text.split('\n'):
        # Si la ligne contient des balises HTML, l'ajouter directement
        if line.strip().startswith('<') and line.strip().endswith('>'):
            if current_paragraph:
                # Terminer le paragraphe en cours s'il existe
                html_lines.append('<p>')
                for i, p_line in enumerate(current_paragraph):
                    html_lines.append(p_line)
                    if i < len(current_paragraph) - 1:
                        html_lines.append('<br/>')
                html_lines.append('</p>')
                current_paragraph = []
            html_lines.append(line)
        elif line.strip() == '':
            if current_paragraph:
                # Terminer le paragraphe en cours
                html_lines.append('<p>')
                for i, p_line in enumerate(current_paragraph):
                    html_lines.append(p_line)
                    if i < len(current_paragraph) - 1:
                        html_lines.append('<br/>')
                html_lines.append('</p>')
                current_paragraph = []
        else:
            # Ajouter la ligne au paragraphe en cours
            current_paragraph.append(line.strip())

    # Gérer le dernier paragraphe s'il existe
    if current_paragraph:
        html_lines.append('<p>')
        for i, p_line in enumerate(current_paragraph):
            html_lines.append(p_line)
            if i < len(current_paragraph) - 1:
                html_lines.append('<br/>')
        html_lines.append('</p>')

    return '\n'.join(html_lines)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        sys.stderr.write(f'Missing {markdown_file}\n')
        sys.exit(1)

    try:
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()

        html_content = convert_headings(markdown_content)
        html_content = convert_unordered_lists(html_content)
        html_content = convert_ordered_lists(html_content)
        html_content = convert_paragraphs(html_content)

        with open(output_file, 'w') as f:
            f.write(html_content)

        sys.exit(0)
    except Exception as e:
        sys.exit(1)
