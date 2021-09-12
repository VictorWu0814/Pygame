# pygame_01
# 起手式：建立一個視窗，點選 x或 esc退出程式

import pygame

surface = pygame.display.set_mode((600, 260))  # 設定視窗畫面
pygame.display.set_caption('這是一個簡易視窗')    # 視窗標題

surface.fill((125,125,125))  # 對視窗著色

pygame.display.flip()     # 顯示畫面
#pygame.display.update()  # 顯示畫面

mainloop = True  # 若為假則退出迴圈
while mainloop:
    for event in pygame.event.get():          # 這一部分就是事件處理
        if event.type == pygame.QUIT:         # 如果按下右上角的叉叉
            mainloop = False                  # 退出主迴圈
        elif event.type == pygame.KEYDOWN:    # 如果按下了鍵盤
            if event.key == pygame.K_ESCAPE:  # 且按下 ESC 鍵
                mainloop = False              # 退出主迴圈
