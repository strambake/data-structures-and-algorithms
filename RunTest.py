"""
Test Runner class

@Author Swapni Trambake, trambake.swapnil@gmail.com
"""

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
import sys
from importlib import import_module
from inspect import isclass
import logging
from pkgutil import iter_modules
from unittest import TextTestRunner, TestCase, TestLoader
from unittest.suite import TestSuite

sys.path.append(os.path.dirname(__file__))
from utility.LogHelper import logger

testFolders = ['problems']

class RunTests():
    def __init__(self, testFolders=None) -> None:
        self.suit = TestSuite()
        self.__getAllTestModules()


    def __getAllTestModules(self):
        for folder in testFolders:
            sys.path.append(os.path.join(os.path.dirname(__file__), folder))

        for (_, module_name, _) in iter_modules(testFolders):
            # import the module and iterate through its attributes
            module = import_module(f"{module_name}")
            attributes = [attribute for attribute in dir(module) if attribute.startswith('Test') and isclass(getattr(module, attribute)) and attribute != 'TestCase']
            for attributeName in attributes:
                attribute = getattr(module, attributeName)
                if issubclass(attribute, TestCase):
                    self.suit.addTests(TestLoader().loadTestsFromTestCase(attribute))


def parseArgs():
    argParser = ArgumentParser(description='Running tests', formatter_class=ArgumentDefaultsHelpFormatter)
    argParser.add_argument('--verbose', action='store_true', help='Add verbose logging')
    knownArgs, _unusedUnknownArgs = argParser.parse_known_args()
    return knownArgs


if __name__ == "__main__":
    args = parseArgs()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        
    logger.debug('Running Tests...')
    testRunner = TextTestRunner(verbosity=2)
    testRunner.run(RunTests().suit)
