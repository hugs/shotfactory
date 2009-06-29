# browsershots.org - Test your web design in different browsers
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
#
# Browsershots is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Browsershots is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
GUI-specific interface functions for X11.
"""

__revision__ = "$Rev: 2747 $"
__date__ = "$Date: 2008-04-08 09:39:48 -0500 (Tue, 08 Apr 2008) $"
__author__ = "$Author: hawk $"


import os
import time
from shotfactory04.gui import linux as base


class Gui(base.Gui):
    """
    Special functions for SeaMonkey.
    """

    def reset_browser(self):
        """
        Delete crash dialog and browser cache.
        """
        home = os.environ['HOME']
	for profile_folder in ('.mozilla', '.mozilla.org'):
            for profile_name in ('default', 'seamonkey*'):
                self.delete_if_exists(os.path.join(
                    home, profile_folder, profile_name, 'Cache'))
                self.delete_if_exists(os.path.join(
                    home, profile_folder, profile_name, '*', 'Cache'))
                self.delete_if_exists(os.path.join(
                    home, profile_folder, profile_name, '*', 'history.dat'))
                self.delete_if_exists(os.path.join(
                    home, profile_folder, profile_name, '*', 'cookies.txt'))
                self.delete_if_exists(os.path.join(
                    home, profile_folder, profile_name, 'Crash Reports'))
                self.delete_if_exists(os.path.join(
                    home, profile_folder, profile_name, '*', 'minidumps'))

    def reuse_browser(self, config, url, options):
        """
        Open a new URL in the same browser window.
        """
        command = config['command'] or config['browser'].lower()
        command = '%s -remote "OpenURL(%s,new-tab)"' % (command, url)
        print "Running", command
        error = self.shell(command)
        if error:
            raise RuntimeError("could not load new URL in the browser")
        print "Sleeping %d seconds while page is loading." % (
            options.reuse_wait)
        time.sleep(options.reuse_wait / 2.0)
        self.maximize()
        time.sleep(options.reuse_wait / 2.0)
