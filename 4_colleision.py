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
stage = pygame.image.load(os.path.join(image_path, "stage.png"))]
stage_size = stage.get_rect().size
stage_height = stage_size[1]    #스테이지 높이위에 캐릭터를 두기 위해 ["가로","세로"]

#캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동방향
character_to_x = 0

#캐릭터 속도
character_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons =[]
weapon_speed = 10

#공 만들기
ball_images =[
    pygame.image.load(os.path.join(image_path, "ball1.png")),
    pygame.image.load(os.path.join(image_path, "ball2.png")),
    pygame.image.load(os.path.join(image_path, "ball3.png")),
    pygame.image.load(os.path.join(image_path, "ball4.png"))]

#공 스피드(크기에 따른 스피드)
ball_speed_y = [-18, -15, -12, -9]

#공 정보, dictionary로 관리
balls = []
#y값을 지정해서 랜덤한 위치에서 생성되게 해보자
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "image_index" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_speed_y" : ball_speed_y[0]})  #y 최초 속도
#사라질 무기, 공 정보
weapon_to_remove = -1
ball_to_remove = -1

#이벤트 루프
running = True
while running:
    dt =clock.tick(30)

    #2.이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key ==pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width/2 -(weapon_width /2)
                weapon_y_pos = character_y_pos 
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                character_to_x = 0   

    #3. 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
         character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    weapons = [[w[0], w[1] - weapon_speed] for w in weapons if w[1]>0]

    #공 위치 정의
    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_image_index = ball_value["image_index"]

        ball_size = ball_images[ball_image_index].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        #공 위치 변경
        if ball_pos_x <=0 or ball_pos_x > screen_width - ball_width:
            ball_value["to_x"] = ball_value["to_x"]*-1
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_value["to_y"] = ball_value["init_speed_y"]
        else:
            ball_value["to_y"] += 0.5

        ball_value["pos_x"] += ball_value["to_x"]
        ball_value["pos_y"] += ball_value["to_y"]

    #4. 충돌 처리
    #캐릭터 rect update
    character_rect= character.get_rect()
    character_rect.left = character_x_pos
    chracter_rect.top = character_y_pos

    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_image_index = ball_value["image_index"]

        #공 rect정보 업데이트
        ball_rect = ball_images[ball_image_index].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball.pos_y
        #공 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running: False
            break

        #공 무기 충돌처리
        for weapon_index, weapon_value in enumerate(weapons):
            weapon_pos_x = weapon_value[0]
            weapon_pos_y = weapon_value[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_index
                ball_to_remove = ball_index

        #충돌 공, 무기 없애기
        if ball_to_remove > -1:
            del balls[ball_to_remove]       
            ball_to_remove = -1
        if weapon_to_remove > -1:
            del weapons[weapon_to_remove]       
            weapon_to_remove = -1


            

    #5. 화면에 그리기
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for index, value in enumerate(balls):
        ball_pos_x = value["pos_x"]
        ball_pos_y = value["pos_y"]
        ball_image_index = value["image_index"]
        screen.blit(ball_images[ball_image_index], (ball_pos_x,ball_pos_y))
            

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    

    pygame.display.update()

pygame.quit()

