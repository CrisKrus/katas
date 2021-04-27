#!/bin/sh

find . -name '*.py' | entr python -m unittest
