package snakeGame.Controllers;
import java.awt.event.*;

// Model Imports
import snakeGame.Models.Food;
import snakeGame.Models.Snake;
import snakeGame.Models.Score;

public class SnakeController implements KeyListener{

    Snake snakey;
	Food apple;
	Score myScore = new Score();
	boolean difficulty = false;
	// Initialize snake, food, score

    public SnakeController(){
    }

	public void addSnake(Snake snake){ // add specific snake
		this.snakey = snake;
	}
	public void addFood(Food apple){ // add specific food
		this.apple = apple;
	}

	public char getSnakeDirection(){ // return snake direction
		return snakey.getDirection();
	}

	/**
	 * These next four methods are used simply for gameplay progression
	 * Essentially the views use these to pass on elements like highscore and difficulty levels
	 */

	public boolean getDifficulty(){
		return difficulty;
	}

	public int getSnakeHighscore(){
		return this.myScore.getHighscore();
	}

	public int checkNewHighScore(int previous){
		return this.myScore.checkHighScore(previous);
	}

	public int setSpeed(boolean difficulty){ // Game initial speed
		this.difficulty = difficulty;
		if(difficulty){
			return 110;
		}
		return 150;
	}

	/**
	 * These methods are used in-game 
	 *
	 */

	public boolean play(boolean running){ // game play
		snakey.move(); //move the snake
		boolean spawn = snakey.checkApple(apple.getAppleX(), apple.getAppleY()); // check if snake eats food
		if(spawn){ // if snake is on same place as food, create a new position
			apple.newApple();
		}
		boolean stopTimer = snakey.checkCollisions(running); // if snake collides, return boolean 
		return stopTimer;
	}

	public void spawnFood(){ // controller call to food to respawn
		apple.newApple();
	}

	public int getScore(){ // controller call to score to evaluate final score
		int ret = myScore.evaluateScore(snakey.getApplesEaten());
		return ret;
	}

	/**
	 * KeyListener Implementations
	 */

    @Override
    public void keyTyped(KeyEvent e) {}

    @Override
    public void keyPressed(KeyEvent e) {
        switch(e.getKeyCode()) {
			case KeyEvent.VK_LEFT:
				if(snakey.getDirection() != 'R') {
					snakey.setDirection('L');
				}
				break;
			case KeyEvent.VK_RIGHT:
				if(snakey.getDirection() != 'L') {
					snakey.setDirection('R');
				}
				break;
			case KeyEvent.VK_UP:
				if(snakey.getDirection() != 'D') {
					snakey.setDirection('U');
				}
				break;
			case KeyEvent.VK_DOWN:
				if(snakey.getDirection() != 'U') {
					snakey.setDirection('D');;
				}
				break;
			}
        
    	}

    @Override
    public void keyReleased(KeyEvent e) {}
    
}
