# NL2SQL Studio: Your One-Stop Workshop for Natural Language to SQL Experimentation

NL2SQL Studio is a comprehensive, open-source toolkit designed to empower developers, data scientists, and analysts in exploring Natural Language to SQL (NL2SQL) and creating production grade NL2SQL pipelines.  Whether you're a seasoned practitioner or just starting out, NL2SQL Studio provides an intuitive interface and a robust set of features to streamline your NL2SQL development workflow.

## Key Features and Components

* **Diverse NL2SQL Library Integration:** Seamlessly integrate with popular NL2SQL libraries and frameworks. Compare performance, experiment, and find the best fit for your needs.
* **Intuitive UI:** A user-friendly web-based interface makes it easy to input schemas, formulate questions, execute translations, and visualize results.
* **Robust Reporting & Analytics :** Gain valuable insights into your NL2SQL models. Track metrics, analyze queries, identify areas for improvement, and generate reports.
* **Evaluation & Benchmarking:** Rigorously test your NL2SQL models against diverse datasets. Utilize built-in evaluation metrics and benchmarking tools to assess accuracy, efficiency, and robustness.
* **Curated Test Datasets:** Jumpstart your experimentation with a collection of pre-built test datasets and sample natural language queries.
* **Sample Code & Tutorials:** Learn from best practices! NL2SQL Studio includes sample code snippets, tutorials, and guides to help you get started quickly.
* **Flexible Deployment (nl2sql-lite):** Choose a lightweight local setup (nl2sql-lite) to match your infrastructure.

## Who Should Use NL2SQL Studio

* **Data Analysts & Scientists:** Empower yourself to query complex databases using natural language, even without deep SQL expertise.
* **Software Developers:** Integrate NL2SQL capabilities into your applications to enhance user interaction and data accessibility.
* **Researchers:** Explore the cutting edge of NL2SQL research and contribute to the development of new techniques and models. 
* **Students & Educators:**  Utilize NL2SQL Studio as a valuable learning resource to teach and learn about natural language processing and database interaction.

## Getting Started

 Check out the details [here](https://googlecloudplatform.github.io/nl2sql-studio/)

## Contributing

We welcome contributions! Please see our `CONTRIBUTING.md` file for guidelines.

## License

This project is licensed under the Apache License 2.0.

Let us know if you have any questions or feedback!


## Warnings
- **SQL Accuracy** : The SQL generated by this tool may be inefficient, inaccurate or incomplete. Always review and test the generated code before using it. We also recommend setting up periodic audits of the generated results.

- **Data Sensitivity** : Exercise caution when using this tool with sensitive or personal data. This framework can send imformation (sample rows, schema, comments etc.) from the database to LLMs, Vector Databases, etc. as part of the SQL generation pipeline. Ensure this does not violate your privacy policies and regulations. The framework may return improperly constructed SQL queries that can be exploited to gain unauthorized access or cause damage to your database. Always sanitize input parameters and validate generated SQL against known vulnerabilities.

- **Security Risks** : Please follow the the principle of least privilege while using this framework. This framework does not handle auth and relies on you to correctly configure access control mechanisms for the environment the code will be running in, so please ensure sufficient access restrictions for the account used to run this framework to prevent unintedned operations, bills etc. This framework may also auto-execute generated SQL queries for validation purposes, please ensure this is always used with read-only permissions to avoid accidental modifications to the database.

## Disclaimer
This is not an official Google product.
