adj-cli-python: Generates a random order of values in the given range
=======================================

![env](/badges/env.svg)
![platform](/badges/platform.svg)

What is adj-cli-python?
-------------
This is a cli(adjust-sequence-shuffler) that generates the numbers from 1 to 10 in a random sequence everytime.
This uses the combination of LCG and Fisher-yates algorithm to generate a random number and shuffle the sequence.
We can generate a random shuffles sequence for a custom limit as well, Please check the [usage](#usage) column
to know more.


Requirements
------------

You need Python 3.5 or later to run adjust-sequence-shuffler.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, macOS and Windows, packages are available at

  https://www.python.org/getit/


Quick start
-----------

**Supported Env:**

- Linux
- MacOs

## Linux  & MacOs

The Installation can be done using the below ways for Linux and MacOs

### 1. Direct installation

Git Clone the repository --> https://github.com/vakees14/adj-cli-python
```
$ git clone https://github.com/vakees14/adj-cli-python
$ cd adj-cli-python/
```

Use the below command to copy it into the /usr/local/bin to use it as a CLI
```
# mv adjust-sequence-shuffler.py /usr/local/bin/adjust-sequence-shuffler
```

### 2. Install using the binary in release

Download the package from the Github Relese tab in the repository.
https://github.com/vakees14/adj-cli-python/releases 

Then place it under the below directory

```
/usr/local/bin/adjust-sequence-shuffler
```


Usage
-----

**How to run ?**
```
# adjust-sequence-shuffler
10 1 2 6 9 5 4 3 8 7
# adjust-sequence-shuffler
1 5 6 4 3 2 7 9 8 10
# adjust-sequence-shuffler
8 1 10 9 3 2 7 6 5 4
# adjust-sequence-shuffler
2 1 8 9 10 3 7 6 5 4

$ adjust-sequence-shuffler
8 1 2 10 4 9 7 6 5 3
$ adjust-sequence-shuffler
7 2 9 6 5 8 3 4 1 10
$ adjust-sequence-shuffler
10 1 9 4 7 5 3 6 2 8
$ adjust-sequence-shuffler
1 4 6 2 8 7 3 10 9 5

```
> You get a random shuffled numbers everytime


**What to do if i want to generate sequence for a different limit ?**
```
# adjust-sequence-shuffler --limit 20
1 19 3 2 11 6 18 15 12 20 8 4 7 14 10 5 17 13 9 16
# adjust-sequence-shuffler --limit 20
2 1 20 10 4 8 17 14 16 12 19 18 6 3 15 13 11 9 7 5

$ adjust-sequence-shuffler --limit 15
5 1 2 4 15 7 8 9 10 11 12 13 14 3 6
$ adjust-sequence-shuffler --limit 15
1 2 11 4 7 14 3 6 9 15 5 13 12 10 8
```

**How to know the available options ?**
```
# adjust-sequence-shuffler -h
usage: adjust-sequence-shuffler [-h] [--limit limit] [--version]

By default this will shuffle the sequence till 10. please provide --limit
<value> to shuffle in the customized limit range

optional arguments:
  -h, --help     show this help message and exit
  --limit limit  The limit for the random numbers to be generated
  --version      show program's version number and exit

Enjoy the CLI Adjust Team!
```

**How to find the version of the adjust-sequence-shuffler you use ?**
```
# adjust-sequence-shuffler --version
adjust-sequence-shuffler 1.0.0
```



## Versioning

Released Verion --> 1.0.0

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/vakees14/adj-cli-python/tags). 

## Authors

* [**VAKEES**](https://github.com/vakees14)

See also the list of [contributors](https://github.com/vakees14/adj-cli-python/graphs/contributors) who participated in this project.
