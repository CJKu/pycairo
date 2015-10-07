#! /usr/bin/env python
import framework
from math import pi
import cairo

class Shapes(framework.Screen):
    def draw(self, cr, width, height):

        # Draw background
        cr.set_source_rgb(1, 1, 1)
        cr.rectangle(0, 0, width, height)
        cr.fill()

        # draw grid
        cr.set_source_rgb(0.9, 0.9, 1)
        cr.set_line_width(1)
        advance = 10.5
        while advance < width:
            cr.move_to(advance, 0)
            cr.rel_line_to(0, height)
            advance += 10

        advance = 10.5
        while advance < width:
            cr.move_to(0, advance)
            cr.rel_line_to(width, 0)
            advance += 10
        
        cr.stroke()
      
        # Draw 7 X 7 pattern image
        cr.new_path()
        matrix = cairo.Matrix(1.571429, 0, 0, 1.571429, 35.00, 23.00) # 1, 1
        cr.set_matrix(matrix);
        cr.rectangle(1, 1, 5, 5)
        imageSurface = cairo.ImageSurface.create_from_png ("img_7_7.png")
        surfacePattern = cairo.SurfacePattern (imageSurface)
        surfacePattern.set_filter (cairo.FILTER_NEAREST)
        surfacePattern.set_extend (cairo.EXTEND_NONE)
        cr.set_antialias (cairo.ANTIALIAS_NONE); # must skip AA.
        #patternMatrix = cairo.Matrix(1, 0, 0, 1, 0, 0) # 1, 1
        #surfacePattern.set_matrix (patternMatrix)
        cr.set_source (surfacePattern)
        cr.fill ()

        # Draw 7 X 5 pattern image
        cr.new_path()
        matrix = cairo.Matrix(1.571429, 0, 0, 1.6, 35.00, 56.00) # 1, 1
        cr.set_matrix(matrix);
        cr.rectangle(1, 0, 5, 21)
        imageSurface = cairo.ImageSurface.create_from_png ("img_7_5.png")
        surfacePattern = cairo.SurfacePattern (imageSurface)
        surfacePattern.set_filter (cairo.FILTER_NEAREST)
        surfacePattern.set_extend (cairo.EXTEND_REPEAT)
        cr.set_antialias (cairo.ANTIALIAS_NONE);
        cr.set_source (surfacePattern)
        cr.fill ()

        # Draw 5 X 7 pattern image
        cr.new_path()
        matrix = cairo.Matrix(1.6, 0, 0, 1.571429, 36.00, 86.00) # 1, 1
        cr.set_matrix(matrix);
        cr.rectangle(0, 1, 21, 5)
        imageSurface = cairo.ImageSurface.create_from_png ("img_5_7.png")
        surfacePattern = cairo.SurfacePattern (imageSurface)
        surfacePattern.set_filter (cairo.FILTER_NEAREST)
        surfacePattern.set_extend (cairo.EXTEND_REPEAT)
        cr.set_antialias (cairo.ANTIALIAS_NONE);
        cr.set_source (surfacePattern)
        cr.fill ()

framework.run(Shapes)
