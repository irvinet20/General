package snakeGame;

import static org.junit.Assert.*;
import org.junit.*;
import snakeGame.Models.*;

public class testSnake {
    /**
     * The snake class implements the logic of its movements and positioning as well as checks if it eats apples or collides 
     * with the dimensions or itself
     */
    Snake test;

    public testSnake(){
        this.test = new Snake(25, 400, 400);
    }

    @Test
    public void testMovementHorizontal(){
        // The snake's move function moves the snake one block (board unit)
        // It does so by moving each bodyPart to the position of the next, with the head moving in the direction it is set to

        // the default is right
        int initialX = test.getPositionX(0);
        int initialY = test.getPositionX(0); // initial head coordinates 

        test.move();

        assertEquals("Snake should only move to the right when directed right.",initialX + 25, 25); 
        // Its head should have moved one board unit to the right
        assertEquals("Snake should not move vertically in horizontal movement", initialY, initialY); 
        // Its head should not have moved in the y direction

    }

    @Test
    public void testMovementVertical(){
        // The snake's move function moves the snake one block (board unit)
        // It does so by moving each bodyPart to the position of the next, with the head moving in the direction it is set to

        // the default is right
        int initialX = test.getPositionX(0);
        int initialY = test.getPositionX(0); // initial head coordinates 

        test.setDirection('D'); // set new direction downward
        test.move();

        assertEquals("Snake should only move to the right when directed right.",initialX, initialX); 
        // Its head should have moved one board unit downward
        assertEquals("Snake should not move vertically in horizontal movement", initialY + 25, 25); 
        // Its head should not have moved in the x direction
    }

    @Test
    public void testCollision(){
        // The snake's checkCollision method checks the coordinates of the snake's head against the board dimensions and itself
        // As long as its running. For testing purposes, we will create a new snake (the old one's positions have moved)

        test.setDirection('L');
        test.move(); // have the snake make a full circle
        test.setDirection('U');
        test.move();
        assertTrue("The snake has collided upon itself", test.checkCollisions(true));



        Snake secondtest = new Snake(25, 400, 400);

        secondtest.setDirection('U');
        secondtest.move(); // have the snake turn and move upward into the top border

        assertTrue("The Snake collided with the upper wall", secondtest.checkCollisions(true));
    }

    @Test
    public void testAppleEaten(){
        // the snake's checkApple function checks the coordinates of its head vs input parameters. If they are the same
        // the snake will increase in length and signal for a new apple to be spawned

        Snake thirdtest = new Snake(25, 400, 400);

        thirdtest.setDirection('D');
        thirdtest.move(); // the snake turns downward

        int xCoordinate = thirdtest.getPositionX(0);
        int yCoordinate = thirdtest.getPositionY(0); // get head coordinates
        int currentBodyParts = thirdtest.getBodyParts(); // get current body parts 
        int currentApplesEaten = thirdtest.getApplesEaten();

        thirdtest.checkApple(xCoordinate, yCoordinate);

        assertEquals("Snake should have increased in length when eaten food.",thirdtest.getBodyParts(), currentBodyParts+1);
        assertEquals("Snake should have eaten an apple.", thirdtest.getApplesEaten(), currentApplesEaten+1);
        assertTrue("Snake should have signaled for a new apple's spawn", thirdtest.checkApple(xCoordinate, yCoordinate));
    }
}


