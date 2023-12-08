# Jucimar Jr
# 2022

import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 10

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE,  COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# speed text

speed_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
speed_text = (speed_font
              .render('speed:', True, COLOR_WHITE, COLOR_BLACK))
speed_text_rect = speed_text.get_rect()
speed_text_rect.bottomleft = (50, 75)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1 and player 2 (robot)
player_1 = player_2 = pygame.image.load("assets/player.png")
player_1_y = player_2_y = 325
player_1_move_up = False
player_1_move_down = False
player_2_dy = 5

# game speed
speed = 60

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = -5
ball_dy = -5

# score
score_1 = 0
score_2 = 0


# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the lower/upper wall
        if ball_y > 700 or ball_y <= 100:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle

        if ball_x == 100:  # This adds angle for the collision of the ball

            # If you are above the middle of the play screen this happens:
            if player_1_y + 75 <= 325:

                # If you hit the part above the middle of the paddle you change the direction

                if player_1_y <= ball_y + 20 and player_1_y + 75 > ball_y:
                    ball_dy *= -1
                    ball_dx *= -1
                    speed += 9
                    bounce_sound_effect.play()

                # If you hit the parte bellow the middle of the paddle you keep going up or going down

                elif player_1_y + 150 >= ball_y and player_1_y + 75 <= ball_y + 20:
                    ball_dx *= -1
                    speed += 9
                    bounce_sound_effect.play()

            # Otherwise if you are bellow the hit of the paddle switch

            elif player_1_y + 75 > 325:
                # If you hit the part above the middle of the paddle you change the direction

                if player_1_y <= ball_y + 20 and player_1_y + 75 >= ball_y:
                    ball_dx *= -1
                    speed += 9
                    bounce_sound_effect.play()

                # If you hit the parte bellow the middle of the paddle you change the direction

                elif player_1_y + 150 >= ball_y and player_1_y + 75 < ball_y + 20:
                    ball_dy *= -1
                    ball_dx *= -1
                    speed += 9
                    bounce_sound_effect.play()

        # This makes the ball don't enter the paddle

        if 50 <= ball_x < 100:
            if ball_y + 20 >= player_1_y >= ball_y:

                ball_dy *= -1
                ball_y = player_1_y - 21
                ball_dx *= -1
                speed += 9
                bounce_sound_effect.play()

            elif player_1_y + 150 > ball_y and player_1_y < ball_y + 20:
                ball_dy *= -1
                ball_y = player_1_y + 151
                ball_dx *= -1
                speed += 9
                bounce_sound_effect.play()

        # If the ball is nearest to the score line it doesn't back
        elif ball_x < 50 or 50 <= ball_x + 20 < 75:
            if ball_y <= player_1_y <= ball_y + 20:

                ball_dy *= -1
                ball_y = player_1_y - 21
                speed += 9
                bounce_sound_effect.play()

            elif player_1_y + 150 > ball_y and player_1_y < ball_y + 20:
                ball_dy *= -1
                ball_y = player_1_y + 151
                speed += 9
                bounce_sound_effect.play()

        # ball collision with the player 2 's paddle

        if ball_x + 20 == 1180:  # This adds angle for the collision of the ball

            # If you are above the middle of the play screen this happens:
            if player_2_y + 75 <= 400:

                # If you hit the part above the middle of the paddle you change the direction

                if player_2_y <= ball_y + 20 and player_2_y + 75 > ball_y:
                    ball_dy *= -1
                    ball_dx *= -1
                    bounce_sound_effect.play()

                # If you hit the parte bellow the middle of the paddle you keep going up or going down

                elif player_2_y + 150 >= ball_y and player_2_y + 75 <= ball_y + 20:
                    ball_dx *= -1
                    bounce_sound_effect.play()

            # Otherwise if you are bellow the hit of the paddle switch

            elif player_2_y + 75 > 400:
                # If you hit the part above the middle of the paddle you change the direction

                if player_2_y <= ball_y + 20 and player_2_y + 75 >= ball_y:
                    ball_dx *= -1
                    bounce_sound_effect.play()

                # If you hit the parte bellow the middle of the paddle you change the direction

                elif player_2_y + 150 >= ball_y and player_2_y + 75 < ball_y + 20:
                    ball_dy *= -1
                    ball_dx *= -1
                    bounce_sound_effect.play()

        # This makes the ball don't enter the paddle
        if 1180 <= ball_x < 1230:
            if ball_y <= player_2_y <= ball_y + 20 or player_2_y + 75 >= ball_y >= player_2_y:

                ball_dy *= -1
                ball_y = player_2_y - 21
                ball_dx *= -1
                bounce_sound_effect.play()

            elif player_2_y + 150 > ball_y and player_2_y < ball_y + 20:
                ball_dy *= -1
                ball_y = player_2_y + 151
                ball_dx *= -1
                bounce_sound_effect.play()

        # If the ball is nearest to the score line it doesn't back

        elif ball_x + 20 > 1205 or 1205 <= ball_x < 1230:
            if ball_y <= player_2_y <= ball_y + 20:

                ball_dy *= -1
                ball_y = player_2_y - 21
                bounce_sound_effect.play()

            elif player_2_y + 150 > ball_y and player_2_y < ball_y + 20:
                ball_dy *= -1
                ball_y = player_2_y + 151
                bounce_sound_effect.play()

        # scoring points
        if ball_x < -50 or ball_x > 1320:
            if ball_x < -50:
                ball_dx = -5
                ball_dy = -5
                score_2 += 1
            elif ball_x > 1320:
                ball_dx = 5
                ball_dy = 5
                score_1 += 1
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            speed = 60
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 5
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 100:
            player_1_y = 100

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 collides with upper wall
        if player_2_y <= 100:
            player_2_y = 100

        # player 2 collides with lower wall
        if player_2_y >= 570:
            player_2_y = 570

        # player 2 "Artificial Intelligence"

        if speed % 2 == 0:
            if ball_dy > 0 or ball_dy < 0 or ball_dy == 0:
                player_2_y += player_2_dy
                if player_2_y + 150 >= 720:
                    player_2_dy *= -1
                if player_2_y <= 100:
                    player_2_dy *= -1

        elif speed % 2 != 0:
            if player_2_y >= ball_y or player_2_y + 75 >= ball_y + 20 <= player_2_y:
                player_2_y -= 5
            elif player_2_y + 150 <= ball_y + 20 or player_2_y + 75 <= ball_y <= player_2_y + 150:
                player_2_y += 5

        # update score hud

        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # update speed hud
        speed_text = speed_font.render('speed:' + str(speed), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
        screen.blit(speed_text, speed_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(speed)

pygame.quit()
