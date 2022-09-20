package snakeGame;

import snakeGame.Views.SnakeGUI;
import snakeGame.Views.UIController;

import java.awt.event.*;

public class SnakeGame{
    public static void main(String[] args){

        SnakeGUI ui = new SnakeGUI();
        UIController controller = new UIController(ui);

        ui.addPlayListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
               controller.play();
            }
         });

         ui.addEasyListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
               controller.setDifficulty(false);
            }
         });

         ui.addHardListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
                controller.setDifficulty(true);
            }
         });
    }
}
