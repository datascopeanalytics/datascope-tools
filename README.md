`datascope-tools` might eventually consist of a collection of scripts,
tools, and ideas that we have collected over the years at
[Datascope Analytics](http://datascopeanalytics.com) that help with
our work. This is somewhat inspired by
[bit.ly's data_hacks](https://github.com/bitly/data_hacks)

Scripts
=======

* `pair-with`: simple script to manipulate `.hg/hgrc` files when
  pairing with other people

* `decrapify`: simple script to remove junk files that commonly occur when
  we're writing code or experimenting with scripts

Functions
=========

* `decorators.cache`: While developing scrapers, code that interacts
  with APIs, and other functions that take a little while to run, I
  find myself often wanting to cache the results of calls to functions
  for a little while during development, like this.

	```python
	from datascope_tools import decorators

	@decorators.cache(expire_after=30*60)
	def v_important():
		time.sleep(42)
		return 'vnice'
	```
