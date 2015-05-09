import pygame
import cwiid
import sys
import time
from GIFImage import GIFImage

objection_playing = False
normal_playing = True
desk_playing = False


def main():
    global normal_playing
    global desk_playing
    global objection_playing

    print 'Press button 1 + 2 on your Wii Remote...'
    time.sleep(1)

    wm = cwiid.Wiimote()
    print 'Wii Remote connected...'
    print '\nPress the PLUS button to disconnect the Wii and end the application'
    time.sleep(1)

    Rumble = False
    wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    wm.led = 1

    pygame.init()
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("testing")
    myfont = pygame.font.SysFont("monospace", 16)
    WHITE = (255, 255, 255)
    GREEN = (0, 140, 50)

    clock = pygame.time.Clock()

    deskslam = GIFImage("img/deskslam.gif")
    objection = GIFImage("img/objection.gif")
    normal = GIFImage("img/normal.gif")

    objection_playing = False
    desk_playing = False
    normal_playing = True

    score = 0

    while True:

        pygame.display.flip()
        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

        screen.fill(WHITE)

        if (objection_playing):
            objection.render(screen, (0, 0), True, reset)
        if (desk_playing):
            deskslam.render(screen, (0, 0), True, reset)
        if (normal_playing):
            normal.render(screen, (0, 0))

        Xaxis = "X: " + str(wm.state['acc'][0])
        Yaxis = "Y: " + str(wm.state['acc'][1])
        Zaxis = "Z: " + str(wm.state['acc'][2])

        wiimotetext = myfont.render(Xaxis + " " + Yaxis + " " + Zaxis, 1, GREEN)
        screen.blit(wiimotetext, (300, 5))

        if wm.state['acc'][2] <= 40:
            print 'SLAM'
            desk_playing = True
            objection_playing = False
            normal_playing = False
            deskslam.rewind()
            pygame.mixer.music.load('sound/sfx-deskslam.wav')
            pygame.mixer.music.play()

        if wm.state['acc'][1] <= 50:
            print 'OBJECTION!'
            objection_playing = True
            desk_playing = False
            normal_playing = False
            objection.rewind()
            pygame.mixer.music.load('sound/objection.mp3')
            pygame.mixer.music.play()

        if wm.state['buttons'] == 512:
            position = 50
            print 'Position: ', position

        while wm.state['buttons'] == 8:
            print(wm.state)

        if wm.state['buttons'] == 2:
            print 'Button 1 pressed'

        if wm.state['buttons'] == 1:
            print 'Button 2 pressed'
        if wm.state['buttons'] == 16:
            if Rumble == False:
                wm.rumble = True
                Rumble = True
            elif Rumble == True:
                wm.rumble = False
                Rumble = False
        if wm.state['buttons'] == 4096:
            print 'closing Bluetooth connection. Good Bye!'
            time.sleep(1)
            exit(wm)
        clock.tick(60)


def reset():
    global normal_playing
    global objection_playing
    global desk_playing
    normal_playing = True
    objection_playing = False
    desk_playing = False


if __name__ == '__main__':
    main()

