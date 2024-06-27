
# Display Icons Program

This Python program allows users to select and display icons fetched from the GitHub Emojis API.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)

## Features
1. Fetches a list of icon names from the GitHub Emojis API.
2. Allows users to:
   - Print all icon names.
   - Search icons by keyword (case-insensitive).
   - Display a selected icon.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/sariwaisbeker/display-icons.git
   cd display-icons
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the program:**
   ```sh
   python display_icons.py
   ```

2. **Select an option:**
   - `1`: Print all icons.
   - `2`: Search icons by keyword.

## Functions

- **print_all_icons()**: Prints the full list of icon names.
- **search_icons_by_keyword(keyword)**: Filters icons based on the keyword and displays the search results.
- **display_icon(icon_name)**: Displays the selected icon using the PIL library.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

Feel free to reach out with any questions or feedback. Happy coding!
