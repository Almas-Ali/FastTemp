# FastTemp - A HTML Template Engine

FastTemp is a simple, fast, and lightweight template engine for Python. It is still in development, and not ready for production use.

## The Principles of FastTemp

FastTemp is designed to be fast and easy to use. It has a rich syntax and supports many features. It's syntax highly inspired by [blade](https://laravel.com/docs/10.x/blade#main-content) from [Laravel](https://laravel.com/). We use the similar syntax to blade, but different in some ways.

## Features

- [x] Variables
    | Syntax | Description |
    | --- | --- |
    | `{variable}` | Print the variable |
    | `{% variable %}` | Print the variable with HTML escaped |

- [x] Comments
    | Syntax | Description |
    | --- | --- |
    | `@comment ... @endcomment` | Comment block |

- [x] Control Structures
    | Syntax | Description |
    | --- | --- |
    | `@if(condition) ... @endif` | If statement |
    | `@if(condition) ... @else ... @endif` | If-else statement |
    | `@unless ... @endunless` | Unless statement |
    
- [] Loops
    | Syntax | Description |
    | --- | --- |
    | `@for ... @endfor` | For loop |
    | `@foreach ... @endforeach` | For-each loop |
    | `@while ... @endwhile` | While loop |

- [] Includes
    | Syntax | Description |
    | --- | --- |
    | `@include ...` | Include a template |

- [] Layouts
    | Syntax | Description |
    | --- | --- |
    | `@extends ...` | Extend a template |
    | `@section ... @endsection` | Define a section |
    | `@yield ...` | Yield a section |
    | `@parent` | Yield the parent section |

- [] Built-in Directives
- [] Built-in Functions
- [] Built-in Filters
- [] Built-in Tags

- [] Custom Directives
- [] Custom Functions
- [] Custom Filters
- [] Custom Tags
