import pygame
from marahel import level_0, level_1, level_2, level_3, level_4

pygame.init()

# تنظیمات اولیه
tole = 642
arz = 460
screen = pygame.display.set_mode((tole, arz))
pygame.display.set_caption("MojiQuest Game")

# رنگ‌ها
siah = (255, 255, 255)

# تصویر زمینه
background = pygame.image.load("4 (2).png")

# لول فعلی
Level = 1
state = {}


# فونت
def font_motan(surface, noe_font, andaze, level_text, motan_zakhamet, rang, font_x, font_y):
    font = pygame.font.SysFont(noe_font, andaze)
    satar = font.render(level_text, motan_zakhamet, rang)
    makan = satar.get_rect(center=(font_x, font_y))
    surface.blit(satar, makan)

# حلقه‌ی اصلی بازی
barsi = True
clock = pygame.time.Clock()

while barsi:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            barsi = False

    # پاک‌سازی صفحه
    screen.fill((0, 0, 0))

    # رسم تصویر زمینه
    screen.blit(background, (0, 0))

    # رسم مستطیل پایین
    mostatil = pygame.Surface((500, 60))
    mostatil.fill((205, 133, 63))
    screen.blit(mostatil, (75, 370))

    # نمایش لول فعلی
    font_motan(screen, "Vazir.ttf", 30, f"Level {Level}", True, siah, 321, 20)
    # اجرای مرحله‌ی مربوطه
    if Level == 0:
        done = level_0(screen, events, state)
        if done:
            Level = 1
            state = {}
    elif Level == 1:
        done = level_1(screen, events, state)
        if done:
            Level = 2
            state = {}
    elif Level == 2:
        done = level_2(screen, events, state)
        if done:
            Level = 3
            state = {}
    elif Level == 3:
        done = level_3(screen, events, state)
        if done:
            Level = 4
            state = {}
    elif Level == 4:
        done = level_4(screen, events, state)
        if done:
            Level = 5
            state = {}


    # به‌روزرسانی صفحه
    pygame.display.update()
    clock.tick(30)

pygame.quit()