#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#    Copyright (C) 2022  Marcus Rickert
#
#    See https://github.com/marcus67/python_base_app_ldap_extension
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest

from python_base_app import log_handling
from python_base_app.test import base_test
from python_base_app_ldap_extension.test.test_git import TestGit
from python_base_app_ldap_extension.test.test_ldap_user_handler import TestLdapUserHandler
from python_base_app_ldap_extension.test.test_settings import TestSettings


def add_test_cases(p_test_suite, p_config_filename=None):
    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=TestLdapUserHandler, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=TestGit, p_config_filename=p_config_filename)

    base_test.add_tests_in_test_unit(
        p_test_suite=p_test_suite,
        p_test_unit_class=TestSettings, p_config_filename=p_config_filename)


def main():
    log_handling.start_logging(p_use_filter=False)
    test_suite = unittest.TestSuite()
    add_test_cases(p_test_suite=test_suite, p_config_filename=base_test.get_config_filename())
    base_test.run_test_suite(p_test_suite=test_suite)


if __name__ == '__main__':
    main()
