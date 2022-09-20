package snakeGame;

import static org.junit.Assert.*;
import org.junit.*;
import snakeGame.Models.*;

public class testScore {
    /**
     * This test class means to test the Score class
     * The Score class is used to evaluate the current score based upon how many apples are eaten and reset that score per game
     */
    Score test;

     public testScore(){
        test = new Score();
     }

     @Test
     public void testEvaluate(){
        // evaluateScore means to take a number of apples eaten and multiply it by 50 for the score

        assertEquals(500, test.evaluateScore(10));
        assertEquals(1250, test.evaluateScore(25));
     }

     @Test
     public void testReset(){
         // resetScore means to reset the score object's score per game

         test.evaluateScore(5); // set's score to 250

         test.resetScore();

         assertEquals(test.getScore(), 0);
     }
}
