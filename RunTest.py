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
from typing import List
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
            self.__getTestModules([folder], os.path.dirname(__file__))
            for root, subDirs, _unused_files in os.walk(os.path.join(os.path.dirname(__file__), folder)):
                self.__getTestModules(subDirs, root)


    def __getTestModules(self, folders: List[str], parent: str) -> None:
        if folders and len(folders) > 0:
            shortListedFolders = [os.path.join(parent, dir) for dir in folders if not dir.startswith('__')]

            for folder in shortListedFolders:
                sys.path.append(folder)

                for (_unsed_finder, module_name, isPkg) in iter_modules([folder]):
                    if not isPkg:
                        # import the module and iterate through its attributes
                        module = import_module(f"{module_name}")
                        attributes = [attribute for attribute in dir(module) if attribute.startswith('Test') and isclass(getattr(module, attribute)) and attribute != 'TestCase']
                        for attributeName in attributes:
                            attribute = getattr(module, attributeName)
                            if issubclass(attribute, TestCase):
                                logger.debug('Adding test class {}'.format(attribute))
                                self.suit.addTests(TestLoader().loadTestsFromTestCase(attribute))


def parseArgs():
    argParser = ArgumentParser(description='Running tests', formatter_class=ArgumentDefaultsHelpFormatter)
    argParser.add_argument('--verbose', action='store_true', help='Add verbose logging')
    knownArgs, _unusedUnknownArgs = argParser.parse_known_args()
    return knownArgs


if __name__ == "__main__":
    args = parseArgs()
    testRunnerVerbosity=2
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        testRunnerVerbosity=3
        
    logger.debug('Running Tests...')
    testRunner = TextTestRunner(verbosity=testRunnerVerbosity)
    result = testRunner.run(RunTests().suit)    
    sys.exit(len(result.failures))
