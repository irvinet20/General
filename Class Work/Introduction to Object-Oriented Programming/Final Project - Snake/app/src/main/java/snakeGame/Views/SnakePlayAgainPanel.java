package snakeGame.Views;

import javax.swing.*;

import snakeGame.Controllers.SnakeController;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.*;
import java.awt.event.*;

public class SnakePlayAgainPanel
{
    /**
     * This class is displayed after the game is finished, offering to play again and displaying the previous score and highscore
     */

    public static int frameSize = 300;

    private JButton playAgain;
    private JLabel score;
    private JFrame mainFrame;

    public SnakePlayAgainPanel(SnakeController controller, int previous){

        //Top level container
        mainFrame = new JFrame("Snake!");
        mainFrame.setPreferredSize(new Dimension(frameSize*2, frameSize-15));
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Top level panel
        JPanel snakeUI = new JPanel();
        snakeUI.setLayout(new BoxLayout(snakeUI, BoxLayout.Y_AXIS));

        //Panel for play again button and score
        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new BorderLayout());
        
        playAgain = new JButton("Play Again");
        score = new JLabel();

        playAgain.setBackground(Color.BLACK);
        playAgain.setForeground(Color.GRAY); 

        score.setText("Game Over! Your score: " + controller.getScore() + " Highscore: " + controller.checkNewHighScore(previous));
        score.setFont(new Font("Serif", Font.BOLD, 30));
        
        score.setHorizontalAlignment(JLabel.CENTER);
        controlPanel.add(score, BorderLayout.NORTH);
        controlPanel.add(playAgain, BorderLayout.CENTER);
        snakeUI.add(controlPanel);

        mainFrame.add(snakeUI);
        mainFrame.pack();
        mainFrame.setVisible(true);
    }
    public void addPlayAgainListener(ActionListener actionListener)
    {
       playAgain.addActionListener(actionListener);
    }

}

