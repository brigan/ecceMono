"""

   EcceHomo restauration game. 

"""

import sys, random as rnd;
from copy import copy;
import pygame as pg;
pg.init();


def moveTile(tilesRect, direction, nW=5, nH=7, tileSize=100):
    """moveTile function: 

        This function solves moving the white tile in one direction. 

    """

    pos = [(rect[0], rect[1]) for rect in tilesRect];
    if (direction=="UP"):
        # Check boundary:
        if (tilesRect[0][1]==0):
            return;
        
        # Move to target tile:
        destIndex = pos.index((tilesRect[0][0], tilesRect[0][1]-tileSize));
        tilesRect[destIndex] = (tilesRect[destIndex][0], tilesRect[destIndex][1]+tileSize);
        tilesRect[0] = (tilesRect[0][0], tilesRect[0][1]-tileSize);

    if (direction=="DOWN"): 
        if (tilesRect[0][1]==(nH-1)*tileSize):
            return;
        destIndex = pos.index((tilesRect[0][0], tilesRect[0][1]+tileSize));
        tilesRect[destIndex] = (tilesRect[destIndex][0], tilesRect[destIndex][1]-tileSize);
        tilesRect[0] = (tilesRect[0][0], tilesRect[0][1]+tileSize);

    if (direction=="LEFT"): 
        if (tilesRect[0][0]==0):
            return;
        destIndex = pos.index((tilesRect[0][0]-tileSize, tilesRect[0][1]));
        tilesRect[destIndex] = (tilesRect[destIndex][0]+tileSize, tilesRect[destIndex][1]);
        tilesRect[0] = (tilesRect[0][0]-tileSize, tilesRect[0][1]);

    if (direction=="RIGHT"): 
        if (tilesRect[0][0]==(nW-1)*tileSize):
            return;
        destIndex = pos.index((tilesRect[0][0]+tileSize, tilesRect[0][1]));
        tilesRect[destIndex] = (tilesRect[destIndex][0]-tileSize, tilesRect[destIndex][1]);
        tilesRect[0] = (tilesRect[0][0]+tileSize, tilesRect[0][1]);
    return;

def randomizeEH(eHTilesRect, eHTiles):
    """randomizeEH function: 

        This function randomizes the tiles of the Ecce Homo. 

    """

    moves = ["UP", "DOWN", "LEFT", "RIGHT"];
    for ii in range(1000): 
        moveTile(eHTilesRect, rnd.choice(moves));
        for iTile, tile in enumerate(eHTiles):
            screen.blit(tile, eHTilesRect[iTile]);
        pg.display.flip();



#### Script: 

size = width, height = 500,700;
nW, nH = 5, 7;
tileSize = 100;
white = 255,255,255;
screen = pg.display.set_mode(size);

eH = pg.image.load("Pics/ecceHomo.jpg");
eHRect = eH.get_rect();

eHTiles = [];
eHTilesRect = [];
for jj in range(nH): 
    for ii in range(nW):
        eHTiles += [pg.image.load("Pics/tile"+str(ii)+'_'+str(jj)+".jpg")];
        eHTilesRect += [(ii*tileSize,jj*tileSize)];
eHTilesRect_ = copy(eHTilesRect);


screen.fill(white);
pg.time.delay(5000);

screen.fill(white);
# screen.blit(eH, eHRect);
for iTile, tile in enumerate(eHTiles):
    screen.blit(tile, eHTilesRect[iTile]);
    pg.display.flip();
    pg.time.delay(100);
pg.time.delay(1000);

randomizeEH(eHTilesRect, eHTiles);


flagLoop = True;
while flagLoop:

    for event in pg.event.get():
        if (event.type is pg.KEYDOWN): 
            if (event.key == 273):
                moveTile(eHTilesRect, "UP");
            if (event.key == 274):
                moveTile(eHTilesRect, "DOWN");
            if (event.key == 276):
                moveTile(eHTilesRect, "LEFT");
            if (event.key == 275):
                moveTile(eHTilesRect, "RIGHT");

            if (event.key == 32):
                randomizeEH(eHTilesRect, eHTiles);

            if (event.key is pg.K_q):
                sys.exit();

        if (event.type is pg.QUIT): 
            sys.exit();

    for iTile, tile in enumerate(eHTiles):
        screen.blit(tile, eHTilesRect[iTile]);
    pg.display.flip();
    
    if (eHTilesRect[0] == (0,0)): 
        flagLoop = False;
        for iRect, rect in enumerate(eHTilesRect):
            if rect != eHTilesRect_[iRect]: 
                flagLoop = True;
                break;

for ii in range(4): 
    screen.fill(white);
    pg.display.flip();
    pg.time.delay(50);
    screen.blit(eH, (0,0));
    pg.display.flip();
    pg.time.delay(100);
pg.time.delay(900);

sys.exit();
