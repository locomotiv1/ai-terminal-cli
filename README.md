
# AI-Terminal

A powerful Command Line Interface (CLI) tool that translates user requests into executable terminal commands using Google's Gemini API
## Prerequisites

 - [A Google gemini API key](https://aistudio.google.com/api-keys)
 -  Python 3.9 or higher
    
## Installation

1.Clone the repository
```bash
  git clone https://github.com/locomotiv1/ai-terminal.git
  cd ai-terminal
```
2.Install the packages
```bash
pip install .
```

## Configuration
This tool uses the google-genai library, which requires an API Key. You must set this as an environment variable before running.
```
echo 'export GOOGLE_API_KEY="your_actual_api_key_here"' >> ~/.bashrc
```
then reload your shell
```
source ~/.bashrc
```

## Usage/Examples

### Basic Syntax:
```
ai <describe what you want to do>
```
### Examples:
- File Management:
```
ai list all python files in the current directory sorted by size
```
- System Administration:
```
ai check how much disk space is left
```
- Networking:
```
ai find the process using the most memory
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
