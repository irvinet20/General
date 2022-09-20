package snakeGame.Models;

public class Snake {

    /**
     * This class contains the position and logic of movement of the snake as well as gameplay rules (apple eating)
     */

    int bodyParts = 6; // number of points/bodily units of snake (what keeps track of size/score)
    int boardSize; // board unit length
    int boardDimensionX; // board width
    int boardDimensionY; //board height
    int applesEaten; 
	char direction = 'R';
	int units;
	int x[];
	int y[];

    public Snake(int boardSize, int boardDimensionX, int boardDimensionY){
        // pass in board unit size and board dimensions
        this.boardSize = boardSize;
        this.boardDimensionX = boardDimensionX;
        this.boardDimensionY = boardDimensionY;
		this.units = boardDimensionX*boardDimensionY/(boardSize*boardSize);
		this.x = new int[units];
		this.y = new int[units];
    }

	public char getDirection(){ // return snake direction
		return direction;
	}

	public void setDirection(char newdirection){ // set new snake direction
		this.direction = newdirection;
	}

    public void move(){ // move snake

		for(int i = bodyParts;i>0;i--) { //move snake by bodyPart to next block
			x[i] = x[i-1];
			y[i] = y[i-1];
		}
		
		switch(direction) { // switch statement to determine the new head position per turn
			case 'U':
				y[0] = y[0] - boardSize;
				break;
			case 'D':
				y[0] = y[0] + boardSize;
				break;
			case 'L':
				x[0] = x[0] - boardSize;
				break;
			case 'R':
				x[0] = x[0] + boardSize;
				break;
			}	
	}

    public boolean checkCollisions(boolean running) {
		//checks if head collides with body
        boolean stopTimer = false;;

		for(int i = bodyParts;i>0;i--) {
			if((x[0] == x[i])&& (y[0] == y[i])) {
				running = false;
			}
		}
		//check if head touches left border
		if(x[0] < 0) {
			running = false;
		}
		//check if head touches right border
		if(x[0] > boardDimensionX) {
			running = false;
		}
		//check if head touches top border
		if(y[0] < 0) {
			running = false;
		}
		//check if head touches bottom border
		if(y[0] > boardDimensionY) {
			running = false;
		}
		
		if(!running) {
			stopTimer = true;
		}
        return stopTimer;
	}

    public boolean checkApple(int appleX, int appleY) { // check if head position is the same as passed in apple coordinates
        boolean newApple = false;
		if((x[0] == appleX) && (y[0] == appleY)) { // if it is, increase apples and bodyparts, and set boolean to respawn apple
			bodyParts++;
			applesEaten++;
            newApple = true;
		}
        return newApple;
	}

    public int getApplesEaten(){ // for score purposes
        return applesEaten;
    }

    public int getBodyParts(){ // for drawing purposes
        return bodyParts;
    }

    public int getPositionX(int index){ // return x coordinate of given index 
        return x[index];
    }

    public int getPositionY(int index){ // return y coordinates of given index
        return y[index];
    }


}
