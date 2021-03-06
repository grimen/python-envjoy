
# `envjoy` [![PyPI version](https://badge.fury.io/py/envjoy.svg)](https://badge.fury.io/py/envjoy) [![Build Status](https://travis-ci.com/grimen/python-envjoy.svg?branch=master)](https://travis-ci.com/grimen/python-envjoy) [![Coverage Status](https://codecov.io/gh/grimen/python-envjoy/branch/master/graph/badge.svg)](https://codecov.io/gh/grimen/python-envjoy)

*A more enjoyable environment variable getter and setter - for Python.*

## Introduction

Environment variable getting and setting has a bit of an itch to it. This is a not-so-whiny library that makes it more easy to get and set environment variables, and optionally smarter data type interpretation.


## Install

Install using **pip**:

```sh
$ pip install envjoy
```


## Use

Very basic **[example](https://github.com/grimen/python-envjoy/tree/master/examples/basic.py)**:

```python
from __future__ import print_function # Optional: Python 2 support for `env.print`

from envjoy import env

# non-casted access - never throws annoying errors

print(env.FOO)

env.FOO = 1

print(env.FOO)

del env.FOO

print(env.FOO)

# casted access - never throws annoying errors

del env['FOO']

print('---')

print(env['FOO']) # => None

env['FOO']= 1 # set value without complaints (casted to string)

print(env['FOO']) # => "1"
print(env['FOO']) # => 1

print('---')

env['FOO'] = None

print(env['FOO']) # => ''
print(env['FOO', bool]) # => False
print(env['FOO', int]) # => 0
print(env['FOO', float]) # => 0.0
print(env['FOO', str]) # => ''
print(env['FOO', tuple]) # => ()
print(env['FOO', list]) # => []
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = True

print(env['FOO']) # => 'True'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 1
print(env['FOO', float]) # => 1.0
print(env['FOO', str]) # => 'true'
print(env['FOO', tuple]) # => (True)
print(env['FOO', list]) # => [True]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = 'true' # => 'true'

print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 1
print(env['FOO', float]) # => 1.0
print(env['FOO', str]) # => 'true'
print(env['FOO', tuple]) # => (True)
print(env['FOO', list]) # => [True]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = 0

print(env['FOO']) # => '0'
print(env['FOO', bool]) # => False
print(env['FOO', int]) # => 0
print(env['FOO', float]) # => 0.0
print(env['FOO', str]) # => '0'
print(env['FOO', tuple]) # => (0)
print(env['FOO', list]) # => [0]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = '0'

print(env['FOO']) # => '0'
print(env['FOO', bool]) # => False
print(env['FOO', int]) # => 0
print(env['FOO', float]) # => 0.0
print(env['FOO', str]) # => '0'
print(env['FOO', tuple]) # => (0)
print(env['FOO', list]) # => [0]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = 1

print(env['FOO']) # => '1'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 1
print(env['FOO', float]) # => 1.0
print(env['FOO', str]) # => '1'
print(env['FOO', tuple]) # => (1)
print(env['FOO', list]) # => [1]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = '1'

print(env['FOO']) # => '1'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 1
print(env['FOO', float]) # => 1.0
print(env['FOO', str]) # => '1'
print(env['FOO', tuple]) # => (1)
print(env['FOO', list]) # => [1]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = -1

print(env['FOO']) # => '-1'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => -1
print(env['FOO', float]) # => -1.0
print(env['FOO', str]) # => '-1'
print(env['FOO', tuple]) # => (-1)
print(env['FOO', list]) # => [1]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = '-1'

print(env['FOO']) # => '-1'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => -1
print(env['FOO', float]) # => -1.0
print(env['FOO', str]) # => '-1'
print(env['FOO', tuple]) # => (-1)
print(env['FOO', list]) # => [1]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = 12.34

print(env['FOO']) # => '12.34'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 12
print(env['FOO', float]) # => 12.34
print(env['FOO', str]) # => '12.34'
print(env['FOO', tuple]) # => (12.34)
print(env['FOO', list]) # => [12.34]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = '12.34'

print(env['FOO']) # => '12.34'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 12
print(env['FOO', float]) # => 12.34
print(env['FOO', str]) # => '12.34'
print(env['FOO', tuple]) # => (12.34)
print(env['FOO', list]) # => [12.34]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = -12.34

print(env['FOO']) # => '-12.34'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => -12
print(env['FOO', float]) # => -12.34
print(env['FOO', str]) # => '-12.34'
print(env['FOO', tuple]) # => (-12.34)
print(env['FOO', list]) # => [-12.34]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = '-12.34'

print(env['FOO']) # => '-12.34'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => -12
print(env['FOO', float]) # => -12.34
print(env['FOO', str]) # => '-12.34'
print(env['FOO', tuple]) # => (-12.34)
print(env['FOO', list]) # => [-12.34]
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = 'foo bar baz 1 2 3'

print(env['FOO']) # => 'foo bar baz 1 2 3'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 123
print(env['FOO', float]) # => 123.0
print(env['FOO', str]) # => 'foo bar baz 1 2 3'
print(env['FOO', tuple]) # => ('foo bar baz 1 2 3')
print(env['FOO', list]) # => ['foo bar baz 1 2 3']
print(env['FOO', dict]) # => {}

print('---')

env['FOO'] = 'foo,bar,baz,1,2,3'

print(env['FOO']) # => 'foo,bar,baz,1,2,3'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 123
print(env['FOO', float]) # => 123.0
print(env['FOO', str]) # => 'foo,bar,baz,1,2,3'
print(env['FOO', tuple]) # => ('foo', 'bar', 'baz')
print(env['FOO', list]) # => ['foo', 'bar', 'baz']
print(env['FOO', dict]) # => {0: 'foo', 1: 'bar', 2: 'baz'}

print('---')

env['FOO'] = ('foo', 'bar', 'baz', 1, 2, 3)

print(env['FOO']) # => '(foo,bar,baz,1,2,3)'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 123
print(env['FOO', float]) # => 123.0
print(env['FOO', str]) # => '(foo,bar,baz,1,2,3)'
print(env['FOO', tuple]) # => ('foo', 'bar', 'baz')
print(env['FOO', list]) # => ['foo', 'bar', 'baz', 1, 2, 3]
print(env['FOO', dict]) # => {} # TODO:  {0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3}

print('---')

env['FOO'] = ['foo', 'bar', 'baz', 1, 2, 3]

print(env['FOO']) # => '[foo,bar,baz,1,2,3]'
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 123
print(env['FOO', float]) # => 123.0
print(env['FOO', str]) # => '[foo, bar, baz, 1, 2, 3]'
print(env['FOO', tuple]) # => ('foo', 'bar', 'baz', 1, 2, 3)
print(env['FOO', list]) # => ['foo', 'bar', 'baz', 1, 2, 3]
print(env['FOO', dict]) # => {} # TODO:  {0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3}

print('---')

env['FOO'] = {'foo': 1, 'bar': 2, 'baz': 3}

print(env['FOO']) # => '{foo:1,bar:2,baz:3}' # REVIEW: handle nested json
print(env['FOO', bool]) # => True
print(env['FOO', int]) # => 123
print(env['FOO', float]) # => 123.0
print(env['FOO', str]) # => '{foo: 1, bar: 2, baz: 3}'
print(env['FOO', tuple]) # => ({0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3})
print(env['FOO', list]) # => [{0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3}]
print(env['FOO', dict]) # => {'foo': 1, 'bar': 2, 'baz': 3}

# etc.

print('---')

env.inspect()

print('---')

env.print()

print('---')
```


## Test

Clone down source code:

```sh
$ make install
```

Run **colorful tests**, with only native environment (dependency sandboxing up to you):

```sh
$ make test
```

Run **less colorful tests**, with **multi-environment** (using **tox**):

```sh
$ make test-tox
```


## About

This project was mainly initiated - in lack of solid existing alternatives - to be used at our work at **[Markable.ai](https://markable.ai)** to have common code conventions between various programming environments where **Python** (research, CV, AI) is heavily used.


## License

Released under the MIT license.
