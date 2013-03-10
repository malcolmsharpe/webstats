import argparse
import re

def parse_listing(path):
  pat = re.compile('<td><a href="([^"]*)">')
  for line in file(path):
    if line.startswith('<tr><td'):
      m = pat.search(line)
      assert m
      yield m.group(1)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('path')
  args = parser.parse_args()

  for line in parse_listing(args.path):
    print line
