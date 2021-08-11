from pylint.lint import Run
import os


class RunPyLint():
    def __init__(self) -> None:
        pass

    def run(self, dirs):
        commandLineArgs = []
        commandLineArgs.append('--rcfile={}'.format(os.path.join(os.path.dirname(__file__), 'pylint.rc')))
        commandLineArgs.append('--output-format=parseable')
        for dir in dirs:
            fullDirPath = os.path.join(os.path.dirname(__file__), "..", dir)
            if os.path.isdir(fullDirPath):
                for root, dirs, files in os.walk(fullDirPath, topdown=True):
                    if any(file.endswith(".py") for file in files):
                        for dir in dirs:
                            commandLineArgs.append(os.path.join(root, dir))
            else:
                print('Ignoring {} directory'.format(dir))

        # Execute PyLint
        Run(commandLineArgs)


if __name__ == "__main__":
    dirs = ['data_structures']
    RunPyLint().run(dirs)