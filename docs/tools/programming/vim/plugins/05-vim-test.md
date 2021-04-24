---
title: "Vim Test"
summary:
---

Vim Test
===

Links
---

- [:fontawesome-brands-github: vim-test](https://github.com/vim-test/vim-test)

Config
---

```vim
nmap <silent> t<C-n> :TestNearest<CR>
nmap <silent> t<C-f> :TestFile<CR>
nmap <silent> t<C-s> :TestSuite<CR>
nmap <silent> t<C-l> :TestLast<CR>
nmap <silent> t<C-g> :TestVisit<CR>

let test#strategy = "vimux"
let test#python#runner = 'pytest'
```


Customisations for docker
---

[:fontawesome-brands-github: Inspiration](https://github.com/vim-test/vim-test/issues/254).

```vim
" the idea is to take any command and transform it so it can be used with
" docker-compose (or docker)
function! DockerTransform(cmd)
    let l:stripped_cmd = substitute(a:cmd, "project/", "", "g")
    " let l:stripped_cmd = substitute(l:stripped_cmd, "pytest", "pytest -m 'not filebeat'", "g")
    let l:docker_cmd = "docker-compose exec web bash -c \"".l:stripped_cmd."\""
    return l:docker_cmd
    endfunction

let g:test#custom_transformations = {'docker': function('DockerTransform')}
let g:test#transformation = 'docker'
```

This will take a command like:

```
pytest project/tests/test_summaries.py::test_create_summary
```

and convert it into:

```
docker-compose exec web bash -c \
    "pytest tests/test_summaries.py::test_create_summary"
```

The original command has `project` because of Vim's working directory, and the
docker container has `tests` in the `WORKDIR`, so `project` has to be removed.
