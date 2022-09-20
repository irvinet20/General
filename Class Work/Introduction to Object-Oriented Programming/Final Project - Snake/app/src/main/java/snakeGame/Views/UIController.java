package snakeGame.Views;

public class UIController
{
    SnakeGUI ui;
    boolean difficulty = true;

    public UIController(SnakeGUI ui)
    {
        this.ui = ui;
    }

    public void play(){ // based upon use case 1, playing the game
        ui.setVisible(false);
        new GameFrame(difficulty, 0);
    }

    public void setDifficulty(boolean easy){
        this.difficulty = easy;
    }

}



 
