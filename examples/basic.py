
# =========================================
#       IMPORTS
# --------------------------------------

import rootpath

rootpath.append()


# =========================================
#       EXAMPLE
# --------------------------------------

from envjoy import env

# non-casted access - never throws annoying errors

env.FOO
env.FOO = 1
del env.FOO
env.FOO = 1

# casted access - never throws annoying errors

del env['FOO']

env['FOO'] # => None
env['FOO'] = 1 # set value without complaints (casted to string)
env['FOO'] # => "1"
env['FOO'] # => 1

env['FOO'] = None
env['FOO'] # => ''
env['FOO', bool] # => False
env['FOO', int] # => 0
env['FOO', float] # => 0.0
env['FOO', str] # => ''
env['FOO', tuple] # => ()
env['FOO', list] # => []
env['FOO', dict] # => {}

env['FOO'] = True
env['FOO'] # => 'True'
env['FOO', bool] # => True
env['FOO', int] # => 1
env['FOO', float] # => 1.0
env['FOO', str] # => 'true'
env['FOO', tuple] # => (True)
env['FOO', list] # => [True]
env['FOO', dict] # => {}

env['FOO'] = 'true' # => 'true'
env['FOO', bool] # => True
env['FOO', int] # => 1
env['FOO', float] # => 1.0
env['FOO', str] # => 'true'
env['FOO', tuple] # => (True)
env['FOO', list] # => [True]
env['FOO', dict] # => {}

env['FOO'] = 0
env['FOO'] # => '0'
env['FOO', bool] # => False
env['FOO', int] # => 0
env['FOO', float] # => 0.0
env['FOO', str] # => '0'
env['FOO', tuple] # => (0)
env['FOO', list] # => [0]
env['FOO', dict] # => {}

env['FOO'] = '0'
env['FOO'] # => '0'
env['FOO', bool] # => False
env['FOO', int] # => 0
env['FOO', float] # => 0.0
env['FOO', str] # => '0'
env['FOO', tuple] # => (0)
env['FOO', list] # => [0]
env['FOO', dict] # => {}

env['FOO'] = 1
env['FOO'] # => '1'
env['FOO', bool] # => True
env['FOO', int] # => 1
env['FOO', float] # => 1.0
env['FOO', str] # => '1'
env['FOO', tuple] # => (1)
env['FOO', list] # => [1]
env['FOO', dict] # => {}

env['FOO'] = '1'
env['FOO'] # => '1'
env['FOO', bool] # => True
env['FOO', int] # => 1
env['FOO', float] # => 1.0
env['FOO', str] # => '1'
env['FOO', tuple] # => (1)
env['FOO', list] # => [1]
env['FOO', dict] # => {}

env['FOO'] = -1
env['FOO'] # => '-1'
env['FOO', bool] # => True
env['FOO', int] # => -1
env['FOO', float] # => -1.0
env['FOO', str] # => '-1'
env['FOO', tuple] # => (-1)
env['FOO', list] # => [1]
env['FOO', dict] # => {}

env['FOO'] = '-1'
env['FOO'] # => '-1'
env['FOO', bool] # => True
env['FOO', int] # => -1
env['FOO', float] # => -1.0
env['FOO', str] # => '-1'
env['FOO', tuple] # => (-1)
env['FOO', list] # => [1]
env['FOO', dict] # => {}

env['FOO'] = 12.34
env['FOO'] # => '12.34'
env['FOO', bool] # => True
env['FOO', int] # => 12
env['FOO', float] # => 12.34
env['FOO', str] # => '12.34'
env['FOO', tuple] # => (12.34)
env['FOO', list] # => [12.34]
env['FOO', dict] # => {}

env['FOO'] = '12.34'
env['FOO'] # => '12.34'
env['FOO', bool] # => True
env['FOO', int] # => 12
env['FOO', float] # => 12.34
env['FOO', str] # => '12.34'
env['FOO', tuple] # => (12.34)
env['FOO', list] # => [12.34]
env['FOO', dict] # => {}

env['FOO'] = -12.34
env['FOO'] # => '-12.34'
env['FOO', bool] # => True
env['FOO', int] # => -12
env['FOO', float] # => -12.34
env['FOO', str] # => '-12.34'
env['FOO', tuple] # => (-12.34)
env['FOO', list] # => [-12.34]
env['FOO', dict] # => {}

env['FOO'] = -'12.34'
env['FOO'] # => '-12.34'
env['FOO', bool] # => True
env['FOO', int] # => -12
env['FOO', float] # => -12.34
env['FOO', str] # => '-12.34'
env['FOO', tuple] # => (-12.34)
env['FOO', list] # => [-12.34]
env['FOO', dict] # => {}

env['FOO'] = 'foo bar baz 1 2 3'
env['FOO'] # => 'foo bar baz 1 2 3'
env['FOO', bool] # => True
env['FOO', int] # => 123
env['FOO', float] # => 123.0
env['FOO', str] # => 'foo bar baz 1 2 3'
env['FOO', tuple] # => ('foo bar baz 1 2 3')
env['FOO', list] # => ['foo bar baz 1 2 3']
env['FOO', dict] # => {}

env['FOO'] = 'foo,bar,baz,1,2,3'
env['FOO'] # => 'foo,bar,baz,1,2,3'
env['FOO', bool] # => True
env['FOO', int] # => 123
env['FOO', float] # => 123.0
env['FOO', str] # => 'foo,bar,baz,1,2,3'
env['FOO', tuple] # => ('foo', 'bar', 'baz')
env['FOO', list] # => ['foo', 'bar', 'baz']
env['FOO', dict] # => {0: 'foo', 1: 'bar', 2: 'baz'}

env['FOO'] = '(foo,bar,baz,1,2,3)'
env['FOO'] # => 'foo,bar,baz,1,2,3'
env['FOO', bool] # => True
env['FOO', int] # => 123
env['FOO', float] # => 123.0
env['FOO', str] # => 'foo,bar,baz,1,2,3'
env['FOO', tuple] # => ('foo', 'bar', 'baz')
env['FOO', list] # => ['foo', 'bar', 'baz']
env['FOO', dict] # => {0: 'foo', 1: 'bar', 2: 'baz'}

env['FOO'] = '[foo,bar,baz,1,2,3]'
env['FOO'] # => 'foo,bar,baz,1,2,3'
env['FOO', bool] # => True
env['FOO', int] # => 123
env['FOO', float] # => 123.0
env['FOO', str] # => 'foo,bar,baz,1,2,3'
env['FOO', tuple] # => ('foo', 'bar', 'baz')
env['FOO', list] # => ['foo', 'bar', 'baz']
env['FOO', dict] # => {0: 'foo', 1: 'bar', 2: 'baz'}

env['FOO'] = ('foo', 'bar', 'baz', 1, 2, 3)
env['FOO'] # => '(foo,bar,baz,1,2,3)'
env['FOO', bool] # => True
env['FOO', int] # => 123
env['FOO', float] # => 123.0
env['FOO', str] # => '(foo,bar,baz,1,2,3)'
env['FOO', tuple] # => ('foo', 'bar', 'baz')
env['FOO', list] # => ['foo', 'bar', 'baz']
env['FOO', dict] # => {0: 'foo', 1: 'bar', 2: 'baz'}

env['FOO'] = ['foo', 'bar', 'baz', 1, 2, 3]
env['FOO'] # => '[foo,bar,baz,1,2,3]'
env['FOO', bool] # => True
env['FOO', int] # => 123
env['FOO', float] # => 123.0
env['FOO', str] # => '[foo,bar,baz,1,2,3]'
env['FOO', tuple] # => ('foo', 'bar', 'baz')
env['FOO', list] # => ['foo', 'bar', 'baz']
env['FOO', dict] # => {0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3}

env['FOO'] = {'foo': 1, 'bar': 2, 'baz': 3}
# env['FOO'] # => 'foo:1,bar:2,baz:3' # REVIEW: handle nested json
env['FOO'] # => '{foo:1,bar:2,baz:3}' # REVIEW: handle nested json
env['FOO', bool] # => True
env['FOO', int] # => 123
env['FOO', float] # => 123.0
env['FOO', str] # => '{foo:1,bar:2,baz:3}'
env['FOO', tuple] # => ({0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3})
env['FOO', list] # => [{0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3}]
env['FOO', dict] # => {0: 'foo', 1: 'bar', 2: 'baz', 3: 1, 4: 2, 5: 3}

env['FOO'] = {'foo': {'bar': {'baz': True}}}
env['FOO'] # => '' # REVIEW: handle nested json
env['FOO', bool] # => True
env['FOO', int] # => 0
env['FOO', float] # => 0.0
env['FOO', str] # => TODO
env['FOO', tuple] # => TODO
env['FOO', list] # => TODO
env['FOO', dict] # => TODO

env.inspect()
env.print()
