#!/usr/bin/env python3
"""
Script qui convertit un fichier Markdown en HTML
"""
import sys
import os

def main():
    # Vérifier le nombre d'arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    
    # Récupérer les noms de fichiers des arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Vérifier si le fichier Markdown existe
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)
    
    # Si tout va bien, sortir avec le code 0
    sys.exit(0)

if __name__ == "__main__":
    main() 