import pygame
import random
# تابع بررسی آزاد بودن کارت
def is_card_free(card, cards):
    rect = pygame.Rect(card["pos"], (80, 80))
    for other in cards:
        if other["visible"] and other["layer"] > card["layer"]:
            if pygame.Rect(other["pos"], (80, 80)).colliderect(rect):
                return False
    return True
# بررسی ست‌های مشابه داخل مستطیل
def check_for_sets(selected):
    counts = {}
    for card in selected:
        img = card["image"]
        counts[img] = counts.get(img, 0) + 1

    to_remove = []
    for img, count in counts.items():
        if count >= 3:
            # پیدا کردن 3 کارت مشابه
            matched = [card for card in selected if card["image"] == img][:3]
            to_remove.extend(matched)

    return to_remove


def level_0(screen, events, state):
    """
    state: دیکشنری برای نگه داشتن وضعیت مرحله (مثل کارت‌ها، انتخاب‌ها و ...)
    """

    # اگر بار اوله، کارت‌ها رو مقداردهی کن
    if "cards" not in state:
        state["cards"] = [
            {"image": "3 (2).png", "pos": (171, 140), "visible": True},
            {"image": "Untitled (2).png", "pos": (251, 140), "visible": True},
            {"image": "Untitled (2).png", "pos": (331, 140), "visible": True},
            {"image": "3 (2).png", "pos": (411, 140), "visible": True},
            {"image": "asd555 (2).png", "pos": (171, 240), "visible": True},
            {"image": "Untitled1 (2).png", "pos": (331, 240), "visible": True},
            {"image": "Untitled1 (2).png", "pos": (411, 240), "visible": True},
            {"image": "asd555 (2).png", "pos": (251, 240), "visible": True},
        ]
        state["selected"] = []
        state["matched_pairs"] = 0

    cards = state["cards"]
    selected = state["selected"]

    # پردازش ایونت‌ها (کلیک موس)
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for card in cards:
                if card["visible"]:
                    rect = pygame.Rect(card["pos"], (80, 80))
                    if rect.collidepoint(mouse_pos):
                        card["visible"] = False
                        selected.append(card)
                        break

    # نمایش کارت‌ها
    for card in cards:
        if card["visible"]:
            img = pygame.image.load(card["image"])
            screen.blit(img, card["pos"])

    # نمایش کارت‌های انتخاب شده (مثلا پایین صفحه)
    for i, card in enumerate(selected):
        x = 75 + i * 60
        y = 375
        img = pygame.image.load(card["image"])
        screen.blit(img, (x, y))

    # بررسی جفت‌ها
    if len(selected) == 2:
        if selected[0]["image"] == selected[1]["image"]:
            # جفت پیدا شد
            selected.clear()
            state["matched_pairs"] += 1
        else:
            # جفت نبودند: صبر کن و دوباره کارت‌ها رو برگردون
            pygame.time.wait(1000)
            for card in selected:
                card["visible"] = True
            selected.clear()

    # چک کنیم اگر همه جفت‌ها پیدا شدند
    if state["matched_pairs"] == len(cards) // 2:
        return True  # مرحله تموم شده

    return False  # مرحله هنوز تموم نشده

def level_1(screen, events, state):
    """
    مرحله دوم: 9 کارت، 3 تا جفت برای هر تصویر (ست 3تایی)
    """
    if "cards" not in state:
        # 3 تا از هر کارت (مثلاً 3 بار "3 (2).png" و 3 بار "Untitled (2).png" و 3 بار "asd555 (2).png")
        state["cards"] = [
            {"image": "3 (2).png", "pos": (150, 140), "visible": True},
            {"image": "3 (2).png", "pos": (230, 140), "visible": True},
            {"image": "3 (2).png", "pos": (310, 140), "visible": True},
            {"image": "Untitled (2).png", "pos": (150, 220), "visible": True},
            {"image": "Untitled (2).png", "pos": (230, 220), "visible": True},
            {"image": "Untitled (2).png", "pos": (310, 220), "visible": True},
            {"image": "asd555 (2).png", "pos": (150, 300), "visible": True},
            {"image": "asd555 (2).png", "pos": (230, 300), "visible": True},
            {"image": "asd555 (2).png", "pos": (310, 300), "visible": True},
        ]
        state["selected"] = []
        state["matched_sets"] = 0  # شمارش ست‌های پیدا شده

    cards = state["cards"]
    selected = state["selected"]

    # پردازش کلیک‌ها
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for card in cards:
                if card["visible"]:
                    rect = pygame.Rect(card["pos"], (80, 80))
                    if rect.collidepoint(mouse_pos):
                        card["visible"] = False
                        selected.append(card)
                        break

    # نمایش کارت‌ها
    for card in cards:
        if card["visible"]:
            img = pygame.image.load(card["image"])
            screen.blit(img, card["pos"])

    # نمایش کارت‌های انتخاب شده پایین صفحه
    for i, card in enumerate(selected):
        x = 75 + i * 60
        y = 375
        img = pygame.image.load(card["image"])
        screen.blit(img, (x, y))

    # بررسی ست‌های 3تایی
    if len(selected) == 3:
        images = [card["image"] for card in selected]
        if images.count(images[0]) == 3:
            # ست 3 تایی پیدا شد
            selected.clear()
            state["matched_sets"] += 1
        else:
            # نبود، کارت‌ها دوباره ظاهر میشن
            pygame.time.wait(1000)
            for card in selected:
                card["visible"] = True
            selected.clear()

    # چک اتمام مرحله
    if state["matched_sets"] == len(cards) // 3:
        return True  # مرحله تموم شده

    return False  # هنوز تموم نشده
def level_2(screen, events, state):
    if "cards" not in state:
        # ساخت کارت‌ها با لایه‌ها
        state["cards"] = [
            {"image": "3 (2).png", "pos": (200, 140), "layer": 0, "visible": True},
            {"image": "3 (2).png", "pos": (240, 140), "layer": 1, "visible": True},
            {"image": "3 (2).png", "pos": (280, 140), "layer": 2, "visible": True},

            {"image": "asd555 (2).png", "pos": (200, 220), "layer": 0, "visible": True},
            {"image": "asd555 (2).png", "pos": (240, 220), "layer": 1, "visible": True},
            {"image": "asd555 (2).png", "pos": (280, 220), "layer": 2, "visible": True},

            {"image": "Untitled (2).png", "pos": (200, 300), "layer": 0, "visible": True},
            {"image": "Untitled (2).png", "pos": (240, 300), "layer": 1, "visible": True},
            {"image": "Untitled (2).png", "pos": (280, 300), "layer": 2, "visible": True},
        ]
        state["selected"] = []
        state["matched_sets"] = 0

    cards = state["cards"]
    selected = state["selected"]

    # بررسی کلیک‌ها
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for card in sorted(cards, key=lambda c: -c["layer"]):  # از بالا به پایین
                if card["visible"]:
                    rect = pygame.Rect(card["pos"], (80, 80))
                    if rect.collidepoint(mouse_pos):
                        # بررسی اینکه کارت آزاد باشه
                        blocked = False
                        for other in cards:
                            if other["visible"] and other["layer"] > card["layer"]:
                                if pygame.Rect(other["pos"], (80, 80)).colliderect(rect):
                                    blocked = True
                                    break
                        if not blocked:
                            card["visible"] = False
                            selected.append(card)
                            break

    # نمایش کارت‌ها به ترتیب لایه
    for card in sorted(cards, key=lambda c: c["layer"]):
        if card["visible"]:
            img = pygame.image.load(card["image"])
            screen.blit(img, card["pos"])

    # نمایش کارت‌های انتخاب شده پایین صفحه
    for i, card in enumerate(selected):
        x = 75 + i * 60
        y = 375
        img = pygame.image.load(card["image"])
        screen.blit(img, (x, y))

    # بررسی ست‌های 3تایی
    if len(selected) == 3:
        images = [card["image"] for card in selected]
        if images.count(images[0]) == 3:
            selected.clear()
            state["matched_sets"] += 1
        else:
            pygame.time.wait(1000)
            for card in selected:
                card["visible"] = True
            selected.clear()

    if state["matched_sets"] == 3:
        return True

    return False
def level_3(screen, events, state):
    if "cards" not in state:
        images = [
            "3 (2).png", "asd555 (2).png", "asd666 (2).png",
            "Untitled (2).png", "Untitled1 (2).png", "asd777 (2).png"
        ]
        cards = []
        positions = [
            (200, 140), (240, 140), (280, 140), (320, 140),
            (180, 180), (220, 180), (260, 180), (300, 180),
            (160, 220), (200, 220), (240, 220), (280, 220),
            (220, 260), (260, 260), (300, 260), (180, 300),
            (240, 300), (280, 300)
        ]
        layers = [0, 1, 2] * 6  # 18 کارت با لایه‌های مختلف

        # ساخت کارت‌ها
        for i in range(18):
            cards.append({
                "image": images[i % 6],
                "pos": positions[i],
                "layer": layers[i],
                "visible": True
            })

        random.shuffle(cards)  # بهم‌ریختگی واقعی
        state["cards"] = cards
        state["selected"] = []
        state["matched_sets"] = 0

    cards = state["cards"]
    selected = state["selected"]

    # پردازش کلیک‌ها
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for card in sorted(cards, key=lambda c: -c["layer"]):
                if card["visible"]:
                    rect = pygame.Rect(card["pos"], (80, 80))
                    if rect.collidepoint(mouse_pos):
                        # بررسی آزاد بودن کارت
                        blocked = False
                        for other in cards:
                            if other["visible"] and other["layer"] > card["layer"]:
                                if pygame.Rect(other["pos"], (80, 80)).colliderect(rect):
                                    blocked = True
                                    break
                        if not blocked:
                            card["visible"] = False
                            selected.append(card)
                            break

    # نمایش کارت‌ها به ترتیب لایه
    for card in sorted(cards, key=lambda c: c["layer"]):
        if card["visible"]:
            img = pygame.image.load(card["image"])
            screen.blit(img, card["pos"])

    # نمایش کارت‌های انتخاب‌شده پایین صفحه
    for i, card in enumerate(selected):
        x = 75 + i * 60
        y = 375
        img = pygame.image.load(card["image"])
        screen.blit(img, (x, y))

    # بررسی ست‌های 3تایی
    if len(selected) == 3:
        images = [card["image"] for card in selected]
        if images.count(images[0]) == 3:
            selected.clear()
            state["matched_sets"] += 1
        else:
            pygame.time.wait(1000)
            for card in selected:
                card["visible"] = True
            selected.clear()

    if state["matched_sets"] == 6:
        return True

    return False
def level_4(screen, events, state):
    if "cards" not in state:
        mouse_images = [
            "3 (2).png", "asd555 (2).png", "asd666 (2).png",
            "asd777 (2).png", "Untitled (2).png", "Untitled1 (2).png"
        ]
        cards = []
        positions = [
            (200, 140), (240, 140), (280, 140), (320, 140),
            (180, 180), (220, 180), (260, 180), (300, 180),
            (160, 220), (200, 220), (240, 220), (280, 220),
            (220, 260), (260, 260), (300, 260), (180, 300),
            (240, 300), (280, 300)
        ]
        layers = [0, 1, 2] * 6

        for i in range(18):
            cards.append({
                "image": mouse_images[i % 6],
                "pos": positions[i],
                "layer": layers[i],
                "visible": True
            })

        random.shuffle(cards)
        state["cards"] = cards
        state["selected"] = []
        state["matched_sets"] = 0
        state["wrong_timer"] = 0

    cards = state["cards"]
    selected = state["selected"]

    # بررسی کلیک موس
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for card in sorted(cards, key=lambda c: -c["layer"]):
                if card["visible"]:
                    rect = pygame.Rect(card["pos"], (80, 80))
                    if rect.collidepoint(mouse_pos) and is_card_free(card, cards):
                        card["visible"] = False
                        selected.append(card)
                        break

    # نمایش کارت‌ها
    for card in sorted(cards, key=lambda c: c["layer"]):
        if card["visible"]:
            img = pygame.image.load(card["image"])
            screen.blit(img, card["pos"])

    # نمایش کارت‌های انتخاب‌شده
    for i, card in enumerate(selected):
        x = 75 + i * 60
        y = 375
        img = pygame.image.load(card["image"])
        screen.blit(img, (x, y))

    # بررسی ست
    if len(selected) == 3 and state["wrong_timer"] == 0:
        images = [card["image"] for card in selected]
        if images.count(images[0]) == 3:
            selected.clear()
            state["matched_sets"] += 1
        else:
            state["wrong_timer"] = pygame.time.get_ticks()

    # برگشت کارت‌های اشتباه بعد از 1 ثانیه
    if state["wrong_timer"] > 0:
        if pygame.time.get_ticks() - state["wrong_timer"] > 1000:
            for card in selected:
                card["visible"] = True
            selected.clear()
            state["wrong_timer"] = 0

    if state["matched_sets"] == 6:
        return True
    return False
