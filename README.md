# Spam_Ham_Classifier

Certainly, here are the step-by-step instructions for setting up and running the application using a virtual environment for Python 3.9:

1. **Setup Virtual Environment**:
   - Open the terminal.
   - Install the virtual environment package if you haven't already: `conda create -p venv python=3.9 -y`.
   - Create a virtual environment: `virtualenv venv`.
   - Activate the virtual environment:
     ```bash
     conda activate venv/
     ```

2. **Install Requirements**:
   - Install the requirements: `pip install -r requirements.txt`.

3. **Set Up the Jupyter Notebook**:
   - Open the Jupyter Notebook in your virtual environment.
   - Install the necessary packages:
     ```bash
     pip install ipykernel
     pip install jupyter notebook
     ```

4. **Run Application.py**:
   - Run the application: `python app.py`.

5. **Download NLTK Resources**:
   - Ensure the required NLTK resources are downloaded:
     ```python
     import nltk
     nltk.download('punkt')
     nltk.download('stopwords')
     ```

By following these steps, you can set up a virtual environment, install necessary requirements, and run the `app.py` script in the Jupyter Notebook environment. This process ensures a clean and isolated development environment for your application.

## Enjoy the Code!
