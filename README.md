# Pyckle (Incomplete, Not Functioning)

Boring static website generator.

## Tags

Include `@tag: text` in markdown files and `{{ tag }}` in layout files (where "tag" can be whatever you want).

The text from each `@tag` will be inserted into `{{ tag }}` in the layout template.
Layouts are specified with the `@layout` tag in markdown files.
Where the content appears is specified with the `{{ content }}` tag in layout files.

### User-defined tags

Any line in a markdown file that begins with `@` and includes a `:` should be accepted as a tag.

### Inferred tags

Some tags are inferred and can be included in templates without being specified in the markdown file.

* `{{ title }}` is the string of text after the first row of any number of `#`'s
* `{{ path }}` is a hyperlinked path string for the current page
* `{{ url }}` is the URL of the current page
* `{{ gen-date }}` is the date that the generator was run in the format `YYYY-MM-DD`

## To do

* Actually get the script working.
* `{{ index }}` tag for listing all page links below a certain directory
* `{{ grab: x y from /path/to/file.html }}` tag for grabbing certain lines of other files

## The name

[Dr. Pyckle and Mr. Pryde](https://en.wikipedia.org/wiki/Dr._Pyckle_and_Mr._Pryde) is a spoof of Dr. Jekyll and Mr. Hyde. [Jekyll](https://jekyllrb.com/) is a static website generator I based Pyckle on. Pyckle is written in Python.
