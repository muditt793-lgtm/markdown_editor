# Markdown Editor

A professional markdown editor with live preview. Write and edit markdown files with real-time preview rendering.

## Features
- Real-time markdown preview
- Full file management (New, Open, Save, Save As)
- Split-pane editor and preview
- Syntax highlighting for markdown elements
- Dark editor theme with light preview
- Support for headers, bold, italic, and code formatting
- Unsaved changes detection
- UTF-8 encoding support

## Requirements
- Python 3.6+
- tkinter (built-in with Python)

## Installation
```bash
python main.py
```

## Project Structure
- `main.py` - Main application file

## Usage
1. **Create New File**: Click "New" to start a fresh document
2. **Open File**: Click "Open" to load an existing markdown file
3. **Edit**: Type or paste markdown content in the left editor panel
4. **Preview**: See real-time rendering in the right preview panel
5. **Save**: Click "Save" to save your work

## Supported Markdown Syntax
- `# Heading 1` - Largest heading (H1)
- `## Heading 2` - Large heading (H2)
- `### Heading 3` - Medium heading (H3)
- `**bold text**` - Bold formatting
- `*italic text*` - Italic formatting
- `` `code` `` - Inline code
- Regular text and paragraphs

## Features in Detail
- **Live Preview**: Changes update instantly as you type
- **File Management**: Create, open, save, and save-as functionality
- **Unsaved Changes**: Indicator shows when you have unsaved work
- **Dark Editor**: Eye-friendly dark theme for writing
- **Light Preview**: High-contrast preview for reading

## Tips
- Use the paned divider to adjust editor/preview width
- Keyboard shortcuts work (Ctrl+Z for undo, etc.)
- Supports .md, .txt, and other text file formats
