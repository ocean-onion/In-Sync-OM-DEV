# In Sync Game Installation Guide

This guide will help you install and run **In Sync Game**, a cooperative card game where players must play cards in ascending order without communication. (This is the developer directory so it contains other tools that are not required for the game.)

## Prerequisites

- Python 3.11 or newer
- `pip` (Python package manager)

## Installation Steps

### 1. Clone the repository

First, clone the repository to your local machine using `git`:

```
git clone https://github.com/ocean-onion/In-Sync-OM-DEV.git
cd In-Sync-OM-Public
```

### 2. Install the required dependencies

Run the following command to install the dependencies:

```
pip3 install -r requirements.txt
```

### 3. Install the game package

Install the In Sync Game package using `pip`:

```bash
pip3 install .
```

> **Note**: If you encounter any errors with `pip3`, make sure Python 3 and pip are correctly installed and available in your environment.

## Running the Game


### 4. Directly run the module:
```bash
python3 -m main
```

You can choose between:
- **S**: Styled game with colours
- **P**: Plain text game
- **T**: Test functions
- **?**: Plus secret games you can find