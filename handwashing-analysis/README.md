# handwashing-analysis
An EDA of the history of handwashing in Jupyter Notebook

With the Covid-19 pandemic ravaging the planet, governments have been reminding the general public to wash their hands, don't touch their face, wear a facemask, and stay at home. It is only natural for one to be curious and have a think about when did handwashing became a thing, and who discovered its importance. In this EDA, we will dive right into data that was at the disposal of Dr. Ignaz Semmelweis, the person who highlighted the gravity of handwashing (spoiler alert: he was not appreciated!).

In this exploration, we are able to answer questions like:
- How significant was the change between pre-handwashing era and post-handwashing era?
- What is the 90% confidence interval of the mean of difference between these eras?

<!--[image](/plots/figure2.png?raw=true)-->

<img src="https://github.com/salfaris/data-analysis/blob/master/handwashing-analysis/plots/figure2.png" alt="image" width="695" height="500">

We will not use a ready-made dataset from Kaggle or somewhere online. Instead, we will scrape the data from <a href='https://en.wikipedia.org/wiki/Historical_mortality_rates_of_puerperal_fever'>Historical mortality rates of puerperal fever</a>. For the usage of future enthusiastic data analysts, the scraped and cleaned data is saved as a csv file and is accesible within the `dataset` folder.

This EDA is inspired by Rasmus Bååth's tutorial project on DataCamp. The major difference is I scraped the data myself from Wikipedia instead of relying on the provided already-cleaned data and extended the original project to analyze further events such as the strict control enforcement. Some idea of the analysis, however, is unoriginal and are derived from Bååth's work.
