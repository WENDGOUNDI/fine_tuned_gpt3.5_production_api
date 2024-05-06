# Fine Tuning GPT-3.5 Turbo and Serving as LLM API

# DESCRIPTION
In the bustling world of e-commerce, customer engagement and satisfaction are paramount. One innovative solution to enhance user experience and streamline interactions is the implementation of a custom chatbot tailored specifically for your e-commerce platform. This project entails fine-tuning the powerful GPT-3.5 Turbo large language model to create an intelligent conversational agent capable of addressing customer inquiries, providing product recommendations, assisting with purchases, and offering personalized assistance. The custom large language model will be converted into an API to facilitate its integration to the e-commerce platform.

# STEPS
 - load the data and drop unnecessary columns.
 - Use pandas for data preprocessing the format the dataset to meet OpenAi gpt model fi the dataset
 - Updload the training data in openai platform the launch the training
Once the training is completed, OpenAI will send a notification. In addition, you will need the fine tuned id to send queries to your custom gpt model.
Finally we used Flask to build an API for quering the custom gpt model.

# DEPENDENCIES
 - Flask
 - Pandas
 - Json
 - Openai

# DATASET
The dataset used in this project has been downloaded from kaggle. It's a Q&A clothes shop chatbot dataset large of 1038 rows. Its main purpose is to support building a chatbot to provide a better customer assistance. It has 3 columns: context, question and answer but only question and answer columns will be used for fine tuning our chatgpt3.5-turbo. Our data will be formated/prepocoessed to follow openai training data format. Each paired question-answer should be a conversation in the same format as openai **Chat Completions API** requirements, specifically where each message (question-answer) has a role, content.
A best practice shared by OpenAI team, is to take a set of instructions and prompts that we found worked best for our model prior the fine-tuning, and includ them in every training example. This should let help the model to reach the best and most general results, especially if we have relatively few (e.g. under a hundred) training examples.

# SYSTEM OVERVIEW

# TESTING

## API Test
![api_inference](https://github.com/WENDGOUNDI/fine_tuned_gpt3.5_production_api/assets/48753146/85dc7514-4017-4104-9f63-7acbcb2513d2)

## Chatbot Test
 - ### Test 1
![inference](https://github.com/WENDGOUNDI/fine_tuned_gpt3.5_production_api/assets/48753146/958b6eeb-6135-42cf-b26a-071d2fb0ef05)

 - ### Test 2
![inference2](https://github.com/WENDGOUNDI/fine_tuned_gpt3.5_production_api/assets/48753146/3bd916c2-3049-4e7b-a71d-d635dd29e286)

# REFERENCE
 - dataset link: https://www.kaggle.com/datasets/quangnguyen711/clothes-shop-chatbot-dataset
 - OpenAI training data preparation: https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset
