# Tools of Data Science

Raw data must pass through various Data Science task categories such as data management, data integration and transformation, data visualization, model building, model deployment, and model monitoring and assessment.

## Data Management Tools

- **MySQL**: Popular open-source RDBMS that uses SQL to manage and store data. Common use: Web applications, data warehouses, and e-commerce.
- **PostgreSQL**: A powerful RDBMS that emphasizes extensibility and SQL compliance. Features: JSON support, full-text search, and spatial data.
- **Apache Cassandra**: Distributed NoSQL database handling large amounts of data across many servers. Features: high-availability, fault tolerance, and tunable consistency.
- **Elasticsearch**: Distributed search and analytics engine based on the Lucene library. Features: scalable, powerful querying, real-time data-indexing.
- **Ceph**: Open-source software-defined storage platform for modern data centers. Provides object, block, and file storage under a unified system.
- **CouchDB**: NoSQL document-oriented database storing data in JSON format. Features: scalable, fault-tolerant, and user-friendly.
- **MongoDB**: NoSQL database using flexible JSON for storing data. Features: scalability and high availability, suitable for large volumes of unstructured data.
- **Hadoop HDFS**: A distributed file system providing high throughput access to data. Features: fault-tolerant, scalable, and efficient for large datasets.

## Data Integration and Transformation Tools

- **Apache Spark SQL**: Provides programming interfaces for structured data using SQL, data frames, and datasets.
- **Kubeflow**: Open-source ML toolkit built on Kubernetes. Supports distributed training, model serving, and hyperparameter tuning.
- **NodeRED**: Open-source visual programming tool for wiring together hardware devices, APIs, and online services.
- **Apache Airflow**: Open-source platform for authoring, scheduling, and monitoring workflows. Supports task dependencies, parallelism, and error handling.
- **Apache Nifi**: Open-source data integration platform for automating data flow between systems.
- **Apache Kafka**: Distributed streaming platform for real-time data streams.

## Data Visualization Tools

- **Pixiedust**: Offers built-in visualizations and data connectors with support for third-party libraries.
- **Kibana**: Commonly used with Elasticsearch to analyze and visualize large datasets.
- **Hue**: User-friendly interface for exploring data and creating visualizations without programming (Apache Hadoop).
- **Superset**: Modern business intelligence web application for visualizing and exploring large datasets.

## Model Deployment Tools

- **PredictionIO**: Open-source machine learning server built on scalable, distributed infrastructure.
- **Kubernetes**: Open-source platform for container orchestration. Automates the management and scaling of containerized applications.
- **MLeap**: Serialization and deserialization of learning models in cross-platform files, supporting frameworks like Spark, Scikit-learn, and TensorFlow.
- **TensorFlow Lite**: Lightweight version of TensorFlow for mobile and embedded devices, supporting hardware accelerators.
- **Apache Seldon**: Deploys and manages ML models on Kubernetes.
- **Red Hat OpenShift**: Container application framework based on Kubernetes.
- **TensorFlow Serving**: Open-source utility for serving ML models in real-world settings.
- **TensorFlow.js**: JavaScript library for building and deploying ML models directly in the browser or Node.js.

## Model Monitoring and Assessment Tools

- **IBM AI Fairness 360**: Open-source toolkit for detecting and mitigating bias in ML models.
- **IBM AI Explainability 360**: Open-source toolkit for explaining ML model behavior and decisions.
- **IBM Adversarial Robustness 360 Toolbox**: Protects ML models from adversarial attacks.
- **Prometheus**: Open-source monitoring system that collects and stores metrics in real-time.
- **ModelDB**: Open-source platform for managing ML models and experiments.

## Code Asset Management Tools

- **Git**, **GitHub**, **GitLab**, **Bitbucket**: Tools for managing code repositories, version control, and collaboration.

## Data Asset Management Tools

- **Apache Atlas**, **ODPi Egeria**, **Kylo**: Tools for managing and governing data assets.

---

# Languages for Data Science

Python is widely used in data science, with libraries like **Pandas**, **NumPy**, **SciPy**, and **Matplotlib** for scientific computing and data visualization. Python also supports Natural Language Processing (NLP) with libraries such as **NLTK**.

R is a free language with array-oriented syntax, making it easy for learners to translate mathematical equations into code.

SQL is a non-procedural language designed for managing relational databases, distinct from other programming languages.

Java supports data science with tools like **Weka**, **Java-ML**, **Apache MLlib**, and **Deeplearning4j**.

Apache Spark, a popular tool for data science, is built with Scala and includes components like **Shark**, **MLlib**, **GraphX**, and **Spark Streaming**.

For data science in JavaScript, **TensorFlow.js** is a prominent tool for building and deploying ML models.

**JuliaDB** is a great application of Julia for data science, supporting high-performance data manipulation.

---

# APIs

API (Application Programming Interface) allows communication between software components. 
For example, **Pandas** can interact with other software through APIs. 
A common type of API is **REST API**, which allows clients to interact with web services using HTTP methods.

Example: **Watson Speech-to-Text API**, which converts speech to text. A POST request sends an audio file, and a GET request returns the text transcription.

---

# Types of Datasets

## Open Datasets

### Government Data
- [Data.gov](https://www.data.gov/)
- [US Census Bureau Data](https://www.census.gov/data.html)
- [UK Government Data](https://data.gov.uk/)
- [Open Data Network](https://www.opendatanetwork.com/)

### Financial Data Sources
- [World Bank Data](https://data.worldbank.org/)
- [Global Financial Data](https://www.globalfinancialdata.com/)
- [UN Comtrade](https://comtrade.un.org/)
- [National Bureau of Economic Research (NBER)](https://www.nber.org/)
- [FRED - St. Louis Fed Economic Data](https://fred.stlouisfed.org/)

### Crime Data
- [FBI Uniform Crime Reporting](https://www.fbi.gov/services/cjis/ucr)
- [ICPSR National Archive of Criminal Justice Data](https://www.icpsr.umich.edu/icpsrweb/content/NACJD/index.html)
- [National Institute on Drug Abuse - Trends and Statistics](https://www.drugabuse.gov/related-topics/trends-statistics)
- [UNODC Data and Analysis](https://www.unodc.org/unodc/en/data-and-analysis/)

### Health Data
- [WHO Global Health Observatory](https://www.who.int/gho/database/en/)
- [FDA - Food Data](https://www.fda.gov/Food/default.htm)
- [SEER Cancer Statistics](https://seer.cancer.gov/faststats/selections.php?series=cancer)
- [Open Science Data Cloud](https://www.opensciencedatacloud.org/)
- [NASA PDS](https://pds.nasa.gov/)
- [NASA Earth Data](https://earthdata.nasa.gov/)
- [SGIM Public Datasets](https://www.sgim.org/communities/research/dataset-compendium/public-datasets-topic-grid)

### Academic and Business Data
- [Google Scholar](https://scholar.google.com/)
- [National Center for Education Statistics (NCES)](https://nces.ed.gov/)
- [Glassdoor Research](https://www.glassdoor.com/research/)
- [Yelp Dataset](https://www.yelp.com/dataset)

### Other General Data
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Reddit Datasets](https://www.reddit.com/r/datasets/)
