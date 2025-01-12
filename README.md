<p align="center">
  <a href="https://academic.oup.com/brain/advance-article-abstract/doi/10.1093/brain/awae417/7950911?redirectedFrom=fulltext&login=false">
      <img width="20%" src="https://img.freepik.com/premium-photo/brain-logo-icon-human-brain-icon-creative-simple-mind-symbol-vector-illustration_1162225-51928.jpg?w=740" alt="Brianlytics" />
      <h1 align="center">Brianlytics</h1>
  </a>
</p>

# Main Source/Article:
https://academic.oup.com/brain/advance-article-abstract/doi/10.1093/brain/awae417/7950911?redirectedFrom=fulltext&login=false

# Data:
<links to your data>

# Documentation:
<Drive link to code general workflow/pipeline> (If not too complicated, add the project's documentation directly under this topic)

# List of usefull commands:
all command should run under project root/working-directory

## Project init:
```bash 
#install Virtualenv is - a tool to set up your Python environments
pip install virtualenv
#create virtual environment (serve only this project):
python -m venv venv
#activate virtual environment
.\venv\Scripts\activate
+ (venv) should appear as prefix to all command (run next command just after activating venv)
#update venv's python package-installer (pip) to its latest version
python.exe -m pip install --upgrade pip
#install projects packages (Everything needed to run the project)
pip install -e .
#install dev packages (Additional packages for linting, testing and other developer tools)
pip install -e .[dev]
``` 
