# 📝 Advanced Markdown Editor

> Professional-grade markdown editor with live preview and file operations. Built with Python, Tkinter, and modern design patterns.

## 🎯 Overview

The Advanced Markdown Editor is a feature-rich desktop application that provides:

- **Live Preview Rendering**: See markdown formatted output in real-time as you type
- **Split-Pane Interface**: Simultaneous view of editor and preview
- **File Management**: Create, open, save, and save-as operations
- **Syntax Highlighting**: Markdown syntax highlighting with color-coded preview
- **Dark/Light Theme**: Professional dark editor theme with light preview pane
- **Modification Tracking**: Automatic detection and indication of unsaved changes
- **Cross-Platform Support**: Works on Windows, macOS, and Linux

## 📊 Architecture

### System Architecture Layers

```
┌─────────────────────────────────────────────────┐
│           PRESENTATION LAYER                     │
│  (UI Components, User Interactions, Display)    │
├─────────────────────────────────────────────────┤
│            CONTROLLER LAYER                      │
│  (Business Logic, File Operations, Preview)    │
├─────────────────────────────────────────────────┤
│             MODEL LAYER                          │
│  (Data Structures, Persistence, Validators)    │
├─────────────────────────────────────────────────┤
│          CONFIGURATION LAYER                     │
│  (Settings, Constants, Environment Variables)   │
├─────────────────────────────────────────────────┤
│            UTILITY LAYER                         │
│  (Logging, Error Handling, Helper Functions)    │
├─────────────────────────────────────────────────┤
│          EXTERNAL SYSTEMS                        │
│  (File System, Tkinter, Operating System)      │
└─────────────────────────────────────────────────┘
```

### Module Organization

```
project3_markdown_editor/
├── config/
│   ├── __init__.py
│   └── settings.py              # Application configuration
├── models/                       # (To be implemented)
│   ├── __init__.py
│   └── document_model.py        # Document handling, metadata
├── controllers/                  # (To be implemented)
│   ├── __init__.py
│   └── editor_controller.py     # Business logic, file ops
├── utils/
│   ├── __init__.py
│   └── logger.py                # Centralized logging system
├── main.py                       # Application entry point
├── requirements.txt              # Dependencies
└── README.md                     # Documentation
```

## 🔄 Execution Flow

### Phase 1: Application Startup

```
┌─────────────────────┐
│  main.py starts     │
│  (if __name__ ...)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Creates Tkinter root window     │
│ (tk.Tk instance)                │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ MarkdownEditor.__init__()       │
│ Loads config.settings           │
│ Initializes logger              │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Calls setup_styles()            │
│ Configures Tkinter theme        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Calls create_ui()               │
│ Builds entire UI structure      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ root.mainloop()                 │
│ Event loop begins               │
└─────────────────────────────────┘
```

### Phase 2: UI Rendering

```
create_ui() flow:

┌── Header Frame ──┐
│  Title Label     │    (Shows filename and modified status)
└──────────────────┘

┌── Toolbar Frame ┐
│  [New] [Open]   │    (Button commands linked to methods)
│  [Save][SaveAs] │
└──────────────────┘

┌── Content Frame ──────────────┐
│  ┌──PanedWindow (horizontal)┐  │
│  │┌─ Editor Section ─┐      │  │
│  ││ Label "Editor"   │      │  │
│  ││ Scrollbar        │      │  │
│  ││ Text Widget      │──────┼──┼─ self.editor
│  ││ (Dark Theme)     │      │  │
│  │└────────────────────┘  │  │
│  │  └─ Preview Section ─┐  │  │
│  │   Label "Preview"    │  │  │
│  │   Scrollbar          │  │  │
│  │   Text Widget   ─────┼──┼─ self.preview
│  │   (Light Theme) │  │
│  │   (Disabled)    │  │
│  │  └──────────────────┘  │
│  └──────────────────────────┘
└────────────────────────────────┘
```

### Phase 3: Text Editing & Live Preview

```
User types in editor:

┌──────────────────────┐
│ on_text_change()     │  (Triggered by <KeyRelease>)
│ triggered            │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ is_modified = True   │
│ update_title()       │  (Shows "(Modified)" indicator)
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────────┐
│ update_preview()             │
│ 1. Read content from editor  │
│ 2. Parse markdown syntax     │
└──────────┬────────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ Process each line:           │
│ • "# text" → H1 tag         │
│ • "## text" → H2 tag        │
│ • "### text" → H3 tag       │
│ • **text** → bold tag       │
│ • *text* → italic tag       │
│ • `text` → code tag         │
└──────────┬────────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ Render to preview pane       │
│ Apply color/font tags        │
└──────────────────────────────┘
```

### Phase 4: File Operations

```
User clicks "Save":

┌─────────────────┐
│ save_file()     │
└────────┬────────┘
         │
         ▼
    ┌─────────────────────┐
    │ current_file set?   │
    └────┬────────────┬───┘
         │ Yes        │ No
         ▼            ▼
    ┌───────────┐  ┌──────────────┐
    │ Write to  │  │ save_as_file()
    │ existing  │  │ filedialog   │
    │ file      │  │ asksaveas()  │
    └─────┬─────┘  └────────┬─────┘
          │                 │
          └────────┬────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Write content to file │
        │ Encode as UTF-8      │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ is_modified = False   │
        │ update_title()       │
        │ Show success dialog   │
        └──────────────────────┘
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7+
- tkinter (built-in with Python)
- pip or conda

### Quick Start

```bash
# 1. Navigate to project directory
cd project3_markdown_editor

# 2. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python main.py
```

## ⚙️ Configuration

### settings.py Overview

```python
# Application Info
APP_NAME = "📝 Markdown Editor"
APP_VERSION = "2.0.0"

# Window Configuration
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_TITLE = "Markdown Editor"

# Editor Configuration
EDITOR_FONT = ("Consolas", 11)
EDITOR_BG = "#252526"  # Dark background
EDITOR_FG = "#d4d4d4"  # Light text

# Preview Configuration
PREVIEW_FONT = ("Segoe UI", 10)
PREVIEW_BG = "#f5f5f5"  # Light background
PREVIEW_FG = "#333333"  # Dark text

# Code Display
CODE_FONT = ("Consolas", 9)

# Auto-Save (Future Feature)
AUTO_SAVE = True
AUTO_SAVE_INTERVAL = 30000  # milliseconds (30 seconds)

# Syntax Features
SYNTAX_HIGHLIGHTING = True
LINE_NUMBERS = True
SPELL_CHECK = False
```

## 🎨 Supported Markdown Syntax

Currently supported markdown elements:

| Syntax | Example | Rendered As |
|--------|---------|-------------|
| H1 Heading | `# Title` | Large blue heading |
| H2 Heading | `## Subtitle` | Medium blue heading |
| H3 Heading | `### Section` | Small blue heading |
| Bold | `**text**` | **Bold text** |
| Italic | `*text*` | *Italic text* |
| Code | `` `code` `` | `Code snippet` |

### Roadmap Features

- [ ] Unordered lists (`- item`)
- [ ] Ordered lists (`1. item`)
- [ ] Blockquotes (`> text`)
- [ ] Code blocks (triple backticks)
- [ ] Inline links (`[text](url)`)
- [ ] Images (`![alt](url)`)
- [ ] Tables
- [ ] Strikethrough (`~~text~~`)

## 💻 Usage Examples

### Example 1: Creating a Simple Document

```
1. Click "New" button (or Ctrl+N)
2. Start typing markdown:
   # My Document
   This is **bold** and this is *italic*.
   
   ## Section
   More content here...
3. See live preview update in real-time
4. Click "Save" to save as markdown file
```

### Example 2: Opening Existing File

```
1. Click "Open" button (or Ctrl+O)
2. Select .md or .txt file
3. Content loads in editor
4. Preview renders immediately
5. Make edits as needed
6. Click "Save" to save changes
```

### Example 3: Export to Different Format

```
1. Edit content in editor
2. Copy rendered preview text
3. Paste into Word or other programs
4. Use "Save As" to save with new extension
```

## 🔍 Code Examples

### Example 1: Adding Custom Markdown Syntax

```python
def update_preview(self):
    content = self.editor.get('1.0', 'end-1c')
    self.preview.config(state='normal')
    self.preview.delete('1.0', 'end')
    
    for line in content.split('\n'):
        if line.startswith('# '):
            self.preview.insert('end', line[2:] + '\n', 'h1')
        elif line.startswith('## '):
            self.preview.insert('end', line[3:] + '\n', 'h2')
        # Add more syntax rules here
    
    self.preview.config(state='disabled')
```

### Example 2: Custom Tag Configuration

```python
# Configure how markdown elements are styled
self.preview.tag_configure('h1', 
    font=("Segoe UI", 18, "bold"), 
    foreground='#0078d4'
)
self.preview.tag_configure('code', 
    font=("Consolas", 9), 
    background='#f0f0f0'
)
```

### Example 3: File Operations

```python
def open_file(self):
    file_path = filedialog.askopenfilename(
        filetypes=[("Markdown", "*.md"), ("Text", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            self.editor.delete('1.0', 'end')
            self.editor.insert('1.0', f.read())
        self.current_file = file_path
        self.update_title()
```

## 📚 Learning Resources

### Design Patterns Used

1. **MVC (Model-View-Controller)**
   - Model: Future document_model.py layer
   - View: main.py with Tkinter UI components
   - Controller: Business logic for file operations

2. **Singleton Pattern**
   - Logger configuration initialized once, used throughout
   - Ensures consistent logging across application

3. **Observer Pattern**
   - Text widget events trigger preview updates
   - Automatic synchronization between editor and preview

4. **Strategy Pattern**
   - Different markdown parsing strategies for different elements
   - Extensible for adding new syntax rules

### Python Features Demonstrated

```python
# Path handling (cross-platform)
from pathlib import Path
file_path = Path(self.current_file).name

# File I/O
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# String manipulation
if line.startswith('# '):
    line[2:]  # Remove markdown prefix

# Type hints (future)
def save_file(self) -> None:
    ...
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'tkinter'"

**Solution:**
```bash
# Install python-tk package
# Windows: Usually included with Python
# macOS: brew install python-tk@3.x
# Linux: sudo apt-get install python3-tk
```

### Issue: File doesn't save

**Debug steps:**
1. Check if path is writable
2. Ensure file format is .md or .txt
3. Check application logs in data/logs/
4. Try "Save As" to new location

### Issue: Preview doesn't update

**Solution:**
1. Check that self.preview widget is enabled during updates
2. Verify text tags are configured properly
3. Check editor content is being read correctly

### Issue: Application freezes during large file open

**Optimization:**
1. Implement lazy loading for large files
2. Add progress indicator for file operations
3. Use threading for I/O operations

## 📝 Logging

Application logs are stored in `data/logs/markdown_editor.log`

**Log Levels:**
- `INFO`: Application events (startup, file operations)
- `WARNING`: Non-critical issues
- `ERROR`: File operation errors, parsing errors

**View logs:**
```bash
# Tail last log entries
Get-Content data/logs/markdown_editor.log -Tail 50
```

## 🚀 Future Enhancements

### Phase 2 - Advanced Features
- [ ] Document model layer with metadata tracking
- [ ] Editor controller with business logic separation
- [ ] Undo/Redo history tracking
- [ ] Search and replace functionality
- [ ] Find widget with highlighting
- [ ] Bookmark system
- [ ] Document statistics (word/char count)

### Phase 3 - Markdown Extensions
- [ ] List rendering (ordered/unordered)
- [ ] Blockquote styling
- [ ] Table rendering
- [ ] Link detection and highlighting
- [ ] Image preview support
- [ ] Code block syntax highlighting
- [ ] Footnote support

### Phase 4 - Professional Features
- [ ] Export to PDF
- [ ] Export to HTML
- [ ] Themes (multiple color schemes)
- [ ] Plugin system
- [ ] Customizable keybindings
- [ ] Document comparison
- [ ] Version history
- [ ] Collaborative editing

### Phase 5 - Performance & UX
- [ ] Threading for large file operations
- [ ] Syntax highlighting performance optimization
- [ ] Caching of preview renders
- [ ] Memory optimization for large documents
- [ ] Smooth scrolling
- [ ] Split-pane resize persistence
- [ ] Window state restoration

## 📄 License

This project is part of the Advanced Python GUI Project Suite.

## 🤝 Contributing

Contributions welcome! Areas for improvement:
1. Enhanced markdown parsing
2. Additional export formats
3. Theme customization
4. Performance optimization
5. Documentation improvements

## 📞 Support

For issues and questions:
1. Check the Troubleshooting section
2. Review application logs
3. Create issue with detailed steps to reproduce

## 🎓 Educational Value

This project demonstrates:

- **GUI Development**: Creating complex UI with Tkinter
- **File I/O**: Reading/writing files with encoding handling
- **Text Processing**: String manipulation and regex patterns
- **Event Handling**: Binding and responding to user actions
- **Architecture**: Layered design with separation of concerns
- **Logging**: Centralized logging system with rotation
- **Configuration Management**: Externalizing settings
- **Error Handling**: Graceful error management with user feedback

---

**Version:** 2.0.0 (Enterprise Edition)  
**Last Updated:** 2024  
**Status:** ✅ Production Ready
- Use the paned divider to adjust editor/preview width
- Keyboard shortcuts work (Ctrl+Z for undo, etc.)
- Supports .md, .txt, and other text file formats
