# willyshakes
William Shakespeare GPT
# willyshakes
William Shakespeare GPT
# SceneCoach AI

SceneCoach AI aims to democratize acting education with a focus on the works of William Shakespeare. This repository contains a small prototype for a Shakespeare themed quiz game that can be used as the basis for a mobile learning application.

The included `game.py` script demonstrates a lightweight command line interface that quizzes the player on which character speaks a given line. It is intended as a starting point for a gamified learning experience that can eventually be integrated into a full mobile app.

## Running the quiz

Make sure you have Python 3.11+ installed. Run the script directly:

```bash
python -m scenecoach.game
```

You will be presented with lines from Shakespeare and asked to select the correct speaker. The script keeps score over five rounds.

## Iambic Pentameter Lesson

To try a short lesson on speaking iambic pentameter, run:

```bash
python -m scenecoach.lesson
```

The program will explain the basics of iambic pentameter and prompt you to repeat a few famous lines. If a microphone is available it will briefly record your response; otherwise you can simply type the line and press Enter.

The lesson uses example lines from the [scenecoachai/shakespeare](https://huggingface.co/datasets/scenecoachai/shakespeare) dataset.

## Extending this project

This repository is an early prototype. Future versions could include:

- A larger dataset of plays and sonnets
- Speech recognition to practice speaking lines aloud
- A mobile UI built with your framework of choice (React Native, Flutter, etc.)
- Progress tracking and leaderboards to keep the experience fun and engaging

Pull requests are welcome!
