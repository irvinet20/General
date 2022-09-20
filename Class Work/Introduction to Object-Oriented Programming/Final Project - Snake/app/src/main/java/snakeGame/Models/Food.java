package snakeGame.Models;

import java.util.Random;

public class Food {

    /**
     * This class contains the food positioning as well as random food placement logic
     */
    
    int appleX;
	int appleY;
    Random random = new Random();
    int boardSize; // board unit length
    int boardDimensionX; // board width
    int boardDimensionY; //board height

    public Food(int boardSize, int boardDimensionX, int boardDimensionY){
        // pass in board unit size, and dimensions
        this.boardSize = boardSize;
        this.boardDimensionX = boardDimensionX;
        this.boardDimensionY = boardDimensionY;
    }

    public void newApple(){ // Create new position randomly for apple
		appleX = random.nextInt((int)(boardDimensionX/boardSize))*boardSize;
		appleY = random.nextInt((int)(boardDimensionY/boardSize))*boardSize;
	}

    public int getAppleX(){ // return apple x coordinate
        return appleX;
    }

    public int getAppleY(){ // return apple y coordinate
        return appleY;
    }

}
