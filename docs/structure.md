
# Project Structure

In Sync Game project is organized as follows:

```
In-Sync-DEV/
├── docs/                 # Documentation
│   ├── cs_doc.md         # Computer Science Task 2 planing documentation
│   ├── development.md    # Development history
│   ├── gantt_chart.md    # Project timeline
│   ├── install.md.       # Installation instructions for project
│   ├── plan.md           # Initial game plan
│   ├── structure.md      # Project Structure
│   ├── pseudocode.md     # Pseudocode for functions
│   ├── test_table.md     # Test cases and results
│   └── fixes/            # Documentation for bug fixes
│       ├── fixs.md       # Overview of fixes
│       └── fix*.md       # Individual fix documentation
│
├── drafts/               # Previous code versions
│   ├── draft*.py         # Draft code verisons
│   └── draft14.py        # Current implementation
│
│
├── games/                # Game implementations
│   ├── plaingame.py      # Plain text version
│   ├── styledgame.py     # Styled version with colours
│   └── testfunc.py       # Testing functions
│
│
├── utils/                # Utility functions
│   ├── tools.py          # Developer commands
│   └── utilities.py       # Shared utility functions
│
│
├── LICENSE               # License
├── main.py               # Entry point
└── README.md             # Brief overview
```

## Key Files:

- **main.py**: Entry point for the application allowing choice between styled and plain versions
- **games/plaingame.py**: Implementation with plain text (no styling)
- **games/styledgame.py**: Implementation with styled text (colours and effects)
- **utils/utilities.py**: Shared utility functions used by both implementations
- **utils/tools.py**: Developer commands for testing and debugging
- **games/testfunc.py**: Testing utilities for individual functions

## Documentation:

- **README.md**: Brief overview of the project
- **LICENSE**: License for use of the code
- **docs/cs_doc.md**: Computer Science documentation for task 2 with project plan, features, and timeline
- **docs/development.md**: History of development stages with key improvements
- **docs/gantt_chart.md**: Project timeline visualization
- **docs/install.md**: Installation instructions for the project 
- **docs/plan.md**: Original planning document
- **docs/pseudocode.md**: Pseudocode for key functions
- **docs/test_table.md**: Test cases and results
- **docs/fixes/**: Documentation of bug fixes and improvements

## Development History:

The game has evolved through ten drafts, with each version improving on the previous one:
1. **Draft 1**: Basic game mechanics
2. **Draft 2**: Improved input validation
3. **Draft 3**: Player privacy implementation
4. **Draft 4**: Added helper functions
5. **Draft 5**: Enhanced user interface
6. **Draft 6**: Real-time game system
7. **Draft 7**: Improved function naming
8. **Draft 8**: Split into plain and styled versions
9. **Draft 9**: Added developer commands
10. **Draft 10**: Bug fixes and refactoring
11. **Draft 11**: Refactoring and improved formatting
12. **Draft 12**: Improved game flow and readability
13. **Draft 13**: Improved developer tools and game flow
14. **Draft 14**: Added welcome message and loading screens
