# Kimaris

Kimaris is a tool that aids in the selection, visualization, and analysis of primarystudies for systematic reviews.  By web scraping Google Scholar, we were ableto attain an algorithm that automatically does the snowballing forward step forany given search on the website. With this result, the user finds primary studiesand the papers that cited those papers (and so forth).  It can go as many stepsforward as wanted (although the number of nodes cannot surpass eight thousand, restricting the search).  

The system displays the results in a 3D networkgraph, which shows all searched elements by the size of citations and connections of citations.  By clicking on a node, it filters and displays the connectionsof that node.  Users can enter a node, being able to see all information about theelement.  When the user selects the node, there is an option to upload the PDFfrom that node.  

We implemented and integrated an NLP-powered system thatextracts the text from any PDF and gives some information about it (i.e., Mostcommon words, bigrams, and trigrams, Summarization of text, Topic Modeling,and others).  The NLP module is also suitable for books, or any PDF formatted document, although our focus was on scientific papers.  By uploading a pdf, theuser can read the pdf on the tool,  read a summary of the PDF text,  see the topics the text talks about, and visualize NLP information.  

We conducted a use case with Kimaris to display its benefits inside a systematic review.  The graphvisualization allows the user to rapidly see which studies are the most cited and connected (thus, probably the most relevant) for it in the review.  By providing summarizations of the PDF and topic modeling, the user can dynamically read and decide faster if the study is suitable for its review.  NLP information enables a fast understanding of the study’s focus.  The tool’s main benefit is theautomatic forward steps on Google Scholar and its visualization; the NLP part of the system permits the user to make more well-informed decisions.

## Contribuiting ##

### Setup the development environment ###

The Python version using on development is 3.7.6. We strongly recommend using the pyenv virtualenv to create the development environment.

Besides all application is developed on Python, there are some additional modules like *language-check* requires your computer has the *LanguageTool* and *Java 1.8 JDK* installed. Newer versions does not work due a version check on language-check install module. *Make sure you have Java 1.8 installed before proceeding with steps below.*


If you are not familiar with pyenv or either don't have it installed, take a look here.

1. Make sure that you have the Python 3.7.6 version install on your computer. If you don't have it, you can use the pyenv to install it:

```
pyenv install 3.7.6
```

2. After the Python is installed, you can create the virtual environment for the project, using:

```
pyenv virtualenv 3.7.6 kimaris
```

3. After the virtual environment is created, you will use the following to activate it:

```
pyenv activate kimaris
```

4. Now you can install the project dependencies with the following:

```
pip install -r requirements.txt
```
