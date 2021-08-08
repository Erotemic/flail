try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def parse_version(fpath):
    """
    Statically parse the version number from a python file
    """
    import ast
    import os
    if not os.path.exists(fpath):
        raise ValueError('fpath={!r} does not exist'.format(fpath))
    with open(fpath, 'r') as file_:
        sourcecode = file_.read()
    pt = ast.parse(sourcecode)
    class Finished(Exception):
        pass
    class VersionVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            for target in node.targets:
                if getattr(target, 'id', None) == '__version__':
                    self.version = node.value.s
                    raise Finished
    visitor = VersionVisitor()
    try:
        visitor.visit(pt)
    except Finished:
        pass
    return visitor.version

setup(name = "flail",
            description="Flail - The Ball and Chain Decorator",
            long_description = """
Decorators with more injuries
""",
            license="""MIT""",
            version = parse_version('flail/__init__.py'),
            author = "David Beazley",
            author_email = "dave@dabeaz.com",
            maintainer = "David Beazley",
            maintainer_email = "dave@dabeaz.com",
            url = "https://github.com/dabeaz/flail",
            packages = ['flail'],
            classifiers = [
              'Programming Language :: Python :: 3',
              ]
            )
