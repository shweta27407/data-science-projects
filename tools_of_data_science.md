## Tools of Data Science

Raw data must pass through various Data Science task categories, such as data management, data integration and transformation, 
data visualization, model building, model deployment, and model monitoring and assessment.

Data management tools are MySQL, PostgreSQL, MongoDB, Apache CouchDB, Apache Cassandra, Hadoop File System, Ceph, and elastic search. 
Data integration and transformation tools are Apache AirFlow, KubeFlow, Apache Kafka, Apache Nifi, Apache SparkSQL, and NodeRED. 
Data Visualization tools are Pixie Dust, Hue, Kibana, and Apache Superset. 
Model deployment tools are Apache PredictionIO, Seldon, Kubernetes, Redhat OpenShift, Mleap, TensorFlow service, TensorFlow lite, and TensorFlow dot JS. 
Model monitoring tools are ModelDB, Prometheus, IBM AI Fairness 360, IBM Adversarial Robustness 360 Toolbox, and IBM AI Explainability 360. 
Code asset management tools are Git, GitHub, GitLab, and Bitbucket. 
And finally, data asset management tools are Apache Atlas, ODPi Egeria, and Kylo.

**Data Management Tools**

MySQL -> popular open-source RDBMS that uses SQL to manage and store data. Common use is Web Applications, Data Warehouse, and e-commerce.
PostgreSQL -> powerful RDBMS that emphasizes extensibility and SQL compliances. Advanced features such as JSON-support, full-text search and spatial data.
Apache Cassandra -> highly scalable, distributed NoSQL database that can handle large amounts of structured, unstructured data across many commodity servers.
    High-availability, fault tolerance, tunable consistency levels, suitable for mission critical applications.
Elasticseach -> distributed, RESTful search and analytics engine based on Lucene library. Highly scalable, easy to use, powerful querying capabilities and
    real time data-indexing.
Ceph -> free, opensource, software-defined storage platform designed for modern data centers. Provides scalable object, block and file storage under unified system, with 
    high-availability, reliability and performance.
CouchDB -> NoSQL document-oriented database that uses JSON to store data. Highly scalable, fault-tolerant and easy to use.
MongoDB -> NoSQL document-oriented database that uses flexible JSON to store data. Scalability, high availability that makes it suitable 
    for modern web applications that handle large volumes of unstructured data.
Hadoop HDFS -> (hadoop distributed file system provides high through-put acccess to application data. Fault tolerant, scalable and efficient 
    making it suitable for storing and processing large datasets in distributed computed environment.

**Data Integration and Transformation Tools**

Apache Spark SQL -> module in Spark ecosystem, that provides programming interface for working with structured data using SQL, data frames and datasets.
Kubeflow -> open source machine learning toolkit built on top of Kubernetes. Provides a platform for building, deploying and managing end-to-end machine learning worklflows
    at scale, with support for distributed training, model serving and hyperparameter tuning.
NodeRED -> open source visual programming tool for wiring together hardware devices, API's and online services. Allows users to create event-driven flows of messages with support     for data transformation, filtering and aggregation
Apache Airflow -> opensource platform for programmatically authoring, scheduling and monitoring workflows. It allows users to define and execute complex workflows, with support       for task dependencies, parallelism and error handling.
Apache nifi -> opensource data integration platform that allows users to automate the flow of data between systems.
Apache Kafka -> distributed streaming platform that allows applications to publish, process and subscribe to streams of records in real time

**Data Visualization Tools**

Pixiedust -> provides range of built in visualizations, data connectors, with support for customization and extensibility through third party libraries.
Kibana -> commonly used with elasticSearch to analyze and visualize large datasets.
Hue -> offers user friendly experience for exploring data and creating visualization without programmming. (Apache Hadoop)
Superset -> modern enterprise ready business intelligence web application that makes it easy to visualize and explore large datasets. 

**Data Deployment Tools**

PredictionIO -> open source machine learning server built on scalable and distributed infrastructure
Kubernetes -> open source platform for container orchestration. Automatically launches, scales and manages containerized applications.
MLeap -> serializing and deserealizing learning models in cross platform files. Ability to export models from different machine learning libraries anf frameworks such as 
    spark, scikit-learna dn TensorFlow, and implement them in high-throughput and low latency environments.
TensorFlow Lite -> runs ML models on mobile and embedded devices. Supports variety of hardware accelerators like CPU, GPU and custom ASIC's.
Apache Seldon -> deploying and manage ML models on Kubernetes, 
Red Hat OpenShift -> container application frameworks based on Kubernetes.
TensorFlow Serving -> opensource utility that serves ML models in real world settings.
TensorFlow.js -> opensource library that builds and deploys ML models in javascript. Trains or executes models directly on browser or on Node.js.

**Data Monitoring and Assessment Tools**

IBM AI Fairness 360 -> open source toolkit for detecting and mitigating bias machine learning models.
IBM AI Explainability 360 -> open source toolkit for explaining the behavior and decisions of machine learning models.
IBM Adversarial Robustness 360 Toolbox -> protecting ML models from adversarial attacks.
Prometheus -> freely available monitoring system that collects and stores metrics in real time from different sources.
ModelDB -> open source platforms for managing ML models and experimensts.

## Languages for Data Science

For data science, you can use Python's scientific computing libraries like Pandas, NumPy, SciPy, and Matplotlib. 

Python can also be used for Natural Language Processing (NLP) using the Natural Language Toolkit (NLTK). 

Python is open source, and R is free software. 

R language’s array-oriented syntax makes it easier to translate from math to code for learners with no or minimal programming background.

SQL is different from other software development languages because it is a non-procedural language.

SQL was designed for managing data in relational databases. 

Data science tools built with Java include Weka, Java-ML, Apache MLlib, and Deeplearning4.

For data science, popular program built with Scala is Apache Spark which includes Shark, MLlib, GraphX, and Spark Streaming.

Programs built for Data Science with JavaScript include TensorFlow.js and R-js.

One great application of Julia for Data Science is JuliaDB.

## API's

API, allows communication between two pieces of software. Ex: Pandas is a set of software components where not all components are written in Python. In your program, there is some data and a set of software components. You can use the Pandas API to process the data by communicating with the other software components. 

The software component at the back end can be the same, but there can be an API for different languages. Consider TensorFlow at the back end, written in C++, that can use APIs for other languages, such as Python, JavaScript, C++, Java, and Go, and thus, the API is just the interface. 

REST APIs are another popular type of API. The R-E stands for Representational, the S stands for State, and the T stands for Transfer. They allow you to communicate through the internet and take advantage of resources, like storage, data, artificially intelligent algorithms, and much more. 

In REST API, your program is the client. The API communicates with a web service you can call through the internet, though there are rules regarding communication, input or request, and output or response. So, let's look at some common terms used with regards to API. You or your code are the client. The web service is the resource. The client finds the service via an endpoint. And the client sends requests to the resource and receives a response from the resource. Data is transmitted over the internet using HTTP methods. 
The REST APIs get all the information from the request sent by the client. The request is sent using an HTTP message that contains a JSON file. The file contains instructions for what operation is to be performed by the web service. This operation is transmitted to the web service via the internet, and the service performs the operation. Similarly, the web service returns a response through an HTTP message where the information is returned using a JSON file. And this information is transmitted back to the client. 

Example of a REST API is Watson Speech-to-Text API. This API converts speech to text. In the API call, you will send a copy of the audio file to the API. This is called a post request. In the API, we'll send the text transcription of what the individual is saying. At the back end, the API is making a GET request.

## Types of Datasets

**Open datasets  : **

# Government Data
- [Data.gov](https://www.data.gov/)
- [US Census Bureau Data](https://www.census.gov/data.html)
- [UK Government Data](https://data.gov.uk/)
- [Open Data Network](https://www.opendatanetwork.com/)

# Financial Data Sources
- [World Bank Data](https://data.worldbank.org/)
- [Global Financial Data](https://www.globalfinancialdata.com/)
- [UN Comtrade](https://comtrade.un.org/)
- [National Bureau of Economic Research (NBER)](https://www.nber.org/)
- [FRED - St. Louis Fed Economic Data](https://fred.stlouisfed.org/)

# Crime Data
- [FBI Uniform Crime Reporting](https://www.fbi.gov/services/cjis/ucr)
- [ICPSR National Archive of Criminal Justice Data](https://www.icpsr.umich.edu/icpsrweb/content/NACJD/index.html)
- [National Institute on Drug Abuse - Trends and Statistics](https://www.drugabuse.gov/related-topics/trends-statistics)
- [UNODC Data and Analysis](https://www.unodc.org/unodc/en/data-and-analysis/)

# Health Data
- [WHO Global Health Observatory](https://www.who.int/gho/database/en/)
- [FDA - Food Data](https://www.fda.gov/Food/default.htm)
- [SEER Cancer Statistics](https://seer.cancer.gov/faststats/selections.php?series=cancer)
- [Open Science Data Cloud](https://www.opensciencedatacloud.org/)
- [NASA PDS](https://pds.nasa.gov/)
- [NASA Earth Data](https://earthdata.nasa.gov/)
- [SGIM Public Datasets](https://www.sgim.org/communities/research/dataset-compendium/public-datasets-topic-grid)

# Academic and Business Data
- [Google Scholar](https://scholar.google.com/)
- [National Center for Education Statistics (NCES)](https://nces.ed.gov/)
- [Glassdoor Research](https://www.glassdoor.com/research/)
- [Yelp Dataset](https://www.yelp.com/dataset)

# Other General Data
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Reddit Datasets](https://www.reddit.com/r/datasets/)
