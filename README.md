[![Latest Version](https://img.shields.io/pypi/v/cccp.svg)](https://pypi.python.org/pypi/cccp) [![Python Support](https://img.shields.io/pypi/pyversions/cccp.svg)](https://pypi.python.org/pypi/cccp)

# CCCP - Semi Server Side Rendered ☭

CCCP uses [dominate](https://github.com/Knio/dominate) for generation of HTML in Python but **extends it with JavaScript snippets**

Includes:

* Custom elements that can be rendered:
    * Function declarations for simple DOM manipulation
    * Indludes of external scripts (like jquery etc.)
* Render function that can take a single or lists of *dominate HTML elements*

## HTML tag manipulation using external sourcecode from GET's

CCCP currently includes the following functions:

(They all work by fetching html from a remote endpoint and manipulating a HTML tag with a given **id**)

* **ReplaceHtml(url, id)**: Lets you replace the contents of an HTML tag
* **AppendHtml(url, id)**: Lets you append to the end of a HTML tag
* **PrependHtml(url, id)**: Lets you prepend to the beginning of a HTML tag

## Usage

Install from **PYPI** (also installs [dominate](https://github.com/Knio/dominate)):

```
$ pip install cccp
```

Import modules:
```
from dominate import tags as t
import cccp
```

Include needed definitions in HTML Head:

```
t.head(
        [
            cccp.REQUIRED,
            cccp.BOOTSTRAP,
            cccp.CreateReplaceHtmlFunc()
        ]
    )
],
t.body(
    [
        div(id="pageContent")
    ]
)
```

Use functions inside HTML to manipulate select DOM elements:

```
t.button(
    "go to blog",
    onClick=cccp.replaceHtml(
        "http://127.0.0.1:9999/page/1", "pageContent"
    ),
)
```

☝️This will replace the contents of the div `"pageContent"` with the **HTML** it `GET`'s from `"http://127.0.0.1:9999/page/1"`

see [examples/flask_example.py](https://github.com/sloev/cccp/blob/master/examples/flask_example.py) for a full demo!

## RoadMap

- [x] Simple functions for replacing/appending/prepending of DOM elements
- [x] Elements for popular js dependencies:
    - [x] **axios** used for HTTP requests (performs GET requests)
    - [x] **jquery** used for HTTP requests (does the DOM manipulation)
- [ ] Error handling in bundled javascript functions
- [ ] Simple **html forms** using **json-schema** for form validation etc
- [ ] Implement tests
- [ ] **chartjs**:
    - [ ] Element for including library
    - [ ] Functions for creating different kinds of interactive charts
- [ ] More DOM manipulation javascript functions:
    - [ ] Function for creating a [Comet](https://en.wikipedia.org/wiki/Comet_(programming)) call and replacing/prepending/appending incomming html to the DOM
    - [ ] Functions for deleting DOM elements
    - [ ] Functions for pulling regularily (timer interupt GET's)
