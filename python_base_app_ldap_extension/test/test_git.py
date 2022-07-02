#    Copyright (C) 2019-2022  Marcus Rickert
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

from python_base_app.test import base_test
from python_base_app_ldap_extension import git


class TestGit(base_test.BaseTestCase):

    def test_git(self):
        self.assertIsNotNone(git.git_metadata)
        self.assertIn("commit_id", git.git_metadata)
        self.assertIn("branch", git.git_metadata)
        self.assertIn("author_name", git.git_metadata)
        self.assertIn("author_email", git.git_metadata)
