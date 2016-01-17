# Copyright 2009 Simon Schampijer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""HelloWorld Activity: A case study for developing an activity."""

import logging
import os
from gettext import gettext as _

from gi.repository import Gtk

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton


class HelloWorldActivity(activity.Activity):
    """HelloWorldActivity class as specified in activity.info"""

    angle = 0

    def __init__(self, handle):
        if os.path.exists('/tmp/1'):
            os.remove('/tmp/1')
            """Set up the HelloWorld activity."""
            activity.Activity.__init__(self, handle)

        if os.path.exists('/tmp/2'):
            os.remove('/tmp/2')
            # we do not have collaboration features
            # make the share option insensitive
            self.max_participants = 1

            # toolbar with the new toolbar redesign
            toolbar_box = ToolbarBox()

            activity_button = ActivityButton(self)
            toolbar_box.toolbar.insert(activity_button, 0)
            activity_button.show()

            title_entry = TitleEntry(self)
            #toolbar_box.toolbar.insert(title_entry, -1)
            toolbar_box.toolbar.insert(title_entry, -1)
            title_entry.show()

            share_button = ShareButton(self)
            toolbar_box.toolbar.insert(share_button, -1)
            share_button.show()

            ##keep_button = KeepButton(self)
            ##toolbar_box.toolbar.insert(keep_button, -1)
            ##keep_button.show()

            separator = Gtk.SeparatorToolItem()
            separator.props.draw = False
            separator.set_expand(True)
            toolbar_box.toolbar.insert(separator, -1)
            separator.show()

            stop_button = StopButton(self)
            toolbar_box.toolbar.insert(stop_button, -1)
            stop_button.show()

            self.set_toolbar_box(toolbar_box)
            toolbar_box.show()
            self.container_vbox = Gtk.VBox()
            self.container_vbox.show()
            self.set_canvas(self.container_vbox)

        if os.path.exists('/tmp/3'):
            os.remove('/tmp/3')   
            self.label = Gtk.Label(_("Hello World!"))
            self.container_vbox.add(self.label)
            self.label.set_angle(self.angle)
            self.label.show()    

        if os.path.exists('/tmp/4'):
            os.remove('/tmp/4')      
            self.button = Gtk.Button("Rotate")
            self.container_vbox.add(self.button)
            self.button.connect('clicked', self.hello, None)
            self.button.show()

    def hello(self, sender, data=None):
        # label with the text, make the string translatable

        self.container_vbox.remove(self.label)
        self.angle = self.angle + 30
        self.label.set_text("Hello World!")
        self.container_vbox.add(self.label)
        self.label.set_angle(self.angle)
        self.label.show()

        self.container_vbox.remove(self.button)
        self.button = Gtk.Button("Rotate")
        self.container_vbox.add(self.button)
        self.button.connect('clicked', self.hello, None)
        self.button.show()

