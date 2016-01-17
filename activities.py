#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
from gi.repository import Pango
from gi.repository import GObject

import logging
import os
import subprocess

from gettext import gettext as _

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import *


class ShowActivities(GObject.GObject):

    def __init__(self, canvas):
        GObject.GObject.__init__(self)
        self.set_canvas = canvas
         
    def add_padding(self):
        self.line_space1 = Gtk.HBox()
        self.main_container.add(self.line_space1)
        self.line_space1.show()

        self.line_space2 = Gtk.HBox()
        self.main_container.add(self.line_space2)
        self.line_space2.show()

    def show_activities(self):
        self.main_container = Gtk.VBox()

        self.add_padding()

        self.line1 = Gtk.HBox()
        button1 = Gtk.Button("Hello World activity")
        button1.connect('clicked', self.show_labels_hello, None)
        button1.get_child().modify_font(pango.FontDescription("Sans 14"))
        button1.show()
        self.line1.add(button1)
        self.main_container.add(self.line1) 
        self.line1.show()

        self.add_padding()

        self.line2 = Gtk.HBox()
        button2 = Gtk.Button("Write activity")
        button2.connect('clicked', self.show_labels_write, None)
        button2.get_child().modify_font(pango.FontDescription("Sans 14"))
        button2.show()
        self.line2.add(button2)
        self.main_container.add(self.line2)
        self.line2.show()

        self.add_padding()

################################################
# If you want to add a new activity            #
# un-comment the following lines and           #
# replace your_activity by the activity name   #
#											   #
# create the front end and name the method as  #
# show_labels_your_activity                    #
#											   #
# In the source files of the activity          #
# insert lines like							   #
#		if os.path.exists('/tmp/1')            #
# which serves as the break-points             #
################################################

#        self.line3 = Gtk.HBox()
#        button3 = Gtk.Button("your_activity")
#        button3.connect('clicked', self.show_labels_your_activity, None)
#        button3.get_child().modify_font(pango.FontDescription("Sans 14"))
#        button3.show()
#        self.line3.add(button3)
#        self.main_container.add(self.line3)
#        self.line3.show()

#        self.add_padding()

        self.set_canvas(self.main_container)
        self.main_container.show()             

    def show_labels_hello(self, sender, data=None):
        # self.back_button.connect('clicked', self.show_activity_list)
        self.main_container = Gtk.VBox()
        
        self.add_padding()
        self.line1 = Gtk.HBox()
        
        self.label1 = Gtk.Label(_("Hello World activity step 1 - call activity.__init__"))
        self.label1.set_line_wrap( True )
        self.label1.modify_font(pango.FontDescription("Sans 12"))
        self.line1.add(self.label1)
        self.label1.show()

        button1 = Gtk.Button("Show result")
        button1.set_size_request(200,80)
        self.line1.pack_start(button1, False, False, 0)
        button1.connect('clicked', self.hello_launch1, None)
        button1.get_child().modify_font(pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1)
        self.line1.show()

        self.add_padding()
        self.line2 = Gtk.HBox()
        
        self.label2 = Gtk.Label(_("Hello Word activity step 2 - add toolbox"))
        self.label2.set_line_wrap( True )
        self.label2.modify_font(pango.FontDescription("Sans 12"))
        self.line2.add(self.label2)
        self.label2.show()

        button2 = Gtk.Button("Show result")
        button2.set_size_request(200,80)
        self.line2.pack_start(button2, False, False, 0)
        button2.connect('clicked', self.hello_launch2, None)
        button2.get_child().modify_font(pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()

        self.add_padding()                        
        self.line3 = Gtk.HBox()
        
        self.label3 = Gtk.Label(_("Hello World activity step 3 - add hello world label"))
        self.label3.set_line_wrap( True )
        self.label3.modify_font(pango.FontDescription("Sans 12"))
        self.line3.add(self.label3)
        self.label3.show()   

        button3 = Gtk.Button("Show result")
        button3.set_size_request(200,80)
        self.line3.pack_start(button3, False, False, 0)
        button3.connect('clicked', self.hello_launch3, None)
        button3.get_child().modify_font(pango.FontDescription("Sans 14"))
        button3.show()
        
        self.main_container.add(self.line3) 
        self.line3.show()

        self.add_padding()
        self.line4 = Gtk.HBox()
        
        self.label4 = Gtk.Label(_("Hello World activity step 4 - add rotate button"))
        self.label4.set_line_wrap( True )
        self.label4.modify_font(pango.FontDescription("Sans 12"))
        self.line4.add(self.label4)
        self.label4.show()   

        button4 = Gtk.Button("Show result")
        button4.set_size_request(200,80)
        self.line4.pack_start(button4, False, False, 0)
        button4.connect('clicked', self.hello_launch4, None)
        button4.get_child().modify_font(pango.FontDescription("Sans 14"))
        button4.show()
        
        self.main_container.add(self.line4) 
        self.line4.show()

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

    def show_labels_write(self, sender, data=None):
        # self.back_button.connect('clicked', self.show_activity_list)
        self.main_container = Gtk.VBox()
        self.add_padding()
        self.line1 = Gtk.HBox()

        self.label1 = Gtk.Label(_("Write activity step 1 "))
        self.label1.set_line_wrap( True )
        self.label1.modify_font(Pango.FontDescription("Sans 12"))
        self.line1.add(self.label1)
        self.label1.show()

        button1 = Gtk.Button("Show result")
        button1.set_size_request(200, 80)
        self.line1.pack_start(button1, False, False, 0)
        button1.connect('clicked', self.write_launch1, None)
        button1.get_child().modify_font(pango.FontDescription("Sans 14"))
        button1.show()
        
        self.main_container.add(self.line1)
        self.line1.show()
        self.add_padding()
        self.line2 = Gtk.HBox()
        
        self.label2 = Gtk.Label(_("Write activity step 2"))
        self.label2.set_line_wrap( True )
        self.label2.modify_font(pango.FontDescription("Sans 12"))
        self.line2.add(self.label2)
        self.label2.show()

        button2 = Gtk.Button("Show result")
        button2.set_size_request(200, 80)
        self.line2.pack_start(button2, False, False, 0)
        button2.connect('clicked', self.write_launch2, None)
        button2.get_child().modify_font(pango.FontDescription("Sans 14"))
        button2.show()
        
        self.main_container.add(self.line2)
        self.line2.show()

        self.set_canvas(self.main_container)
        self.add_padding()
        self.line3 = Gtk.HBox()
        
        self.label3 = Gtk.Label(_("Write activity step 3"))
        self.label3.set_line_wrap( True )
        self.label3.modify_font(pango.FontDescription("Sans 12"))
        self.line3.add(self.label3)
        self.label3.show()   

        button3 = Gtk.Button("Show result")
        button3.set_size_request(200,80)
        self.line3.pack_start(button3, False, False, 0)
        button3.connect('clicked', self.write_launch3, None)
        button3.get_child().modify_font(pango.FontDescription("Sans 14"))
        button3.show()
        
        self.main_container.add(self.line3) 
        self.line3.show()
        self.add_padding()
        self.set_canvas(self.main_container)
        self.main_container.show()        
    
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

