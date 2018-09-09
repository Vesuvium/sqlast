# SqlAst

An SQL parser that uses LALR (instead of regex), providing precise, accurate
and complete SQL parsing. SqlAst is meant to be used as library, but a cli is
also provided.

Once the SQL is parsed, is provided as an abstract syntax tree that can be used
to transpile to another language, for example in an SQL to YAML transpiler,
to analyse the sql file, or to write your own SQL interpreter.


## Installing

```sh
pip install sqlast
```

## Usage

```python
from sqlast.App import SqlAst


tree = SqlAst.parse('hello.sql')
print(tree.pretty())
```

### Cli

```sh
sqlast parse hello.sql
```
