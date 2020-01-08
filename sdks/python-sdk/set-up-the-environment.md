---
description: >-
  Managing several Python versions locally could be a real pain. This guide
  explains how to manage our environment to easily switch between different
  Python versions using pyenv.
---

# Set up the environment

## Why Use `pyenv`?

`pyenv` is a wonderful tool for managing multiple Python versions. Even if you already have Python installed on your system, it is worth having `pyenv` installed so that you can easily try out new language features or help contribute to a project that is on a different version of Python.

You can find more information on the [GitHub](https://github.com/pyenv/pyenv) project repository.

## Installation

Installation couldn't be easier:

```text
curl https://pyenv.run | bash
```

This will install `pyenv` along with a few plugins that are useful:

* **`yenv`**: The actual `pyenv` application
* **`pyenv-virtualenv`**: Plugin for `pyenv` and virtual environments
* **`pyenv-update`**: Plugin for updating `pyenv`
* **`pyenv-doctor`**: Plugin to verify that `pyenv` and build dependencies are installed
* **`pyenv-which-ext`**: Plugin to automatically lookup system commands

Add the following lines to your `.bashrc` or `.zshrc` files:

```text
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## Basic Usage

`pyenv` allows to install both specific version per project and a global one. Let's install a global Python 3.6 version:

```text
pyenv install 3.6.8
```

You can check the available versions using the following command:

```text
pyenv install --list
```

Finally, check that the new version has been installed correctly:

```text
python --version

Python 3.6.8
```

