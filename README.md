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

* `iterators.itergrams`: Iterate over consecutive overalapping tuples
  in an iterable. Doesn't read the entire list into memory so is
  useful for BIG DATA.

  ```python
  from datascope_tools import iterators
  
  data = ['you', 'like-a', 'da', 'juice', 'eh?']
  for ngram in iterators.itergrams(data, n=3):
      print(ngram)

  >> ('you', 'like-a', 'da')
  >> ('like-a', 'da', 'juice')
  >> ('da', 'juice', 'eh?')
  ```

* `iterators.rank_sorted`: A combination of `enumerate` and `sort` iterators that also deals
   with tied ranks. Say there is a game where you get scored and you want to rank people:
 
  ```python
  scores = [
      ('alex', 100),
      ('bo', 100),
      ('brian', 100),
      ('dean', 10),
      ('horatio', 90),
      ('irmak', 100),
      ('jess', 100),
      ('karlota', 90),
      ('melba', 90),
      ('meridith', 100),
      ('michael', 100),
      ('mike', 100),
      ('mollie', 100),
      ('vlad', 100),
  ]
  answer = list(rank_sorted(scores, key=operator.itemgetter(1)))
  >> [
      (1, ('alex', 100)),
      (1, ('bo', 100)),
      ...
      (11, ('horatio', 90)),
      (11, ('karlota', 90)),
      (11, ('melba', 90)),
      (14, ('dean', 10)),
  ]
  ```

Classes
=======

* `mixins.UniqueKey`: Sometimes it's nice to have instances of classes as keys in a dictionary or as members of a set. The UniqueKey mixin sets the `__hash__` and `__eq__` function so that instances will be hashed using a "unique identifier" attribute.

  ```python
  class Snowflake(UniqueKey):
      def __init__(self, snowflake_id):
          self.id = snowflake_id
  
  set([Snowflake('a'), Snowflake('a')])
  >> set([Snowflake('a')])
  ```
  
  
