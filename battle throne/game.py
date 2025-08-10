import pygame
pygame.init()

# اندازه صفحه
width = 1200
length = 700
screen = pygame.display.set_mode((width, length))
pygame.display.set_caption("Battle Throne game")

# بارگذاری تصاویر
button_image = pygame.image.load("setting.png")
mouse_location = button_image.get_rect(topleft=(0, 0))

background = pygame.image.load("background.png")

a = pygame.image.load("Exit.png")
mouse_location_exit = a.get_rect(topleft=(1150, 500))

# مقادیر
show_setting = False
check = True

# حلقه اصلی
while check:
    # گرفتن همه ایونت‌ها
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_location.collidepoint(event.pos):
                show_setting = True
            if show_setting and mouse_location_exit.collidepoint(event.pos):
                show_setting= False

    # رسم پس‌زمینه
    screen.blit(background, (0, 0))
    screen.blit(button_image, mouse_location)

    # رسم مستطیل و دکمه دوم
    if show_setting:
        pygame.draw.rect(screen, (0, 200, 0), (0, 500, 1200, 200))
        screen.blit(a, mouse_location_exit)

    pygame.display.update()

pygame.quit()