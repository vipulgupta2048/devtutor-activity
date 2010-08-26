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

import gtk
import logging
import pango
import os
import subprocess

import gobject

from gettext import gettext as _

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import *


class ShowModules(gobject.GObject):

    __gsignals__ = {
        'back': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,
                        ())
    }

    def __init__(self, canvas):
        gobject.GObject.__init__(self)
        self.set_canvas = canvas    
         
    def signal_handler(self, sender, data=None):
        self.emit('back')

    def show_modules(self):
        
        self.main_container = gtk.VBox()
        
        self.header = gtk.HBox()

        back_button = gtk.Button("Back")
        self.header.pack_start(back_button, False, False, 0)
        back_button.connect('clicked', self.signal_handler, None)
        back_button.show()        


        self.line1 = gtk.HBox()
        
        button1 = gtk.Button("Activity")
        self.line1.add(button1)
        button1.connect('clicked', self.activity, None)
        button1.show()
        button1.get_child().modify_font(pango.FontDescription("Sans 18"))
        
        self.line2 = gtk.HBox()
        button2 = gtk.Button("Graphics")
        self.line2.add(button2)
        button2.connect('clicked', self.graphics, None)
        button2.show()
        button2.get_child().modify_font(pango.FontDescription("Sans 18"))

        self.line3 = gtk.HBox()
        
        button3 = gtk.Button("Bundle")
        self.line3.add(button3)
        button3.connect('clicked', self.bundle, None)
        button3.show()
        button3.get_child().modify_font(pango.FontDescription("Sans 18"))

        self.line4 = gtk.HBox()
        button4 = gtk.Button("Datastore")
        self.line4.add(button4)
        button4.connect('clicked', self.datastore, None)
        button4.show()
        button4.get_child().modify_font(pango.FontDescription("Sans 18"))
        
        self.line5 = gtk.HBox()
        
        button5 = gtk.Button("Toolkit")
        button5.get_child().modify_font(pango.FontDescription("Sans 18"))
        self.line5.add(button5)        
        button5.connect('clicked', self.toolkit, None)
        button5.show()
        
        self.line6 = gtk.HBox()        
        button6 = gtk.Button("Dispatch")
        self.line6.add(button6)
        button6.connect('clicked', self.dispatch, None)
        button6.show()
        button6.get_child().modify_font(pango.FontDescription("Sans 18"))
        
        self.main_container.add(self.header) 
        self.main_container.add(self.line1) 
        self.main_container.add(self.line2)
        self.main_container.add(self.line3)
        self.main_container.add(self.line4) 
        self.main_container.add(self.line5)
        self.main_container.add(self.line6)

        self.header.show()   
        self.line1.show() 
        self.line2.show() 
        self.line3.show() 
        self.line4.show() 
        self.line5.show() 
        self.line6.show() 
        
        self.set_canvas(self.main_container)
        self.main_container.show()    
    
    def activity(self, sender, data=None):
        self.main_container = gtk.VBox()
        
        self.line1 = gtk.HBox()
        
        button1 = gtk.Button("Activity")
        self.line1.add(button1)
        #button1.connect('clicked', self.activity123, None)
        button1.show()
        button1.get_child().modify_font(pango.FontDescription("Sans 18"))

        button2 = gtk.Button("Bundlebuilder")
        self.line1.add(button2)
        #button2.connect('clicked', self.bundlebuilder, None)
        button2.show()
        button2.get_child().modify_font(pango.FontDescription("Sans 18"))

        self.line2 = gtk.HBox()
        
        button3 = gtk.Button("Factory")
        self.line2.add(button3)
        #button3.connect('clicked', self.factory, None)
        button3.show()
        button3.get_child().modify_font(pango.FontDescription("Sans 18"))

        button4 = gtk.Button("Handles")
        self.line2.add(button4)
        #button4.connect('clicked', self.handles, None)
        button4.show()
        button4.get_child().modify_font(pango.FontDescription("Sans 18"))

        self.line3 = gtk.HBox()
        
        button5 = gtk.Button("NamingAlert")
        self.line3.add(button5)
        #button5.connect('clicked', self.namingalert, None)
        button5.show()
        button5.get_child().modify_font(pango.FontDescription("Sans 18"))

        button6 = gtk.Button("Widgets")
        self.line3.add(button6)
        button6.connect('clicked', self.widgets, None)
        button6.show()
        button6.get_child().modify_font(pango.FontDescription("Sans 18"))
        
        self.main_container.add(self.line1) 
        self.main_container.add(self.line2)
        self.main_container.add(self.line3)
        self.line1.show() 
        self.line2.show() 
        self.line3.show() 
        
        self.set_canvas(self.main_container)
        self.main_container.show()    
    
        
    def graphics(self, sender, data=None):
        pass   
        
    def bundle(self, sender, data=None):
        pass
        
    def datastore(self, sender, data=None):
        pass
    
    def toolkit(self, sender, data=None):
        pass
        
    def dispatch(self, sender, data=None):
        pass
      
    def widgets(self, sender, data=None):
        self.container = gtk.VBox()         
        self.set_canvas(self.container)
        
        self.heading()
        self.add_line1()        
        #self.add_line2()
        self.add_line3()        
        #self.add_line4()
        self.add_line5()        
        self.add_line6()
        self.add_line7()
        self.add_line8()        
        self.container.show()    
                    
    def heading(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("Module/Method"))
        self.line.add(self.label)          
        self.label.show()    
       
        self.label1 = gtk.Label(_("GUI"))
        self.line.add(self.label1)          
        self.label1.show()    
       
        self.label2 = gtk.Label(_("Description"))
        self.line.add(self.label2)          
        self.label2.show()    
       
        self.container.add(self.line) 
        self.line.show() 
    
    
    def add_line1(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.StopButton()"))
        self.line.add(self.label)          
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        title_entry1 = StopButton(self)
        toolbar_box1.toolbar.insert(title_entry1, 0)
        title_entry1.show()        
        
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
       
        self.container.add(self.line) 
        self.line.show() 
    
    
    def add_line2(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.ActivityButton()"))
        self.line.add(self.label)        
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        activity_button1 = ActivityButton(self)
        toolbar_box1.toolbar.insert(activity_button1, 0)
        activity_button1.show()       
        
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
        
        self.container.add(self.line) 
        self.line.show() 
    
    def add_line3(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.KeepButton()"))       
        self.line.add(self.label)  
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        title_entry1 = KeepButton(self)
        toolbar_box1.toolbar.insert(title_entry1, 0)
        title_entry1.show()
         
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
        
        self.container.add(self.line) 
        self.line.show() 
    
    def add_line4(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.ShareButton()"))          
        self.line.add(self.label)  
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        title_entry1 = ShareButton(self)
        toolbar_box1.toolbar.insert(title_entry1, 0)
        title_entry1.show()
         
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
       
        self.container.add(self.line) 
        self.line.show() 
    
    def add_line5(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.RedoButton()"))        
        self.line.add(self.label)  
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        title_entry1 = RedoButton()
        toolbar_box1.toolbar.insert(title_entry1, 0)
        title_entry1.show()
         
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
       
        self.container.add(self.line) 
        self.line.show() 
    
    def add_line6(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.UndoButton()"))         
        self.line.add(self.label)  
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        title_entry1 = UndoButton()
        toolbar_box1.toolbar.insert(title_entry1, 0)
        title_entry1.show()
         
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
       
        self.container.add(self.line) 
        self.line.show() 
    
    def add_line7(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.CopyButton()"))         
        self.line.add(self.label)  
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        title_entry1 = CopyButton()
        toolbar_box1.toolbar.insert(title_entry1, 0)
        title_entry1.show()
         
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
        
        self.container.add(self.line) 
        self.line.show() 
    
    def add_line8(self):
        self.line = gtk.HBox()
        
        self.label = gtk.Label(_("sugar.activity.widgets.PasteButton()"))      
        self.line.add(self.label)  
        self.label.show()    
       
        toolbar_box1 = ToolbarBox()        
        self.line.add(toolbar_box1) 
        toolbar_box1.show()
        
        title_entry1 = PasteButton()
        toolbar_box1.toolbar.insert(title_entry1, 0)
        title_entry1.show()
         
        self.label1 = gtk.Label(_("Some Description"))
        self.line.add(self.label1)          
        self.label1.show()    
       
        self.container.add(self.line) 
        self.line.show() 
    
  
