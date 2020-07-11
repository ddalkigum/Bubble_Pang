import pygame

pygame.init()   #초기화

screen_width = 640
screen_height = 480
pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Bubble pang")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

pygame.quit()

