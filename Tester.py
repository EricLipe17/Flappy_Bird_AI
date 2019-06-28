import FlappyBird

game = FlappyBird.FlappyBird(fps=60)

game.run()


# import pygame as pg
# import Pipe
#
# pg.init()
# win = pg.display.set_mode((800, 600))
#
# test = True
# pipes = list()
# pipes.append(Pipe.Pipe(win, 200))
# count = 0
#
# while test:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             test = False
#
#     win.fill((135, 206, 235))
#     if (count / 500).is_integer():
#         pipes.append(Pipe.Pipe(win, 180))
#     for pipe in pipes:
#         if pipe.off_screen():
#             pipes.remove(pipe)
#         pipe.show()
#         pipe.update()
#     count += 1
#     pg.display.update()
# pg.quit()


