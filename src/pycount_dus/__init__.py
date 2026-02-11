# read version from installed package
from importlib.metadata import version
__version__ = version(__name__)

# populate package namespace
from pycount_dus.pycount_dus import count_words
from pycount_dus.plotting import plot_words