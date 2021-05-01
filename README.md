

# Chess Game Result Prediction

Entertainment is a feature of human behaviour since the earliest of times, countless games
and other forms of entertainment have been devised over the centuries, one of the earliest
games recorded in relatively recent human history that it is still played worldwide is Chess, or
Checkers. As in any other competitive task, humans have been looking for an advantage in competitive
chess, for this any tool available to humans were used to try to obtain knowledge, mechanics and
mathematics were used to ”beat” chess from the earliest of times.

# Motivation

According to IBM’s Shanon , there are around 1043 possible number of board positions,
which is a lower bound estimate, thus making it almost impossible to solve the problem using
brute force, and also it explain the complexity of chess itself, we think it might be possible
that the hardware of modern computers has improved enough to provide a somewhat accurate
prediction, using advanced machine learning techniques, and database technology, using our
personal computers. <br><br> Magnus Carlsen is a Norwegian chess player who faced world chess champion Viswanathan Anand (India) 
and won the World Chess Championship in 2013 , becoming the second youngest world chess champion at age 22.

# [ Dataset ](https://www.kaggle.com/datasnaek/chess)
This is a set of just over 20,000 games collected from a selection of users on the site Lichess.org.

### [Attributes information:]()

* **white_rating** - strength of a player based on their performance versus other players.
* **black_rating** - strength of a player based on their performance versus other players.
* **opening_name** -  initial moves of a chess game.


### [Experiment Results:]()

 * **Performance Evaluation**
    * Splitting the dataset by 67 % for training set and 33 % validation set.
 * **Training and Validation**
    * Logistic Regression with MinMaxScalar gets a higher accuracy score than other classification models.
    * Logistic Regression ( 99 % accuracy score )
 * **Performance Results**
    * Training Score: 61.5%
    * Validation Score: 63.1%

 
# Demo
## Live Demo: https://chess-game-result-prediction.herokuapp.com/

![](https://github.com/SahilSK202/Chess-Game-Result-Prediction/blob/main/static/images/chessapp1.png)
![](https://github.com/SahilSK202/Chess-Game-Result-Prediction/blob/main/static/images/chessapp2.png)

## Further Improvements
There are lot of things to improve upon

- Frontend can be made more nicer 
- Need to improve responsiveness for mobile
- Learning Neural Nets will try to apply soon
- More data => More Accuracy => More Reliable
