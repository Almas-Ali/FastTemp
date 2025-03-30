<h1 align="center"> FastTemp - A HTML Template Engine </h1>

<p align="center">
<a href="https://github.com/Almas-Ali/FastTemp/"><img src="https://img.shields.io/github/license/Almas-Ali/FastTemp?style=flat-square"></a>
<a href="https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/018c8c58-0154-4fe7-8a63-02c545cc1fa2"><img src="https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/018c8c58-0154-4fe7-8a63-02c545cc1fa2.svg" alt="wakatime"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAlmas-Ali%2FFastTemp&count_bg=%2352B308&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
</p>

<p align="center">FastTemp is a simple, fast, and lightweight template engine for Python. It is still in development, and not ready for production use.
</p>

## The Principles of FastTemp

FastTemp is designed to be fast and easy to use. It has a rich syntax and supports many features. It's syntax highly inspired by [blade](https://laravel.com/docs/10.x/blade#main-content) from [Laravel](https://laravel.com/). We use the similar syntax to blade, but different in some ways. We are not trying to copy blade, but we are trying to make a template engine with a similar syntax to blade which is easy to use and fast. We are also trying to make it as lightweight as possible.

## Features

- [x] Variables
      | Syntax | Description |
      | --- | --- |
      |[x] `@set(variable, value)` | Set a variable |
      |[x] `{variable}` | Print the variable escaped HTML tags |
      |[x] `@safe {variable} @endsafe` | Print the variable with HTML in safe mode |
      |[ ] `@unset(variable)` | Unset a variable |
      |[ ] `@isset(variable) ... @endisset` | Check if a variable is set |
      |[ ] `@empty(variable) ... @endempty` | Check if a variable is empty |

- [x] Comments
      | Syntax | Description |
      | --- | --- |
      |[x] `@comment ... @endcomment` | Comment block |

- [x] Control Structures
      | Syntax | Description |
      | --- | --- |
      |[x] `@if(condition) ... @endif` | If statement |
      |[x] `@if(condition) ... @else ... @endif` | If-else statement |
      |[x] `@unless ... @endunless` | Unless statement |

- [ ] Loops
      | Syntax | Description |
      | --- | --- |
      |[ ] `@for ... @endfor` | For loop |
      |[ ] `@foreach ... @endforeach` | For-each loop |
      |[ ] `@while ... @endwhile` | While loop |

- [ ] Includes
      | Syntax | Description |
      | --- | --- |
      |[ ] `@include ...` | Include a template |

- [ ] Layouts
      | Syntax | Description |
      | --- | --- |
      |[ ] `@extends ...` | Extend a template |
      |[ ] `@section ... @endsection` | Define a section |
      |[ ] `@yield ...` | Yield a section |
      |[ ] `@parent` | Yield the parent section |

- [ ] Built-in Directives
- [ ] Built-in Functions
- [ ] Built-in Filters
- [ ] Built-in Tags

- [ ] Custom Directives
- [ ] Custom Functions
- [ ] Custom Filters
- [ ] Custom Tags

## Installation

```bash
pip install fasttemp
```

## Usage

```python
class FastTemp(
    ContextMixin,
    ResolverMixin,
):
    """FastTemp is a simple, fast, and lightweight template engine for Python."""

    def __init__(
        self,
        *,
        template: str,
        context: Union[Dict[Any, Any], None] = None,
        minify: bool = False,
        pretty: bool = False,
    ) -> None:
        """
        FastTemp is a simple, fast, and lightweight template engine for Python.

        Args:
            template (str): The template string.
            context (Dict[Any, Any], optional): The context variables. Defaults to None.
            minify (bool, optional): Whether to minify the template. Defaults to False.
            pretty (bool, optional): Whether to prettify the template. Defaults to False.
        """


```

```python
from fasttemp import FastTemp

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{description}</p>
    <p>{author}</p>
</body>
</html>
"""

fast_template = FastTemp(
    template=template, # The template
    context={ # The context
        "title": "FastTemp",
        "description": "A HTML Template Engine",
        "author": "Almas Ali",
    }
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

FastTemp is licensed under the [MIT License](LICENSE)
