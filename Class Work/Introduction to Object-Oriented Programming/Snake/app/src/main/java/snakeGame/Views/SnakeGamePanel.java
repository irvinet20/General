package snakeGame.Views;

import snakeGame.Controllers.SnakeController;
import snakeGame.Models.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class SnakeGamePanel extends JPanel implements ActionListener{


	/**
	 * This class implements the graphics of the gameplay and uses the controller to implement gameplay function
	 */
    
    static int SCREEN_WIDTH = 600;
	static int SCREEN_HEIGHT = 600;
	static int UNIT_SIZE = 25;
	static int DELAY;
    // Initialize the game board dimensions:
    // Grid board, with squares separated by UNIT_SIZE
    // Timer delay is 125 (higher means slower gameplay)


    boolean running = false;
    Timer timer;
    // initialize timer and running boolean
	int previousscore;
    Snake snakey;
    Food apple;
    Score score;
	SnakeController control;
    // create snake, food, score, and controller

    public SnakeGamePanel(boolean difficulty, SnakeController control, int previousscore){

		this.setPreferredSize(new Dimension(SCREEN_WIDTH,SCREEN_HEIGHT));
		this.setBackground(Color.black);
		// create background

		this.previousscore = previousscore;
        snakey = new Snake(UNIT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT);
        apple = new Food(UNIT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT);
		// create snake and apple

		this.control = control;
		this.control.addFood(apple);
		this.control.addSnake(snakey);;

		// initialize controller as passed in, add the snake/apple

		DELAY = control.setSpeed(difficulty);
		// set snake speed based on home panel input


		startGame(); // begin game on instantiation
	}

    public void startGame() { // to start game, begin timer and spawn food
		control.spawnFood();
		running = true;
		timer = new Timer(DELAY, this);
		timer.start();
	}

    public void paintComponent(Graphics g) {
		super.paintComponent(g);
		draw(g);
	}

	public void draw(Graphics g) { //this runs at each repaint call
		
		if(running) {
			
			for(int i=0;i<SCREEN_HEIGHT/UNIT_SIZE;i++) { // This is the grid system, can change color, etc.
                g.setColor(Color.ORANGE);
				g.drawLine(i*UNIT_SIZE, 0, i*UNIT_SIZE, SCREEN_HEIGHT);
				g.drawLine(0, i*UNIT_SIZE, SCREEN_WIDTH, i*UNIT_SIZE);
			}
			
			g.setColor(Color.red); // set food graphical implementation
			g.fillOval(apple.getAppleX(), apple.getAppleY(), UNIT_SIZE, UNIT_SIZE);
		
			for(int i = 0; i< snakey.getBodyParts();i++) { //this draws the snake
				if(i == 0) {
					g.setColor(Color.green);
					g.fillRect(snakey.getPositionX(i), snakey.getPositionY(i), UNIT_SIZE, UNIT_SIZE);
				}
				else {
					g.setColor(new Color(45,180,0));
					//g.setColor(new Color(random.nextInt(255),random.nextInt(255),random.nextInt(255)));
					g.fillRect(snakey.getPositionX(i), snakey.getPositionY(i), UNIT_SIZE, UNIT_SIZE);
				}			
			}
		}
		else { // if the game is no longer running, gameOver is called. 
			gameOver(g);
		}
    }

    @Override
	public void actionPerformed(ActionEvent e) {
		// This is continually called, if running it will use the controller to create gameplay
		
		if(running) {
			boolean stop = control.play(running);
            if(stop){ // gameplay ends when a collision occurs
                timer.stop();
				running = false;
            }
		}
		repaint(); // redraw
	}

    public void gameOver(Graphics g) {
		this.setVisible(false);
		SnakePlayAgainPanel newPlayPanel = new SnakePlayAgainPanel(control, previousscore);
		// make play again panel and send in previous score to be evaluated 

		newPlayPanel.addPlayAgainListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
				new GameFrame(control.getDifficulty(), control.getSnakeHighscore());
            }
         });

		score.resetScore();
	}
}
