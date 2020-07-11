import pygame
import os

pygame.init()   #초기화

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Bubble pang")


#FPS
clock = pygame.time.Clock() #화면에 초당 몇번 출력 할지

#1.게임 초기화(배경, 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일 위치 반환
image_path = os.path.join(current_path, "images")   #images 폴더 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]    #스테이지 높이위에 캐릭터를 두기 위해

#캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2)
character_y_pos = screen_height - character_height - stage_height


#이벤트 루프
running = True
while running:
    dt =clock.tick(30)

    #2.이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

    #3. 캐릭터 위치 정의
    #4. 충돌 처리
    #5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()

