import os

from lxml import etree

from resources.sbtabpy import modelSystem

compiler = modelSystem()
compiler.load_folder("resources","tsv")