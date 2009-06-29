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
GUI-specific interface functions for Google Chrome on Microsoft Windows.
"""

__revision__ = "$Rev: 3053 $"
__date__ = "$Date: 2008-09-03 02:32:38 -0500 (Wed, 03 Sep 2008) $"
__author__ = "$Author: johann $"

import os
import time
import win32gui
import win32con
from win32com.shell import shellcon
from win32com.shell import shell
from shotfactory04.gui import windows


class Gui(windows.Gui):
    """
    Special functions for Chrome on Windows.
    """

    def reset_browser(self):
        """
        Delete previous session and browser cache.
        """
        appdata = shell.SHGetFolderPath(0, shellcon.CSIDL_LOCAL_APPDATA, 0, 0)
        self.delete_if_exists(os.path.join(
            appdata, 'Google', 'Chrome', 'User Data', '*'))

    def start_browser(self, config, url, options):
        """
        Start browser and load website.
        """
        command = config['command']
        if not command:
            appdata = shell.SHGetFolderPath(0, shellcon.CSIDL_LOCAL_APPDATA, 0, 0)
            command = appdata + '\Google\Chrome\Application\chrome.exe'
        print 'running', command
        try:
            import subprocess
        except ImportError:
            os.spawnl(os.P_DETACH, command, os.path.basename(command), url)
        else:
            subprocess.Popen([command, url])
        print "Sleeping %d seconds while page is loading." % options.wait
        time.sleep(options.wait - 10)
        self.maximize()
        time.sleep(10)

    def maximize(self):
        """Maximize the browser window."""
        window = self.find_maximizable()
        if window:
             win32gui.PostMessage(window,
                 win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE)

    def find_maximizable(self):
        """Find window to maximize."""
        return self.find_window_by_classname('Chrome_XPFrame')
        # return self.find_window_by_title_suffix('Google Chrome')

    def find_scrollable(self):
        """Find scrollable window."""
        return win32gui.WindowFromPoint((self.width/2, self.height/2))


# Test browser interface from command line                                              
if __name__ == '__main__':
    config = {
        'width': 1024,
        'height': 768,
        'bpp': 24,
        'request': 123,
        }

    class Options:
        verbose = 3
        max_pages = 7

    gui = Gui(config, Options())
    gui.maximize()
