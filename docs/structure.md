
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
│   └── draft18.py        # Current implementation
│
│
├── games/                # Game implementations
│   ├── plaingame.py      # Plain text version
│   ├── styledgame.py     # Styled version with colours
│   └── testfunc.py       # Testing functions
│
├── unused/               # Unused/unfinished tests/features
│   └── tests*.py         # Individual testing 
│
├── utils/                # Utility functions
│   ├── logo.py           # Ocean-onion logo
│   ├── tools.py          # Developer commands
│   └── utilities.py      # Shared utility functions
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
- **utils/logo.py**: Prints out ocean-onion logo
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