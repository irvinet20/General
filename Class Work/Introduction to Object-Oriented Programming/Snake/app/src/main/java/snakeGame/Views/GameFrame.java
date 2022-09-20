package snakeGame.Views;

import javax.swing.JFrame;

import snakeGame.Controllers.SnakeController;

public class GameFrame extends JFrame{
    
    public GameFrame(boolean difficulty, int previouscsore){

        SnakeController control = new SnakeController();

        this.add(new SnakeGamePanel(difficulty, control, previouscsore));
        // add a GamePanel JPanel to the GameFrame JFrame

        this.addKeyListener(control);
        // add controller keylistener to the gameframe

        this.setTitle("Snake!");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack();
        this.setVisible(true);
        // Create JFrame of our game


    }
}
