#!/usr/bin/env python
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
Find vertical offset between two PPM files.
"""

__revision__ = "$Rev: 2006 $"
__date__ = "$Date: 2007-08-19 19:32:52 -0500 (Sun, 19 Aug 2007) $"
__author__ = "$Author: johann $"

import sys
from shotfactory04.image import hashmatch

arg0, filename1, filename2 = sys.argv
print hashmatch.find_offset(filename1, filename2)
