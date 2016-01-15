# Copyright (C) 2010 Kandarp Kaushik
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
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

"""DevTutor Activity: A case study for developing an activity."""

import logging
import telepathy

import os
import subprocess

from gettext import gettext as _

from gi.repository import Gtk
from gi.repository import GConf
from gi.repository import Pango

from dbus.service import method, signal
from dbus.gobject_service import ExportedGObject

from sugar3.activity import activity
from sugar3.graphics.alert import Alert
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import *
from sugar3.graphics.toolbutton import ToolButton

from sugar3.presence import presenceservice
from sugar3.presence.tubeconn import TubeConnection

SERVICE = "org.laptop.DevTutor"
IFACE = SERVICE
PATH = "/org/laptop/DevTutor"

from helloworld import HelloWorldActivity
from modules import ShowModules
from AbiWordActivity import *


class DevTutorActivity(activity.Activity):
    """DevTutorActivity class as specified in activity.info"""    

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
             
        self.max_participants = 10

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show() 
            
        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show() 

        self.back_button = BackButton()
        self.back_button.connect('clicked', self.show_options1)
        toolbar_box.toolbar.insert(self.back_button, 0)
        self.back_button.show() 

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()
        
        self.show_options()  
        
        self._logger = logging.getLogger('hellomesh-activity')


        self.hellotube = None  # Shared session
        self.initiating = False

        # get the Presence Service
        self.pservice = presenceservice.get_instance()
        # Buddy object for you
        owner = self.pservice.get_owner()
        self.owner = owner

        self.connect('shared', self._shared_cb)
        self.connect('joined', self._joined_cb)
       

    def show_options1(self, data=None):   
        self.show_options()

    def show_options(self):         
        
        self.main_container = Gtk.VBox()

        self.add_padding()   
        self.line1 = Gtk.HBox()
        
        button1 = Gtk.Button("Show modules")
        #button1.set_size_request(200,80)
        #self.line1.pack_start(button1, False, False, 0)
        self.line1.add(button1)
        button1.connect('clicked', self.show_modules, None)
        button1.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1) 
        self.line1.show()

        self.add_padding()

        self.line2 = Gtk.HBox()
        button2 = Gtk.Button("Show activities")
        #button2.set_size_request(200,80)
        #self.line2.pack_start(button2, False, False, 0)
        self.line2.add(button2)
        button2.connect('clicked', self.show_activity_list, None)
        button2.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()
        self.add_padding()

        self.line3 = Gtk.HBox()
        text = Gtk.TextView()
        self.entry = Gtk.Entry()
        self.entry.set_sensitive(True)
        self.entry.connect('activate', self.entry_activate_cb)

        self.entry.show()
        self.line3.add(self.entry)
        self.main_container.add(self.line3)
        self.line3.show()
        
        self.set_canvas(self.main_container)
        
        self.main_container.show()             
    
    def add_padding(self):
        self.line_space1 = Gtk.HBox()
        self.main_container.add(self.line_space1) 
        self.line_space1.show()

        self.line_space2 = Gtk.HBox()
        self.main_container.add(self.line_space2) 
        self.line_space2.show()

    def show_modules(self, sender, data=None):
        
        self.mod = ShowModules(self.set_canvas)       
        self.mod.show_modules()

    def show_activity_list(self, sender, data=None):
        self.back_button.connect('clicked', self.show_options1)
        self.main_container = Gtk.VBox()

        self.add_padding()   
        self.line1 = Gtk.HBox()
        
        button1 = Gtk.Button("Hello World activity")
        #button1.set_size_request(200,80)
        #self.line1.pack_start(button1, False, False, 0)
        self.line1.add(button1)
        button1.connect('clicked', self.show_labels_hello, None)
        button1.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1) 
        self.line1.show()

        self.add_padding()
        self.line2 = Gtk.HBox()
        
        button2 = Gtk.Button("Write activity")
        #button2.set_size_request(200,80)
        #self.line2.pack_start(button2, False, False, 0)
        self.line2.add(button2)
        button2.connect('clicked', self.show_labels_write, None)
        button2.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()
        self.add_padding()

        self.set_canvas(self.main_container)
        self.main_container.show()             
    
    def show_labels_hello(self, sender, data=None):
        self.back_button.connect('clicked', self.show_activity_list)
        self.main_container = Gtk.VBox()
        
        self.add_padding()
        self.line1 = Gtk.HBox()
        
        self.label1 = Gtk.Label(_("Hello World activity step 1 - call activity.__init__"))
        self.label1.set_line_wrap( True )
        self.label1.modify_font(Pango.FontDescription("Sans 12"))
        self.line1.add(self.label1)
        self.label1.show()

        button1 = Gtk.Button("Show result")
        button1.set_size_request(200,80)
        self.line1.pack_start(button1, False, False, 0)
        button1.connect('clicked', self.hello_launch1, None)
        button1.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1)
        self.line1.show()

        self.add_padding()
        self.line2 = Gtk.HBox()
        
        self.label2 = Gtk.Label(_("Hello Word activity step 2 - add toolbox"))
        self.label2.set_line_wrap( True )
        self.label2.modify_font(Pango.FontDescription("Sans 12"))
        self.line2.add(self.label2)
        self.label2.show()

        button2 = Gtk.Button("Show result")
        button2.set_size_request(200,80)
        self.line2.pack_start(button2, False, False, 0)
        button2.connect('clicked', self.hello_launch2, None)
        button2.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()

        self.add_padding()                        
        self.line3 = Gtk.HBox()
        
        self.label3 = Gtk.Label(_("Hello World activity step 3 - add hello world label"))
        self.label3.set_line_wrap( True )
        self.label3.modify_font(Pango.FontDescription("Sans 12"))
        self.line3.add(self.label3)
        self.label3.show()   

        button3 = Gtk.Button("Show result")
        button3.set_size_request(200,80)
        self.line3.pack_start(button3, False, False, 0)
        button3.connect('clicked', self.hello_launch3, None)
        button3.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button3.show()
        
        self.main_container.add(self.line3) 
        self.line3.show()

        self.add_padding()
        self.line4 = Gtk.HBox()
        
        self.label4 = Gtk.Label(_("Hello World activity step 4 - add rotate button"))
        self.label4.set_line_wrap( True )
        self.label4.modify_font(Pango.FontDescription("Sans 12"))
        self.line4.add(self.label4)
        self.label4.show()   

        button4 = Gtk.Button("Show result")
        button4.set_size_request(200,80)
        self.line4.pack_start(button4, False, False, 0)
        button4.connect('clicked', self.hello_launch4, None)
        button4.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button4.show()
        
        self.main_container.add(self.line4) 
        self.line4.show()

        self.add_padding()
        self.set_canvas(self.main_container)
        self.main_container.show()

    def show_labels_write(self, sender, data=None):
        self.back_button.connect('clicked', self.show_activity_list)
        self.main_container = Gtk.VBox()
        self.add_padding()
        self.line1 = Gtk.HBox()

        self.label1 = Gtk.Label(_("Write activity step 1 "))
        self.label1.set_line_wrap( True )
        self.label1.modify_font(Pango.FontDescription("Sans 12"))
        self.line1.add(self.label1)
        self.label1.show()

        button1 = Gtk.Button("Show result")
        button1.set_size_request(200,80)
        self.line1.pack_start(button1, False, False, 0)
        button1.connect('clicked', self.write_launch1, None)
        button1.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button1.show()

        self.main_container.add(self.line1)
        self.line1.show()
        self.add_padding()
        self.line2 = Gtk.HBox()

        self.label2 = Gtk.Label(_("Write activity step 2"))
        self.label2.set_line_wrap( True )
        self.label2.modify_font(Pango.FontDescription("Sans 12"))
        self.line2.add(self.label2)
        self.label2.show()

        button2 = Gtk.Button("Show result")
        button2.set_size_request(200,80)
        self.line2.pack_start(button2, False, False, 0)
        button2.connect('clicked', self.write_launch2, None)
        button2.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button2.show()

        self.main_container.add(self.line2)
        self.line2.show()

        self.set_canvas(self.main_container)
        self.add_padding()
        self.line3 = Gtk.HBox()

        self.label3 = Gtk.Label(_("Write activity step 3"))
        self.label3.set_line_wrap( True )
        self.label3.modify_font(Pango.FontDescription("Sans 12"))
        self.line3.add(self.label3)
        self.label3.show()   

        button3 = Gtk.Button("Show result")
        button3.set_size_request(200,80)
        self.line3.pack_start(button3, False, False, 0)
        button3.connect('clicked', self.write_launch3, None)
        button3.get_child().modify_font(Pango.FontDescription("Sans 14"))
        button3.show()
        
        self.main_container.add(self.line3) 
        self.line3.show()
        self.add_padding()
        self.set_canvas(self.main_container)
        self.main_container.show()
         
    def hello_launch1(self, sender, data=None):
        f = open('/tmp/1', 'w')
        os.putenv('TUTOR_CLASS','HelloWorldActivity')
        self.launch()

    def hello_launch2(self, sender, data=None):
        f = open('/tmp/2', 'w')
        self.hello_launch1(sender, data)

    def hello_launch3(self, sender, data=None):
        f = open('/tmp/3', 'w')
        self.hello_launch2(sender, data)

    def hello_launch4(self, sender, data=None):
        f = open('/tmp/4', 'w')
        self.hello_launch3(sender, data)

    def write_launch1(self, sender, data=None):
        f = open('/tmp/1', 'w')
        os.putenv('TUTOR_CLASS','AbiWordActivity')
        self.launch()

    def write_launch2(self, sender, data=None):
        f = open('/tmp/2', 'w')
        self.write_launch1(sender, data)

    def write_launch3(self, sender, data=None):
        f = open('/tmp/3', 'w')
        self.write_launch2(sender, data)

    def launch(self):
        subprocess.Popen(['sugar-launch', 'org.sugarlabs.DevTutor'])

    def entry_activate_cb(self, entry):
        """Handle the event when Enter is pressed in the Entry."""
        text = entry.props.text
        if self.hellotube is not None:
            self.hellotube.SendText(text)

    def entry_text_update_cb(self, text):
        """Update Entry text when text received from others."""
        self.entry.props.text = text

    def _alert(self, title, text=None):
        try:
            self.remove_alert(self.alert)
        finally:
            self.alert = Alert()
            self.alert.props.title = title
            self.alert.props.msg = text
            self.add_alert(self.alert)
            self.alert.connect('response', self._alert_cancel_cb)
            self.alert.show()

    def _alert_cancel_cb(self, alert, response_id):
        #self.remove_alert(alert)
        pass

    def _shared_cb(self, activity):        
        self._logger.debug('My activity was shared')
        self.alert = Alert()
        self.alert.props.title = 'Shared Activity'
        self.alert.props.msg = 'Shared messages to be displayed here'
        self.add_alert(self.alert)
        self.initiating = True
        self._sharing_setup()

        self._logger.debug('This is my activity: making a tube...')
        id = self.tubes_chan[telepathy.CHANNEL_TYPE_TUBES].OfferDBusTube(
            SERVICE, {})

    def _sharing_setup(self):
        if self.shared_activity is None:
            self._logger.error('Failed to share or join activity')
            return

        self.conn = self.shared_activity.telepathy_conn
        self.tubes_chan = self.shared_activity.telepathy_tubes_chan
        self.text_chan = self.shared_activity.telepathy_text_chan

        self.tubes_chan[telepathy.CHANNEL_TYPE_TUBES].connect_to_signal(
            'NewTube', self._new_tube_cb)

        self.shared_activity.connect('buddy-joined', self._buddy_joined_cb)
        self.shared_activity.connect('buddy-left', self._buddy_left_cb)

        self.entry.set_sensitive(True)
        self.entry.grab_focus()

        # Optional - included for example:
        # Find out who's already in the shared activity:
        for buddy in self.shared_activity.get_joined_buddies():
            self._logger.debug('Buddy %s is already in the activity',
                               buddy.props.nick)

    def _list_tubes_reply_cb(self, tubes):
        for tube_info in tubes:
            self._new_tube_cb(*tube_info)

    def _list_tubes_error_cb(self, e):
        self._logger.error('ListTubes() failed: %s', e)

    def _joined_cb(self, activity):
        if not self.shared_activity:
            return

        self._logger.debug('Joined an existing shared activity')
        self._alert('Joined', 'Joined a shared activity')
        self.initiating = False
        self._sharing_setup()

        self._logger.debug('This is not my activity: waiting for a tube...')
        self.tubes_chan[telepathy.CHANNEL_TYPE_TUBES].ListTubes(
            reply_handler=self._list_tubes_reply_cb,
            error_handler=self._list_tubes_error_cb)

    def _new_tube_cb(self, id, initiator, type, service, params, state):
        self._logger.debug('New tube: ID=%d initator=%d type=%d service=%s '
                     'params=%r state=%d', id, initiator, type, service,
                     params, state)
        if (type == telepathy.TUBE_TYPE_DBUS and
            service == SERVICE):
            if state == telepathy.TUBE_STATE_LOCAL_PENDING:
                self.tubes_chan[telepathy.CHANNEL_TYPE_TUBES].AcceptDBusTube(id)
            tube_conn = TubeConnection(self.conn,
                self.tubes_chan[telepathy.CHANNEL_TYPE_TUBES],
                id, group_iface=self.text_chan[telepathy.CHANNEL_INTERFACE_GROUP])
            self.hellotube = TextSync(tube_conn, self.initiating,
                                      self.entry_text_update_cb,
                                      self._alert,
                                      self._get_buddy)

    def _buddy_joined_cb (self, activity, buddy):
        """Called when a buddy joins the shared activity.

        This doesn't do much here as HelloMesh doesn't have much 
        functionality. It's up to you do do interesting things
        with the Buddy...
        """
        self._logger.debug('Buddy %s joined', buddy.props.nick)
        self._alert('Buddy joined', '%s joined' % buddy.props.nick)

    def _buddy_left_cb (self, activity, buddy):
        """Called when a buddy leaves the shared activity.

        This doesn't do much here as HelloMesh doesn't have much 
        functionality. It's up to you do do interesting things
        with the Buddy...
        """
        self._logger.debug('Buddy %s left', buddy.props.nick)
        self._alert('Buddy left', '%s left' % buddy.props.nick)

    def _get_buddy(self, cs_handle):
        """Get a Buddy from a channel specific handle."""
        self._logger.debug('Trying to find owner of handle %u...', cs_handle)
        group = self.text_chan[telepathy.CHANNEL_INTERFACE_GROUP]
        my_csh = group.GetSelfHandle()
        self._logger.debug('My handle in that group is %u', my_csh)
        if my_csh == cs_handle:
            handle = self.conn.GetSelfHandle()
            self._logger.debug('CS handle %u belongs to me, %u', cs_handle, handle)
        elif group.GetGroupFlags() & telepathy.CHANNEL_GROUP_FLAG_CHANNEL_SPECIFIC_HANDLES:
            handle = group.GetHandleOwners([cs_handle])[0]
            self._logger.debug('CS handle %u belongs to %u', cs_handle, handle)
        else:
            handle = cs_handle
            self._logger.debug('non-CS handle %u belongs to itself', handle)
            # XXX: deal with failure to get the handle owner
            assert handle != 0
        return self.pservice.get_buddy_by_telepathy_handle(
            self.conn.service_name, self.conn.object_path, handle)

class BackButton(ToolButton):
    def __init__(self, **kwargs):
        ToolButton.__init__(self, 'back', **kwargs)
        self.props.tooltip = _('Back')
        self.props.accelerator = '<Alt>Left'


class TextSync(ExportedGObject):
    """The bit that talks over the TUBES!!!"""

    def __init__(self, tube, is_initiator, text_received_cb,
                 alert, get_buddy):
        super(TextSync, self).__init__(tube, PATH)
        self._logger = logging.getLogger('hellomesh-activity.TextSync')
        self.tube = tube
        self.is_initiator = is_initiator
        self.text_received_cb = text_received_cb
        self._alert = alert
        self.entered = False  # Have we set up the tube?
        self.text = '' # State that gets sent or received
        self._get_buddy = get_buddy  # Converts handle to Buddy object
        self.tube.watch_participants(self.participant_change_cb)

    def participant_change_cb(self, added, removed):
        self._logger.debug('Tube: Added participants: %r', added)
        self._logger.debug('Tube: Removed participants: %r', removed)
        for handle, bus_name in added:
            buddy = self._get_buddy(handle)
            if buddy is not None:
                self._logger.debug('Tube: Handle %u (Buddy %s) was added',
                                   handle, buddy.props.nick)
        for handle in removed:
            buddy = self._get_buddy(handle)
            if buddy is not None:
                self._logger.debug('Buddy %s was removed' % buddy.props.nick)
        if not self.entered:
            if self.is_initiator:
                self._logger.debug("I'm initiating the tube, will "
                    "watch for hellos.")
                self.add_hello_handler()
            else:
                self._logger.debug('Hello, everyone! What did I miss?')
                self.Hello()
        self.entered = True

    @signal(dbus_interface=IFACE, signature='')
    def Hello(self):
        """Say Hello to whoever else is in the tube."""
        self._logger.debug('I said Hello.')

    @method(dbus_interface=IFACE, in_signature='s', out_signature='')
    def World(self, text):
        """To be called on the incoming XO after they Hello."""
        if not self.text:
            self._logger.debug('Somebody called World and sent me %s',
                               text)
            self._alert('World', 'Received %s' % text)
            self.text = text
            self.text_received_cb(text)
            # now I can World others
            self.add_hello_handler()
        else:
            self._logger.debug("I've already been welcomed, doing nothing")

    def add_hello_handler(self):
        self._logger.debug('Adding hello handler.')
        self.tube.add_signal_receiver(self.hello_cb, 'Hello', IFACE,
            path=PATH, sender_keyword='sender')
        self.tube.add_signal_receiver(self.sendtext_cb, 'SendText', IFACE,
            path=PATH, sender_keyword='sender')

    def hello_cb(self, sender=None):
        """Somebody Helloed me. World them."""
        if sender == self.tube.get_unique_name():
            # sender is my bus name, so ignore my own signal
            return
        self._logger.debug('Newcomer %s has joined', sender)
        self._logger.debug('Welcoming newcomer and sending them the game state')
        self.tube.get_object(sender, PATH).World(self.text,
                                                 dbus_interface=IFACE)

    def sendtext_cb(self, text, sender=None):
        """Handler for somebody sending SendText"""
        if sender == self.tube.get_unique_name():
            # sender is my bus name, so ignore my own signal
            return
        self._logger.debug('%s sent text %s', sender, text)
        self._alert('sendtext_cb', 'Received %s' % text)
        self.text = text
        self.text_received_cb(text)

    @signal(dbus_interface=IFACE, signature='s')
    def SendText(self, text):
        """Send some text to all participants."""
        self.text = text
        self._logger.debug('Sent text: %s', text)
        client = GConf.Client.get_default()
        Text = client.get_string("/desktop/sugar/user/nick")
        self._alert(Text, '%s' % text)

