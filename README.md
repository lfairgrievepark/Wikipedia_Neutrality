# Wikipedia_Neutrality
This is a python project that allows for automated differentition between "flagged" and "unflagged" wikipedia articles. This is achieved by training a naive bayes model on articles that have been tagged by wikipedia editors in some way ("POV", "Autobiographical" etc.) and articles randomly chosen either from all of wikipedia or a specific section ("Living Person" etc.). This code could likely be improved by experimenting with different machine learning models for classification. The naive bayes model is simple but fast and is an effective proof of concept.

The main script for doing this is Wikitest.py and contains all the functions used for gathering the links, scraping the articles for text, training and exporting the model and charcterizing other articles using that model.

wikiscrape.py is taken from https://github.com/kohjiaxuan/Wikipedia-Article-Scraper and is used for article scraping purposes. Many thanks to its creator.

WikiNotebook.ipynb contains some early testing of the functions found in Wikitest.py and different attempts at machine learning models.

