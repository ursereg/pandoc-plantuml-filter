# pandoc-plantuml-filter

Pandoc filter which converts PlantUML code blocks to PlantUML images.

````
```plantuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: another authentication Response
```
````

## Usage

Install it with pip:

```
pip install pandoc-plantuml-latex
```

And use it like any other pandoc filter:

```
pandoc tests/sample.md -o sample.pdf --filter pandoc-plantuml
```

The PlantUML binary must be in your `$PATH` or can be set with the
`PLANTUML_BIN` environment variable.

### Additional parameters

You could pass additional parameters into `plantuml` filter which will be processed as picture's options:

````
```{ .plantuml height=50% plantuml-filename=test.png }
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
```
````

The `plantuml-filename` parameter create a symlink for the destination picture, which could be used in the same file as an image directly.

## But there is ...

- merged pull request [Raw latex support](https://github.com/timofurrer/pandoc-plantuml-filter/pull/4)  
  see [tests/](tests/)

- also generate vector images for latex `beamer` template

- added debugging environment variable `DEBUG=1`
