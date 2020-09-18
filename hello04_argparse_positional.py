#!/usr/bin/env python3
# Purpose: Say hello

# p. 23 in book
# make sure to import argparse
import argparse

# POSITION - does NOT run from the command line

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
