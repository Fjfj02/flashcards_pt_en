# Flashcards (Brazilian Portuguese - English)

Flashcards is an app based on one of the courses I took. This one, in particular, is used to train the Portuguese-English variation.

The original was in French-English and had fewer words. The words were removed according to the number of frequencies used in the language, and can be found on the following GitHub:

https://github.com/hermitdave/FrequencyWords


This app works as follows:

A word appears in Portuguese, and after a few seconds, it appears in English.

So, you mark whether you knew the word or not, and this data is stored in the words_to_learn.csv file in the data folder. Follow the images:

![image](https://github.com/Fjfj02/flashcards_pt_en/assets/84993558/792aca77-1177-4fab-913e-0dafa3bd3d69)

![image](https://github.com/Fjfj02/flashcards_pt_en/assets/84993558/58d775b7-0528-4ed1-8441-6527b78283cd)

The interface may be crooked if it is not running on Windows.

## Run code

First you have to install the following library:

```shell
pip install pandas
```

To run the code, use:

```shell
python3 main.py
```

## Change of data and progress

If you want to change the style or number of flashcards, you can change the brazilianportuguese_words.csv file in the data folder.

Also, if you want to delete your progress, you can just delete the words_to_learn.csv file in the data folder.
