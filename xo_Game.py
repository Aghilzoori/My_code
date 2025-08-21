import random
import pygame
pygame.init()
#مقدار های پنجره و اسم بازی 
white = (255, 255, 255)
red = (250, 10, 0)
length = 400
height = 600
Window_size = pygame.display.set_mode((length, height))
pygame.display.set_caption("xo game")
#تابع نمایش مربع 
def Draw_a_square(lengthx, heighty, x, y, colors, display):
    square = pygame.Rect(lengthx, heighty, x, y)
    pygame.draw.rect(display, colors, square)
    return square
#تابع نمایش متن 
def Display_text(font_size, name_font, TEXT, color_text, x, y, center_rect=None):
    font = pygame.font.SysFont(name_font, font_size)
    text = font.render(TEXT, True, color_text)
    text_rect = text.get_rect(center=(x, y))
    if center_rect:
        text_rect.center = center_rect.center 
    else:
        text_rect.center = (x, y)
    Window_size.blit(text, text_rect)
    pygame.display.update()
#مقدار های بازی
turn = "X"
win_x = 0
win_y = 0  
#مربع ها برابر با کدو بازی کن هستن 
a1 = ""
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
a8 = ""
a9 = ""
#حلقه اصلی
start = True
while start:
    # mouse_pos = pygame.mouse.get_pos()
    #مربع ها 
    square1 = Draw_a_square(10, 50, 120, 120, red, Window_size)
    Display_text(200, None, str(a1), white, 100, 100, square1)
    square2= Draw_a_square(140, 50, 120, 120, red, Window_size)
    Display_text(200, None, str(a2), white, 100, 100, square2)
    square3= Draw_a_square(270, 50, 120, 120, red, Window_size)
    Display_text(200, None, str(a3), white, 100, 100, square3)
    square4= Draw_a_square(10, 180, 120, 120, red, Window_size)
    Display_text(200, None, str(a4), white, 100, 100, square4)
    square5= Draw_a_square(140, 180, 120, 120, red, Window_size)
    Display_text(200, None, str(a5), white, 100, 100, square5)
    square6= Draw_a_square(270, 180, 120, 120, red, Window_size)
    Display_text(200, None, str(a6), white, 100, 100, square6)
    square7= Draw_a_square(10, 310, 120, 120, red, Window_size)
    Display_text(200, None, str(a7), white, 100, 100, square7)
    square8= Draw_a_square(140, 310, 120, 120, red, Window_size)
    Display_text(200, None, str(a8), white, 100, 100, square8)
    square9= Draw_a_square(270, 310, 120, 120, red, Window_size)
    Display_text(200, None, str(a9), white, 100, 100, square9)
    #
    if (a1 == "X" and a2 == "X" and a3 == "X") or (a4 == "X" and a5 == "X" and a6 == "X") or (a7 == "X" and a8 == "X" and a9 == "X") or (a1 == "X" and a4 == "X" and a7== "X") or (a2 == "X" and a5 == "X" and a8 == "X") or (a3 == "X" and a6 == "X" and a9 == "X") or (a1 == "X" and a5 == "X" and a9 == "X") or (a3 == "X" and a5 == "X" and a7 == "X"):
        Display_text(30, None, "x bordeeeeeeeeeeeeeeeee", white, 150, 500)
        win_x += 1
    if (a1 == "O" and a2 == "O" and a3 == "O") or (a4 == "O" and a5 == "O" and a6 == "O") or (a7 == "O" and a8 == "O" and a9 == "O") or (a1 == "O" and a4 == "O" and a9== "O") or (a2 == "O" and a5 == "O" and a8 == "O") or (a3 == "O" and a6 == "O" and a9 == "O") or (a1 == "O" and a5 == "O" and a9 == "O") or (a3 == "O" and a5 == "O" and a7 == "O"):
        Display_text(30, None, "o bordeeeeeeeeeeeeeeeee", white, 150, 500)
        win_y += 1
    #دریافت ایونت ها 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == "X":
                if square1.collidepoint(event.pos):
                    if a1 == "":
                        a1 = "X"
                if square2.collidepoint(event.pos):
                    if a2 == "":
                        a2 = "X"
                if square3.collidepoint(event.pos):
                    if a3 == "":
                        a3 = "X"
                if square4.collidepoint(event.pos):
                    if a4 == "":
                        a4 = "X"
                if square5.collidepoint(event.pos):
                    if a5 == "":
                        a5 = "X"
                if square6.collidepoint(event.pos):
                    if a6 == "":
                        a6 = "X"
                if square7.collidepoint(event.pos):
                    if a7 == "":
                        a7 = "X"
                if square8.collidepoint(event.pos):
                    if a8 == "":
                        a8 = "X"
                if square9.collidepoint(event.pos):
                    if a9 == "":
                        a9 = "X"
                turn = "O"
            else:
                if square1.collidepoint(event.pos):
                    if a1 == "":
                        a1 = "O"
                if square2.collidepoint(event.pos):
                    if a2 == "":
                        a2 = "O"
                if square3.collidepoint(event.pos):
                    if a3 == "":
                        a3 = "O"
                if square4.collidepoint(event.pos):
                    if a4 == "":
                        a4 = "O"
                if square5.collidepoint(event.pos):
                    if a5 == "":
                        a5 = "O"
                if square6.collidepoint(event.pos):
                    if a6 == "":
                        a6 = "O"
                if square7.collidepoint(event.pos):
                    if a7 == "":
                        a7 = "O"
                if square8.collidepoint(event.pos):
                    if a8 == "":
                        a8 = "O"
                if square9.collidepoint(event.pos):
                    if a9 == "":
                        a9 = "O"
                turn = "X"
            print(event)
    #اپدیت و ...ظ
    Display_text(30, None, f"x = {win_x} and O = {win_y}", red , 200, 550)
    pygame.display.update()
pygame.quit()
quit