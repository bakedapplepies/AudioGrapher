import pygame
import numpy

class Keyboard:
    def __init__(self):
        # self.keyInputs = numpy.zeros(10, dtype=numpy.int8)
        pass
        
    def GetKeyNormals(self, keyInputs, event, keys):
        if event.type == pygame.KEYDOWN and keys[pygame.K_1]:
            keyInputs[0] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_1]:
            keyInputs[0] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_2]:
            keyInputs[1] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_2]:
            keyInputs[1] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_3]:
            keyInputs[2] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_3]:
            keyInputs[2] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_4]:
            keyInputs[3] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_4]:
            keyInputs[3] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_5]:
            keyInputs[4] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_5]:
            keyInputs[4] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_6]:
            keyInputs[5] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_6]:
            keyInputs[5] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_7]:
            keyInputs[6] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_7]:
            keyInputs[6] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_8]:
            keyInputs[7] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_8]:
            keyInputs[7] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_9]:
            keyInputs[8] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_9]:
            keyInputs[8] = 0;
        if event.type == pygame.KEYDOWN and keys[pygame.K_0]:
            keyInputs[9] = 1;
        elif event.type == pygame.KEYUP and keys[pygame.K_0]:
            keyInputs[9] = 0;
            
        # numpy.copyto(keyInputs, self.keyInputs)
            