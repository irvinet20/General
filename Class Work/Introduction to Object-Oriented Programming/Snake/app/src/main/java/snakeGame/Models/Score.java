package snakeGame.Models;

public class Score {

    /**
     * This class means to implement the score logic 
     */

    int score;
    int highscore;

    public Score(){
    }

    public int evaluateScore(int applesEaten){
        // the user score ups by 50 points each time food is eaten
        this.score = applesEaten * 50;
        return score;
    }

    public void resetScore() {
        score = 0;
    }

    public int getScore(){ // for testing purposes
        return score;
    }

    public int checkHighScore(int oldscore){ // to evaluate the higher score between previous and current
        if(this.score < oldscore){
            this.highscore = oldscore;
            return oldscore;
        }
        this.highscore = score;
        return this.score;
    }

    public int getHighscore(){ // work in conjunction with controller
        return this.highscore;
    }
}
