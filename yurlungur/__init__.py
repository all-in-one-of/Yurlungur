# -*- coding: utf-8 -*-
import sys

assert sys.version_info > (2, 7), ('yurlungur currently requires Python 2.7 later')
sys.dont_write_bytecode = True

__all__ = []
__version__ = "0.9.6"

from yurlungur.core import *  # noQA
from yurlungur.tool import meta, ui
from yurlungur.tool.standalone import *  # noQA

# info
name = __name__
version = __version__

del sys
