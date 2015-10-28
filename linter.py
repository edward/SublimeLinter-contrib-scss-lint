#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Edward Ocampo-Gooding
# Copyright (c) 2015 Edward Ocampo-Gooding
#
# License: MIT
#

"""This module exports the ScssLint plugin class."""

from SublimeLinter.lint import Linter, util


class ScssLint(Linter):

    """Provides an interface to scss-lint."""

    syntax = ('css', 'sass', 'scss')
    cmd = 'bundle exec scss-lint'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.42.2'
    regex = r'^.+?:(?P<line>\d+) (?:(?P<error>\[E\])|(?P<warning>\[W\])) (?P<message>[^`]*(?:`(?P<near>.+?)`)?.*)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'scss'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = ('include-linter', 'exclude-linter')
    comment_re = r'^\s*/[/\*]'
    config_file = ('--config', '.scss-lint.yml', '~')

