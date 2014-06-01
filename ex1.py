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

import pygame
from pyfader import IFader

def main():

    DONE = False

    pygame.init()
    screen = pygame.display.set_mode((1000,606))
    pygame.display.set_caption("Pyfader Image Fade-in Example.")

    img = IFader("","mesm.jpg")

    while not DONE:

        img.fadeIn()
        img.draw(screen)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                DONE = True

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
