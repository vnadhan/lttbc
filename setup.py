import os.path as osp
import sys

import numpy as np
from setuptools import Extension, setup


def get_script_path():
    return osp.dirname(osp.realpath(sys.argv[0]))


def read(*parts):
    return open(osp.join(get_script_path(), *parts)).read()


setup_args = dict(
    ext_modules=[
        Extension(
            "lttbc",
            sources=["lttbc.c"],
            define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
            include_dirs=[np.get_include(), get_script_path()],
        )
    ]
)
setup(**setup_args)
