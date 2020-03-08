
**Introduction :-**

	In project, i am going to build a chatbot using deep learning techniques. The chatbot will be trained on the dataset which contains categories (intents), pattern and responses. We use a special recurrent neural network (LSTM) to classify which category the user’s message belongs to and then we will give a random response from the list of responses.

**Prerequisites :-** 

	pip install tensorflow, keras, pickle, nltk

**Files Details :-**

	Now we are going to build the chatbot using Python but first, let us see the file structure and the type of files we will be creating:

	intents.json :- The data file which has predefined patterns and responses.
	train_model.py :- In this Python file, we wrote a script to build the model and train our chatbot.
	Words.pkl :- This is a pickle file in which we store the words Python object that contains a list of our vocabulary.
	Classes.pkl :- The classes pickle file contains the list of categories.
	Chatbot_model.h5 :- This is the trained model that contains information about the model and has weights of the neurons.
	helper_function :- This is the Python script in which have helper function for chatbot GUI. For first time then uncomment these download.
	                   #nltk.download('punkt')
                       #nltk.download('wordnet')
                       
 
	chatbot_app.py :- This is the Python script in which we implemented GUI for our chatbot. Users can easily interact with the bot.
	
**Here are the 5 steps to create a chatbot in Python from scratch :-**

	Import and load the data file
	Preprocess data
	Create training and testing data
	Build the model
	Predict the response	# Chatbot-Neural-Network 
# Chatbot-Neural-Network
