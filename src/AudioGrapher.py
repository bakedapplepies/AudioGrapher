import sys
import pygame
import numpy

from Audio import Audio
from Bar import Bar
from Keyboard import Keyboard

# OTHER
RESOLUTION = (1400, 800)

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = WHITE

# CLOCK
fpsClock = pygame.time.Clock()
FPS = 60


pygame.init()
class Window:
    def __init__(self) -> None:
        # WINDOW
        pygame.display.set_caption("Audio Grapher")
        self.window = pygame.display.set_mode(RESOLUTION, vsync=0)
        self.run = True

        # BARS VARIABLES
        self.barNumbers = 40;

        # BAR WIDTH
        self.barGap = 5
        self.barWidth = (RESOLUTION[0] - self.barGap * (self.barNumbers + 1)) / self.barNumbers;

        # INITIALIZATION OF BARS
        self.bars = numpy.empty(self.barNumbers, dtype=Bar)
        # spacing
        for i in range(1, self.barNumbers+1):
            self.bars[i-1] = Bar(self.barGap * i + (i-1) * self.barWidth, RESOLUTION[1], self.barWidth, 0, windowHeight=RESOLUTION[1])

        # AUDIO CHANNELS
        self.keyInputs = numpy.zeros(10, dtype=numpy.int8)
        
        # KEYBOARD
        self.keyboard = Keyboard()

    def loop(self) -> None:
        while self.run:
            self.Render()
            self.PollInput();

            pygame.display.update()
            fpsClock.tick(FPS)

    # RENDERING
    def Render(self) -> None:
        self.window.fill(BG_COLOR)

        self.DrawBars()

    def DrawBars(self) -> None:
        for i in range(0, self.barNumbers):
            pygame.draw.rect(self.window, BLACK, self.bars[i])
            self.bars[i].updateHeight(normal=self.keyInputs[int(i/self.barNumbers * 10)])

    # INPUT
    def PollInput(self) -> None:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            pygame.key
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # or python would continue rendering without the pygame context
            # self.keyInputs = self.keyboard.GetKeyNormals(event, keys)
            self.keyboard.GetKeyNormals(self.keyInputs, event, keys)

    # PROCESSING
    def ChannelMapping(self):
        pass


def change(a):
    a += 1

if __name__ == "__main__":
    window = Window()
    window.loop()
    # audio = Audio()
    # audio.getAudio(len=10)
    