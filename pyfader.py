"""
====================================================================

Pyfader - v1.0
Copyright (C) <2014>  <Ericson Willians.>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

====================================================================
Written by Ericson Willians, a brazilian composer and programmer.

CONTACT: ericsonwrp@gmail.com
AS A COMPOSER: https://soundcloud.com/r-p-ericson-willians
YOUTUBE CHANNEL: http://www.youtube.com/user/poisonewein
====================================================================
"""

import os
import pygame

class IFader():

    """
    The Image Fader.
    It creates a Surface object given a raw image file.
    It provides a method for drawing the Surface, whether it fades or not.
    """

    def __init__(self,path,name,size=None,bgColor=(0,0,0),initAlpha=0):
        self.sur = self.loadImage(path,name)
        if size is not None: # Where None is 'default image size'.
            try:
                self.sur = pygame.transform.scale(self.sur,size)
            except:
                print "A tuple with two indexes with integers is an acceptable size. '(n,n)'"
        elif size is None:
            pass
        self.bgColor = bgColor
        self.initAlpha = initAlpha
        self.sur.set_alpha(self.initAlpha)

    def loadImage(self,path,name,colorkey=None):

        fullname = os.path.join(path,name)
        try:
            i = pygame.image.load(fullname)
        except error, message:
            print "Cannot load image:", name
            raise SystemExit, message
        if ".png" not in name:
            i = i.convert()
        else:
            i = pygame.Surface.convert_alpha(i)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = i.get_at((0,0))
            i.set_colorkey(colorkey,pygame.RLEACCEL)
        return i

    def fadeIn(self,fSpeed=0.1):

        self.initAlpha += fSpeed

    def fadeOut(self,fSpeed=0.1):

        self.initAlpha -= fSpeed

    def draw(self,destSur,pos=(0,0)): # Where 'destSur' means 'Destination Surface'.

        destSur.fill(self.bgColor)
        destSur.blit(self.sur,(pos[0],pos[1]))
        self.sur.set_alpha(self.initAlpha)

class GSFader():

    """
    The General Surface Fader.
    It requires an external Surface object.
    It provides a method for drawing the Surface, whether it fades or not.
    """

    def __init__(self,surface,bgColor=(0,0,0),initAlpha=0):
        self.sur = surface
        self.bgColor = bgColor
        self.initAlpha = initAlpha

    def fadeIn(self,fSpeed=0.1):

        self.initAlpha += fSpeed

    def fadeOut(self,fSpeed=0.1):

        self.initAlpha -= fSpeed

    def draw(self,destSur,pos=(0,0)):

        destSur.fill(self.bgColor)
        destSur.blit(self.sur,(pos[0],pos[1]))
        self.sur.set_alpha(self.initAlpha)

