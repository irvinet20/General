package snakeGame;

import static org.junit.Assert.*;
import org.junit.*;
import snakeGame.Models.*;

public class testFood {
    /**
     * This test class means to test the Food class
     * The Food class is resposible for creating a Food object that is randomly placed on the board
     * This object can be respawned into a new random position when eaten
     */

    Food test;
    int xCoordinate;
    int yCoordinate;

    public testFood(){
        // Instantiate a Food object with arbritrary board unit size and dimensions
        this.test = new Food(25, 400, 400);
        this.xCoordinate = test.getAppleX();
        this.yCoordinate = test.getAppleY();
    }

     @Test
     public void testSpawn(){
         String errmsg = "Spawned Food object must be within board dimensions";
                 // This test method means to see if the spawned food is within the board dimensions

        assertTrue(errmsg, xCoordinate < 400);
        assertTrue(errmsg, yCoordinate < 400);
        assertTrue(errmsg, xCoordinate >= 0);
        assertTrue(errmsg, yCoordinate >= 0);

        // to see if RESPAWNED food is still within board dimensions

        test.newApple();

        assertTrue(errmsg, xCoordinate < 400);
        assertTrue(errmsg, yCoordinate < 400);
        assertTrue(errmsg, xCoordinate >= 0);
        assertTrue(errmsg, yCoordinate >= 0);
     }

     @Test
     public void testRespawn(){
         String errmsg = "Food object must be randomly coordinated when respawned.";
         // This test method means to see if the respawned food is in a new random location

         test.newApple();

         int new_xCoordinate = test.getAppleX();
         int new_yCoordinate = test.getAppleY();
 
         assertNotEquals(errmsg, xCoordinate, new_xCoordinate);
         assertNotEquals(errmsg, yCoordinate, new_yCoordinate);

         // NOTE: It is still possible for the newly spawned Food object to be randomly coordinated in the same position.
         // This is just highly unlikely
     }
}
