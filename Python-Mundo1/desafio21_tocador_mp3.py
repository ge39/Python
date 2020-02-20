#faça um programa em python que reproduza o áudio deu arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('legiao.mp3')
pygame.event.wait()
