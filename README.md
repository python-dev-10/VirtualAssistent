# VirtualAssistent

### To contribute with this project:

1. Clone this repository in your computer with `git clone https://github.com/Jeferson-Peter/VirtualAssistent.git`;
2. To work correctly with this project, you must have a virtualenv, for this execute in the terminal `pip install virtualenv==20.6.0`;
3. The next step is creating a virtualenv, run `virtualenv env`in the project root directory  and wait for a while;
4. We need to activate the virtualenv for been working on this project, if you are in a Mac or Linux setup, you may run `source env/bin/activate`, if you are in a Windows setup, run `cd env\bin` and then `activate`;
5. In this repository will have a file called `requirements.txt`, we need to watch out here because, its important to keep mantaining the installed version of all packages:
 - First, in your terminal run `pip freeze > requirements.txt`, idiomatically to freeze versions;
 - Secondly, run `pip install -r requirements.txt`, this will install all the packages in the specified versions;

After this simple steps, its time to take our tools and shoot the works!!

Iniciando o projeto: 
- 1: Abra https://www.python.org/downloads/ baixe python e inicio, next next finish, reinicie o computador.
- 2: Abra a pasta do aplicativo no terminal e digite: pip install -r requirements.txt
- 3: Por fim digite: pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

As of September, 09th, the project will follow the PEP8 pattern.

Pay attention on what you will commit from now:
- The code format;
- The max length of characters;
- Spacings/Lines between functions;
- Docstrings;

### MaxLength Character:
By  deafult the PEP8 only allows lines with up to 79 charaters.
```py

def very_long_function(long_variable_name, long_variable_name2, long_variable_name3, long_variable_name4, long_variable_name5):
    pass
```

you can use: `black filename.py`, to reformat the file in the correct pattern

```py

def very_long_function(
    long_variable_name,
    long_variable_name2,
    long_variable_name3,
    long_variable_name4,
    long_variable_name5
):
    pass
```

### Code Format in general:
Checks the style and quality of your Python code.
```py

def function_name(n1, n, n3,
n4, n5):
    print(n1, n2, n3, n4, n5)

function_name(1, 2, 3, 4, 5)
```
you can use: `flake8 filename.py`, to reformat the file in the correct pattern
```py

def function_name(n1, n, n3,n4, n5):
    print(n1, n2, n3, n4, n5)


function_name(1, 2, 3, 4, 5)

```
### Rearranging  the imports:
for rearranging the imports you can use `isort filename.py`

### Docstrings:
```py
class  Test:
    def __init__(self, num) -> None:
        self.num = num 

    def plus_two(self):
        return self.num + 2
```

In the example above we do not have any docstring there, we need to add them to identify what each function provides and do. So for this add docstrings, we use `"""something"""`, three quotations marks instead of `#something`

```py
"""Example of class test"""

class Test:
    """Perform some operation"""
    def __init__(self, num) -> None:
        self.num = num 

    def plus_two(self):
        """Add 2"""
        return self.num + 2
```

the `__init__` method it is not necessary add a docstring, so this method will be ignored. You can use `interrogate -vv filename.py`, to help you to look for the missed docstrings.



