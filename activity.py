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

import gtk
import logging
import pango
import os
import subprocess

from gettext import gettext as _

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import *

from helloworld import HelloWorldActivity
from modules import ShowModules
from AbiWordActivity import *

class DevTutorActivity(activity.Activity):
    """DevTutorActivity class as specified in activity.info"""    

    def __init__(self, handle):
      
        activity.Activity.__init__(self, handle)
                  
        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()
            
        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show() 

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()
        
        self.show_options()  
        #self.show_labels()          

    def show_options1(self, data=None):   
        self.show_options()                
    def show_options(self):         
        
        self.main_container = gtk.VBox()

        self.add_padding()   
        self.line1 = gtk.HBox()
        
        button1 = gtk.Button("Show modules")
        #button1.set_size_request(200,80)
        #self.line1.pack_start(button1, False, False, 0)
        self.line1.add(button1)
        button1.connect('clicked', self.show_modules, None)
        button1.get_child().modify_font(pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1) 
        self.line1.show()

        self.add_padding()
        self.line2 = gtk.HBox()
        
        button2 = gtk.Button("Show activities")
        #button2.set_size_request(200,80)
        #self.line2.pack_start(button2, False, False, 0)
        self.line2.add(button2)
        button2.connect('clicked', self.show_activity_list, None)
        button2.get_child().modify_font(pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()
        self.add_padding()

        self.set_canvas(self.main_container)
        self.main_container.show()             
    
    def add_padding(self):
        self.line_space1 = gtk.HBox()           
        self.main_container.add(self.line_space1) 
        self.line_space1.show()

        self.line_space2 = gtk.HBox()     
        self.main_container.add(self.line_space2) 
        self.line_space2.show()

    def show_modules(self, sender, data=None):
        
        self.mod = ShowModules(self.set_canvas)
        self.mod.connect("back", self.show_options1)
        self.mod.show_modules()

    def show_activity_list(self, sender, data=None):
        self.main_container = gtk.VBox()

        self.add_padding()   
        self.line1 = gtk.HBox()
        
        button1 = gtk.Button("Hello World activity")
        #button1.set_size_request(200,80)
        #self.line1.pack_start(button1, False, False, 0)
        self.line1.add(button1)
        button1.connect('clicked', self.show_labels_hello, None)
        button1.get_child().modify_font(pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1) 
        self.line1.show()

        self.add_padding()
        self.line2 = gtk.HBox()
        
        button2 = gtk.Button("Write activity")
        #button2.set_size_request(200,80)
        #self.line2.pack_start(button2, False, False, 0)
        self.line2.add(button2)
        button2.connect('clicked', self.show_labels_write, None)
        button2.get_child().modify_font(pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()
        self.add_padding()

        self.set_canvas(self.main_container)
        self.main_container.show()             
    
    def show_labels_hello(self, sender, data=None):         
        self.main_container = gtk.VBox()
        
        self.line1 = gtk.HBox()
        
        self.label1 = gtk.Label(_("Hello World activity step 1 - call activity.__init__"))
        self.label1.set_line_wrap( True )
        self.label1.modify_font(pango.FontDescription("Sans 12"))
        self.line1.add(self.label1)
        self.label1.show()

        button1 = gtk.Button("Show result")
        button1.set_size_request(200,80)
        self.line1.pack_start(button1, False, False, 0)
        button1.connect('clicked', self.hello_launch1, None)
        button1.get_child().modify_font(pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1)
        self.line1.show()

        self.line2 = gtk.HBox()
        
        self.label2 = gtk.Label(_("Hello Word activity step 2 - add toolbox"))
        self.label2.set_line_wrap( True )
        self.label2.modify_font(pango.FontDescription("Sans 12"))
        self.line2.add(self.label2)
        self.label2.show()

        button2 = gtk.Button("Show result")
        button2.set_size_request(200,80)
        self.line2.pack_start(button2, False, False, 0)
        button2.connect('clicked', self.hello_launch2, None)
        button2.get_child().modify_font(pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()

                        
        self.line3 = gtk.HBox()
        
        self.label3 = gtk.Label(_("Hello World activity step 3 - add hello world label"))
        self.label3.set_line_wrap( True )
        self.label3.modify_font(pango.FontDescription("Sans 12"))
        self.line3.add(self.label3)
        self.label3.show()   

        button3 = gtk.Button("Show result")
        button3.set_size_request(200,80)
        self.line3.pack_start(button3, False, False, 0)
        button3.connect('clicked', self.hello_launch3, None)
        button3.get_child().modify_font(pango.FontDescription("Sans 14"))
        button3.show()
        
        self.main_container.add(self.line3) 
        self.line3.show()


        self.line4 = gtk.HBox()
        
        self.label4 = gtk.Label(_("Hello World activity step 4 - add rotate button"))
        self.label4.set_line_wrap( True )
        self.label4.modify_font(pango.FontDescription("Sans 12"))
        self.line4.add(self.label4)
        self.label4.show()   

        button4 = gtk.Button("Show result")
        button4.set_size_request(200,80)
        self.line4.pack_start(button4, False, False, 0)
        button4.connect('clicked', self.hello_launch4, None)
        button4.get_child().modify_font(pango.FontDescription("Sans 14"))
        button4.show()
        
        self.main_container.add(self.line4) 
        self.line4.show()

        self.set_canvas(self.main_container)
        self.main_container.show()         
         

    def show_labels_write(self, sender, data=None):         
        self.main_container = gtk.VBox()
        
        self.line1 = gtk.HBox()
        
        self.label1 = gtk.Label(_("Write activity step 1 "))
        self.label1.set_line_wrap( True )
        self.label1.modify_font(pango.FontDescription("Sans 12"))
        self.line1.add(self.label1)
        self.label1.show()

        button1 = gtk.Button("Show result")
        button1.set_size_request(200,80)
        self.line1.pack_start(button1, False, False, 0)
        button1.connect('clicked', self.write_launch1, None)
        button1.get_child().modify_font(pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1)
        self.line1.show()

        self.line2 = gtk.HBox()
        
        self.label2 = gtk.Label(_("Write activity step 2"))
        self.label2.set_line_wrap( True )
        self.label2.modify_font(pango.FontDescription("Sans 12"))
        self.line2.add(self.label2)
        self.label2.show()

        button2 = gtk.Button("Show result")
        button2.set_size_request(200,80)
        self.line2.pack_start(button2, False, False, 0)
        button2.connect('clicked', self.write_launch2, None)
        button2.get_child().modify_font(pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()

        self.set_canvas(self.main_container)
                
        self.line3 = gtk.HBox()
        
        self.label3 = gtk.Label(_("Write activity step 3"))
        self.label3.set_line_wrap( True )
        self.label3.modify_font(pango.FontDescription("Sans 12"))
        self.line3.add(self.label3)
        self.label3.show()   

        button3 = gtk.Button("Show result")
        button3.set_size_request(200,80)
        self.line3.pack_start(button3, False, False, 0)
        button3.connect('clicked', self.write_launch3, None)
        button3.get_child().modify_font(pango.FontDescription("Sans 14"))
        button3.show()
        
        self.main_container.add(self.line3) 
        self.line3.show()

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

    
