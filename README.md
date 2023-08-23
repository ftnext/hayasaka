# hayasaka

Hayasaka saves the rendered HTML as an image.

## Use cases

- Save the slides (an HTML file) using [reveal.js](https://revealjs.com/) as an image

⚠️To Run hayasaka, you currently need to have the **Firefox** browser installed (Google Chrome will be supported in the future).

## Installation

```sh
$ pip install hayasaka
```

## Usage

📸Generate an image from URL

```sh
$ hayasaka-cli https://ftnext.github.io/2022_slides/pyconjp/python_and_star.html python_and_star.png
```

📸Generate an image from a local HTML file path

```sh
$ hayasaka-cli ../2022_slides/build/revealjs/pyconjp/python_and_star.html python_and_star.png
```

## Development environment

```sh
$ git clone git@github.com:ftnext/hayasaka.git
$ cd hayasaka

$ python3.11 -m venv venv --upgrade-deps
$ source venv/bin/activate

(venv) $ pip install -e '.[dev]'
(venv) $ task test
```
