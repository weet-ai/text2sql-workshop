## Text2SQL Workshop
### Using OpenAI, Langchain and Postgresql

<hr />

<img src="https://github.com/weet-ai/text2sql-workshop/blob/main/img/nosql.png?raw=true"/>

### Overview

* This repo demonstrates the power of **Large Language Models** and **Generative AI** for simplifying access to data: instead of querying a database using **SQL**, why not doing so using **Natural Language**?

### Usage

* Create a virtual environment with your tool of choice and install the **text2sql** Python package
* Once the package is installed, you can create an IPython kernel and use it in Jupyter - checkout the notebooks provided in the `sandbox` folder.

## Prereqs

* We use Docker to boot up a Postgresql DB. Just run `docker-compose up -d` and you should be good to go
* To ingest data into Postgres, run `text2sql/ingest.py`
* Make sure that you properly set your `OPENAI_API_KEY`

## Authors

* [Rafael Pierre](https://www.linkedin.com/in/rafaelpierre)