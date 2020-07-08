# PDF Protecter

Desktop GUI applications to encryption and decription PDF files with Python3 using PyQT5 graphic modul.

## Demo

![program-demo](https://user-images.githubusercontent.com/34337622/86960486-deaaa280-c15f-11ea-9723-71fc0986de2a.gif)

## Technologies

-   Python 3.7
-   PyQT5 graphic module
-   PyPDF2

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installing/)
-   [pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip)

## Installation

-   [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo to your local machine using:

```
$ git clone https://github.com/tarnowski-git/Simple_Note_Recognizer.git
```

-   Setup your [local environment](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv):

```
# Spawn a shell with the virtualenv activated
$ pipenv shell

# Install dependencies
$ pipenv install

# Run script into local environment
$ pipenv run python pdf_protecter.py
```

-   Compile with Pyinstaller to exectutable file:

```
# Windows
pyinstaller --hidden-import pkg_resources.py2_warn --onefile --windowed pdf_protecter.py
```

## [License](https://github.com/tarnowski-git/PDF_Protecter/blob/master/LICENSE)

MIT © [Konrad Tarnowski](https://github.com/tarnowski-git)
