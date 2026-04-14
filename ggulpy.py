# import pygame
# import random
# import asyncio

# pygame.init()

# screen_width = 450
# screen_height = 610
# screen = pygame.display.set_mode((screen_width, screen_height))

# pygame.display.set_caption("Ggulpy Game")
# background = pygame.image.load("background3.jpg")
# background = pygame.transform.scale(background, (450, 610))

# #screen.fill((255,255,255))
# #screen.blit(background, (50,50))

# #clock = pygame.time.Clock()


# character = pygame.image.load("ggulbogpig.png")
# character = pygame.transform.scale(character, (100, 100))
# character_size = character.get_rect().size
# character_width = character_size[0]
# character_height = character_size[1]
# character_x_pos = (screen_width/2) - (character_width/2)
# character_y_pos = screen_height - character_height
# #character_rect = character.get_rect(topleft = (character_x_pos, character_y_pos))
# character_rect = pygame.Rect(character_x_pos+40, character_y_pos+60, character_width-60, character_height-60)

# cloud = pygame.image.load("sun.png")
# cloud = pygame.transform.scale(cloud, (100,100))

# flower = pygame.image.load("rose2.png")
# flower = pygame.transform.scale(flower, (50,100))

# block = pygame.image.load("block.png")
# block = pygame.transform.scale(block, (120,60))

# to_x=0
# to_y=0

# sky_trigger_y = 0
# sky_mode = character_y_pos <= sky_trigger_y


# camera_x = character_x_pos - screen_width//2
# camera_y = character_y_pos - screen_height//2

# screen_x = character_x_pos - camera_x
# screen_y = character_y_pos - camera_y

# draw_x = 0
# draw_y = 0



# #velocity
# y_vel=0

# #background position
# y_pos_bg=0
# x_pos_bg = 0
# game_speed = 10
# screen.blit(background,(x_pos_bg+screen_width,0))


# class Cloud():
#     def __init__(self):
#         self.x = screen_width + random.randint(100,450)
#         self.y = random.randint(100,200)
#         self.image = cloud
#         self.width = self.image.get_width()
#         self.height = self.image.get_height()

#     def update(self):
#         #self.x -= game_speed
#         if self.x < camera_x - self.width:
#             self.x = camera_x + screen_width + random.randint(100,450)
#             self.y = random.randint(50,150)
#     def draw(self):
#         screen.blit(self.image, (self.x - camera_x, self.y - camera_y))


# class Obstacle(Cloud):
#     def __init__(self):
#         self.x = screen_width + random.randint(100,450)
#         self.y=screen_height-100
#         self.image = flower
#         self.width = self.image.get_width()
#         self.height = self.image.get_height()
#         self.rect = self.image.get_rect(topleft = (self.x, self.y))
#         #self.rect = pygame.Rect(self.x+20, self.y+20, self.width-40, self.height-40)

#     def update(self):
#         #self.x -= game_speed
#         self.rect.topleft = (self.x,self.y)
#         #self.rect.x = self.x+20
        
        
#         if self.x < camera_x - self.width:
#             self.x = camera_x + screen_width + random.randint(100,450)
        

#     def draw(self):
#         Cloud.draw(self)


# class Platformer(Obstacle):
#     def __init__(self):
#         self.image = block
#         self.steps = []
#         self.width = self.image.get_width()
#         self.height = self.image.get_height()

#         for i in range(8):
#             x = random.randint(0,screen_width+400)
#             y=random.randint(0,200)
#             rect = self.image.get_rect(topleft = (x, y))
#             self.steps.append(rect)


#     def update(self, sky_mode):
#         for step in self.steps:

#         #  disappear -> new right side one
#             if step.x < camera_x - self.width:
#                 step.x = camera_x + screen_width + random.randint(100, 450)

#                 if sky_mode:
#                 # sky mode
#                     step.y = random.randint(int(camera_y - 300), int(camera_y + screen_height - 100))
#                 else:
#                 # ground mode
#                     step.y = random.randint(0, 500)

#         #  sky mode -> high extension
#             if sky_mode:
#             # below disappear -> new one
#                 if step.y > camera_y + screen_height + 100:
#                     step.x = random.randint(int(camera_x), int(camera_x + screen_width + 200))
#                     step.y = camera_y - random.randint(-100, 300)

#     def draw(self):
#         for step in self.steps:
#             screen.blit(self.image, (step.x-camera_x, step.y-camera_y))



# def menu(death_count):

#     #while running:
#         #screen.fill((255,255,255))
#         font = pygame.font.Font('freesansbold.ttf', 30)

#         if death_count == 0:
#             text = font.render("Press any Key to Start", True, (0,0,0))
#         elif death_count > 0:
#             text = font.render("Press any Key to Start", True, (0,0,0))

#         screen.blit(text, (screen_width//2 - 150,screen_height//2 - 50)) 

#         pygame.display.update()





# async def main():
#     global x_pos_bg, game_speed, y_pos_bg, character_x_pos, character_y_pos, y_vel, camera_x, camera_y, to_x, to_y
#     death_count = 0
#     running = True
#     ground_y=610
#     offset_x = 40
#     offset_y = 60
#     rect_w = character_width - 60
#     rect_h = character_height - 60
#     camera_y=0
#     sky_start = -100
#     sky_end=-300
#     jump_count=0
#     max_jump=2

#     clouds = Cloud()
#     flowers = Obstacle()
#     blocks = Platformer()

#     while running:
#         #clock.tick(60) 
#         await asyncio.sleep(1/60)
        
#         prev_x = character_x_pos
#         prev_y = character_y_pos
        
#         character_x_pos += to_x
#         character_y_pos += y_vel
#         y_vel += 1


#         prev_rect = pygame.Rect(
#             prev_x + offset_x,
#             prev_y + offset_y,
#             rect_w,
#             rect_h
#         )

        
#         character_rect = pygame.Rect(
#             character_x_pos + offset_x,
#             character_y_pos + offset_y,
#             rect_w,
#             rect_h
#         )

#         for step in blocks.steps:
#             if character_rect.colliderect(step):
#                 if y_vel > 0 and prev_rect.bottom <= step.top: #y_vel = 0
#                     character_y_pos = step.y - rect_h - offset_y
#                     y_vel=0
#                     jump_count=0

#                     character_rect = pygame.Rect(
#                         character_x_pos + offset_x,
#                         character_y_pos + offset_y,
#                         rect_w,
#                         rect_h
#                     )
#                     break


#         t = (sky_start - character_y_pos) / (sky_start-sky_end)
#         t=max(0,min(1,t))

#         bg_width = background.get_width()
#         start_x = int(camera_x // bg_width) * bg_width

#         for i in range(3):
#             draw_x = start_x + i * bg_width - camera_x
#             screen.blit(background, (draw_x, 0))


#         sky_overlay = pygame.Surface((screen_width, screen_height))
#         sky_overlay.fill((135,206,255))
#         sky_overlay.set_alpha(int(255*t))

#         screen.blit(sky_overlay,(0,0))
        

         
#         #item, obstacle add
#         clouds.update()
#         clouds.draw()

#         flowers.update()
#         flowers.draw()

#         sky_trigger_y = -150
#         sky_mode = character_y_pos <= sky_trigger_y
#         blocks.update(sky_mode)
#         blocks.draw()

        
        


#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     to_x -= 1
                    
#                 elif event.key == pygame.K_RIGHT:
#                     to_x += 3


#                 elif event.key == pygame.K_SPACE:
#                     if jump_count < max_jump:
#                         y_vel = -20
#                         jump_count+=1
                    

#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     to_x =0
#                 elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                     to_y=0




#         if character_rect.colliderect(flowers.rect):
#             pygame.draw.rect(screen, (255,0,0), character_rect, 2)
#             pygame.draw.rect(screen, (0,255,0), flowers.rect, 2)
#             #pygame.time.delay(1000)
#             await asyncio.sleep(1)
            
        
#             death_count += 1
#             menu(death_count)
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 if event.type == pygame.KEYDOWN:
#                     main()
            


#         if not sky_mode:
#             if character_rect.bottom >= ground_y and y_vel > 0:
#                 character_y_pos = ground_y - rect_h - offset_y
#                 y_vel = 0
#                 jump_count=0

#         #camera move
#         camera_x = character_x_pos - screen_width//2




#         if sky_mode:
#             top_margin = 100
#             screen_y = character_y_pos - camera_y
#             if screen_y < top_margin:
#                 camera_y = character_y_pos - top_margin
#                 screen_y = top_margin

#         else:
#             camera_y=0
        
    


#         draw_x = character_x_pos - camera_x
#         draw_y = character_y_pos - camera_y
       
#         screen.blit(character, (draw_x, draw_y))

#         #screen.blit(character, (character_x_pos, character_y_pos))
#         pygame.display.update()
#         #await asyncio.sleep(0)

#     pygame.quit()



# #main()
# asyncio.run(main())
# # if __name__ == "__main__":
# #     import asyncio
# #     asyncio.run(main())

import pygame
import asyncio

pygame.init()

async def main():
    screen = pygame.display.set_mode((450, 610))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255,0,0))
        pygame.display.update()

        await asyncio.sleep(1/60)

import asyncio
asyncio.run(main())