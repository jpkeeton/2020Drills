# shebang line tellse OS which program to use to execute the program
#!/usr/bin/env python3

# add a comment calling out the purpose fo the program
# Purpose: Say hello

# p. 23 in book
# make sure to import argparse
import argparse

# POSITION - does NOT run from the PyCharm

# parser = argparse.ArgumentParser(description='Say hello')
parser = argparse.ArgumentParser(description='You should really say hello now')
# so when you run '-h' flag you get the positional arguments 'name' and 'name to greet'
# parser.add_argument('name', help='Name to greet')
parser.add_argument('help me!', help='this is some help')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
