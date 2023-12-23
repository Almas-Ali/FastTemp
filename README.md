<h1 align="center"> FastTemp - A HTML Template Engine </h1>

<center>

<a href="https://github.com/Almas-Ali/FastTemp/"><img src="https://img.shields.io/github/license/Almas-Ali/FastTemp?style=flat-square"></a>
<a href="https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/018c8c58-0154-4fe7-8a63-02c545cc1fa2"><img src="https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/018c8c58-0154-4fe7-8a63-02c545cc1fa2.svg" alt="wakatime"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAlmas-Ali%2FFastTemp&count_bg=%2352B308&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>

FastTemp is a simple, fast, and lightweight template engine for Python. It is still in development, and not ready for production use.

</center>

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
