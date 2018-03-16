# Markov-Chains-and-Twitter WIP

Tweet random words from your favorite book.  Pretty neat! I did Pride and Prejudice. 



![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/PrideandPrejudicetweet.png)





```
git clone https://github.com/GraceDurham/Markov-Chains-and-Twitter.git
cd Markov-Chains-and-Twitter
```

![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/TwittterInstructions.png)

### Create Keys and Access Tokens for Twitter API

![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/CreateKeysandAccessTokens.png)

![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/CreatingYour%20SecretsFile.png)

```
Secrets file is not provided in terminal please create a file called secrets.sh by doing touch secrets.sh
```


![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/sourcesecrets.sh_instructions.png)

### Create .gitignore file and add secrets.sh to it 

![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/Create%20.gitignore%20file%20and%20add%20secrets.sh%20to%20it.png)

#### Create and run virtual environment on command line

```
pip install virtualenv
virtualenv VENV
source venv/bin/activate
```

#### Install system dependancies 

```
pip install -r requirements.txt
```
#### Run in terminal python markovsolution.py prideandprejudice.txt. If pride and prejudice is not your flavor you can choose a different text file in the respository

![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/instructions_python_file_and_txt.png)

![alt text](https://github.com/GraceDurham/Markov-Chains-and-Twitter/blob/master/random_tweet.png)

