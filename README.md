## Text2SQL Workshop
### Using OpenAI, Langchain and Postgresql to Talk to Your Data

<hr />

<img src="https://github.com/weet-ai/text2sql-workshop/blob/main/img/nosql.png?raw=true"/>

### Overview

* This repo demonstrates the power of **Large Language Models** and **Generative AI** for simplifying access to data: instead of querying a database using **SQL**, why not doing so using **Natural Language**?
* **text2sql** is a basic Python package which ships with [Langchain](https://www.langchain.com/). It contains simple logic for connecting to a local [Postgresql](https://www.postgresql.org/) instance, and by leveraging Langchain's `create_sql_query_chain`, it obtains metadata from our local DB instances and creates multiple prompts which are executed against an LLM (in our case, [OpenAI](https://openai.com/) ChatGPT).
* As a result, we are able to convert questions from Natural Language to SQL Queries that are compliant with Postgresql's dialect.

### Usage

* Create a virtual environment with your tool of choice and install the **text2sql** Python package
* Once the package is installed, you can create an IPython kernel and use it in Jupyter - checkout the notebooks provided in the `sandbox` folder.

#### Example

```python
from text2sql.core import Text2SQL

sql = Text2SQL(model = "gpt-3.5-turbo")
query = sql.query("How much do we have in total sales?")
print(query)
```

```bash
> SELECT SUM("Weekly_Sales") AS total_sales FROM sales
```

## Prereqs

* We use Docker to boot up a Postgresql DB. Just run `docker-compose up -d` and you should be good to go
* To ingest data into Postgres, run `text2sql/ingest.py` (for simplification purposes, the package expects you to be running a local instance of Postgresql at port 5432)
* Make sure that you properly set your `OPENAI_API_KEY`

## Authors

* [Rafael Pierre](https://www.linkedin.com/in/rafaelpierre)