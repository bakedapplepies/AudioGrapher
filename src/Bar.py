import pygame


class Bar(pygame.Rect):
    def __init__(self, *args, windowHeight: int) -> None:
        super().__init__(*args)

        self.barHeight = self[3]
        self.heightIncrease: bool = True
        self.speed = 10
        self.rise = 50
        self.fall = 40
        self.windowHeight = windowHeight
        self.maxHeight = self.windowHeight * 0.75

    def changeHeight(self) -> None:
        self[1] = self.windowHeight - self.barHeight   # top-left corner
        self[3] = self.barHeight                       # vertical length

    def updateHeight(self, normal=0):
        if bool(normal):
            self.barHeight += self.rise
            if (self.barHeight > self.maxHeight):
                self.barHeight = self.maxHeight
        else:
            self.barHeight -= self.fall
            if (self.barHeight < 0):
                self.barHeight = 0
            
        self.changeHeight()
    
    def getInfo(self) -> None:
        print(self)
        