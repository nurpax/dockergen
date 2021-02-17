
import sys
from dockergen import Gen

from typing import List

g = Gen()
g.from_('nvidia/cuda:11.1-devel-ubuntu20.04', platform='linux/amd64')
g.label(maintainer='Example User <foo@example.com>')
g.run(['apt-get update -yq', 'apt-get install wget gcc'])
g.write(sys.stdout)
