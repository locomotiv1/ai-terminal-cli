from setuptools import setup, find_packages

setup(
    name='ai-terminal',
    version='0.1.0',
    description='A CLI tool to translate natural language into Linux commands.',
    author='Kacper R',
    author_email='jdoe@example.com',
    url='https://github.com/yourusername/ai-terminal',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'google-genai',
    ],
    python_requires='>=3.9',
    # 💡 Entry Point (The Magic Part)
    # This creates a command 'ai-terminal' that runs the 'callApi' function
    # inside 'ai_terminal/main.py'.
    entry_points={
        'console_scripts': [
            'ai=ai_terminal.main:aiInit',
        ],
    },
)
