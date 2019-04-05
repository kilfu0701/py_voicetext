#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension

py_voicetext_module = Extension(
    '_py_voicetext',
    sources=[
        'py_voicetext.i',
    ],
    extra_link_args=['/usr/vt/hikari/D44/bin/libvt_jpn.so'],
    #extra_compile_args=[''],
)

setup(
    name = 'py_voicetext',
    version = '0.1',
    author      = "kilfu0701",
    description = """A Wrapper library for voicetext.""",
    ext_modules = [py_voicetext_module],
    py_modules = ["py_voicetext"],
)
