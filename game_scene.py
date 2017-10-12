# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# Updated by: Roman Beya
# Updated on: 4-Oct-2017
# Updated for: ICS3U
# Updated by: Roman Beya
# Updated on: 11-Oct-2017
# Updated for: ICS3U
# This scene shows the main game.

from scene import *
import ui


class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.center_of_screen = self.size / 2
        self.left_button_down = False
        self.right_button_down = False
        self.ship_move_speed = 20.0
        
        # add background color
        self.background = SpriteNode('./assets/sprites/star_background.PNG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
        spaceship_position = self.center_of_screen
        spaceship_position.y = 100
        self.spaceship = SpriteNode('./assets/sprites/spaceship.PNG',
                                     parent = self,
                                     position = spaceship_position)
                                       
        left_button_position = self.center_of_screen
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                       parent = self,
                                       position = left_button_position,
                                       alpha = 0.5)
                                       
        right_button_position = self.center_of_screen
        right_button_position.x = 300
        right_button_position.y = 100
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5)
                                       
        fire_button_position = self.size
        fire_button_position.x = fire_button_position.x - 100
        fire_button_position.y = 100
        self.fire_button = SpriteNode('./assets/sprites/red_button.PNG',
                                       parent = self,
                                       position = fire_button_position,
                                       alpha = 0.5)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # move spaceship if button down
        if self.left_button_down == True:
            self.spaceship.run_action(Action.move_by(-1*self.ship_move_speed, 0.0, 0.1))
        if self.right_button_down == True:
            self.spaceship.run_action(Action.move_by(self.ship_move_speed, 0.0, 0.1))
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if left or right button is down
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if I removed my finger, then no matter what spaceship
        #    should not be moving any more
        self.left_button_down = False
        self.right_button_down = False
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
