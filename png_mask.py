#!/usr/bin/python

'''
ZetCode PyCairo tutorial 

This program shows how to draw 
an image on a GTK window in PyCairo.

author: Jan Bodnar
website: zetcode.com 
last edited: August 2012
'''

from gi.repository import Gtk
import cairo


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        self.load_image()
        
        
    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Image")
        self.resize(400, 400)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
        
    def load_image(self):
        
        self.ims = cairo.ImageSurface.create_from_png("imgs/stmichaelschurch.png")
        self.mask = cairo.ImageSurface.create_from_png("imgs/omen.png") 
            
    def on_draw(self, wid, cr):

        cr.set_source_surface(self.ims, 0, 0)
        #cr.paint()
        #cr.set_source_rgb(100, 0, 0)
        maskPattern = cairo.SurfacePattern(self.mask)
        mat = cairo.Matrix();
        mat.scale(2, 2)
        maskPattern.set_matrix(mat)
        cr.mask(maskPattern)
        #cr.mask_surface(self.mask, 0, 0)
        cr.fill()
    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()