import pygame

class Rook():
    def __init__(self, x, y, startx, starty, team):
        self.team = None
        self.x = x
        self.y = y
        self.startx = startx
        self.starty = starty
        self.width = 50
        self.height = 50
        self.hitbox = [self.x,self.y,self.width,self.height] #(self.x,self.y,self.width,self.height)
        self.rook_hold = False


        if team == 'b':
            self.team = 'black'
            self.image = 'BlackRook1.png'
        elif team == 'w':
            self.team = 'white'
            self.image = 'WhiteRook1.png'

    def draw(self, win):
        pawnImage = pygame.image.load(self.image)
        win.blit(pawnImage, (self.x, self.y))

    def collidepoint(self,n,w):
        # print(self.x)
        # print(self.y)
        # print(n)
        # pygame.draw.rect(w, (0,255,0), self.hitbox,2)
        if (n[0] >= self.hitbox[0] and n[0] <= self.hitbox[0]+self.width) and (n[1] >= self.hitbox[1]) and (n[1] <= self.hitbox[1]+self.height):
            # print('lol')
            return True
