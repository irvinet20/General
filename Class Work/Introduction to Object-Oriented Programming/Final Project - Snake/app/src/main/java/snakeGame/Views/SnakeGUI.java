package snakeGame.Views;

import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.*;
import java.awt.event.ActionListener;


public class SnakeGUI extends JPanel{
       /**
    * This class is the home panel for the game. It prompts the user with difficulty options and to play (easy is default)
    */
    public static int frameSize = 425;

    private JButton   easy;
    private JButton   hard;
    private JButton   play;
    private JLabel description;
    private JFrame    mainFrame;
    JPanel snakeUI = new JPanel();

    final static boolean shouldFill = true;
    final static boolean shouldWeightX = true;
    final static boolean RIGHT_TO_LEFT = false;

    public SnakeGUI(){

        // top level container for the game
        mainFrame = new JFrame("Snake!");
        mainFrame.setPreferredSize(new Dimension(frameSize*2, frameSize-15));
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //mainFrame.setContentPane(new JLabel(new ImageIcon("snake.jpg")));

        // panel for difficulty buttons and play button, as well as game description/rules
        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();
	    if (shouldFill) {
	    //natural height, maximum width
	    c.fill = GridBagConstraints.HORIZONTAL;
	    }
        easy = new JButton("Easy");
        hard = new JButton("Hard");
        play = new JButton("Play");
        description = new JLabel();
        JLabel background =new JLabel(new ImageIcon("snake.jpg"));
        description.add(background, CENTER_ALIGNMENT);

        easy.setBackground(Color.BLACK);
        easy.setForeground(Color.GRAY); 
        hard.setBackground(Color.BLACK);
        hard.setForeground(Color.GRAY); 
        play.setBackground(Color.BLACK);
        play.setForeground(Color.GRAY); 

        description.setText("<html>How to Play:" + "<br/>" + "<br/>" + 
        "1. Use your arrow keys to move" +  "<br/>" +
        "2. Eat food to get bigger and increase score" + "<br/>" +
        "3. Don't touch the walls or yourself or you LOSE</html>");
        description.setFont(new Font("Serif", Font.BOLD, 17));

        // Add description
        c.fill = GridBagConstraints.HORIZONTAL;
	    c.weightx = 0.5;
	    c.gridx = 1;
	    c.gridy = 0;
        controlPanel.add(description, c);

        // Add easy button
        if (shouldWeightX) {
            c.weightx = 0.5;
            }
        c.fill = GridBagConstraints.WEST;
        c.ipadx = 150;
        c.ipady = 150;
        c.gridx = 0;
        c.gridy = 0;
        controlPanel.add(easy, c);
        
        // Add hard button
        c.fill = GridBagConstraints.EAST;
	    c.weightx = 0.5;
        c.ipadx = 150;
        c.ipady = 150;
	    c.gridx = 2;
	    c.gridy = 0;
        controlPanel.add(hard, c);

        // Add play button
        c.fill = GridBagConstraints.HORIZONTAL;
	    c.ipady = 150;      //make this component tall
	    c.weightx = 0.0;
	    c.gridwidth = 3;
	    c.gridx = 0;
	    c.gridy = 1;
        controlPanel.add(play, c);

        snakeUI.add(controlPanel);

        addComponentsToPane(mainFrame.getContentPane());

        mainFrame.add(snakeUI);
        mainFrame.pack();
        mainFrame.setVisible(true);
    }


    public static void addComponentsToPane(Container controlpanel) {
        if (RIGHT_TO_LEFT) {
            controlpanel.setComponentOrientation(ComponentOrientation.RIGHT_TO_LEFT);
        }
    }

    public void addPlayListener(ActionListener actionListener)
    {
       play.addActionListener(actionListener);
    }
 
    public void addEasyListener(ActionListener l)
    {
       easy.addActionListener(l);
    }
 
    public void addHardListener(ActionListener l)
    {
       hard.addActionListener(l);
    }
}
