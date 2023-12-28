# Building a Scalable Data Warehouse for AI-Driven Traffic Analytics

## Project Overview

Welcome to our AI startup's ambitious project aimed at transforming the way traffic data is analyzed and utilized for smart city initiatives. This README will guide you through the project structure, business need, data source, and instructions for setting up the data warehouse tech stack using Airflow, dbt, PostgreSQL, and Redash.

[Read the Blog for details](https://medium.com/@natnaelbekele142/data-warehousing-the-engine-of-business-intelligence-2dac8adeb921)

![Project Overview](images/project_overview.jpg)


### Project Structure

- **/dags:** Airflow DAG scripts for orchestrating data loading and transformation.
- **/dwh_dbt:** dbt project folder containing models for data transformation.
- **/notebooks:** Jupyter notebook files for raw CSV data processing and loading.
- **/data:** Raw CSV files used in the project.
- **/images:** Images used in the README.
- **/redash:** Redash project folder for visualization and reporting.
- **/test:** Contains test scripts.
- **.gitignore:** Git configuration to exclude unnecessary files.
- **docker-compose.yaml:** Docker Compose configuration for fully dockerized deployment.
- **requirements.txt:** File containing the list of project dependencies.

### Business Need

Our AI startup collaborates with businesses to deploy sensors, collecting diverse data for critical intelligence. The city traffic department has entrusted us to create a scalable data warehouse that analyzes vehicle trajectory data from swarm UAVs, aiming to enhance traffic flow and contribute to undisclosed projects.

### Data Source

We utilize the pNEUMA dataset, a large-scale collection of naturalistic vehicle trajectories in Athens, Greece. This dataset, acquired by a unique experiment using swarm drones, provides valuable insights into traffic patterns.

**Data Source:** [pNEUMA Dataset](https://zenodo.org/records/7426506)

**References for Understanding Data Generation:**
- [PIA15_poster.pdf](datafromsky.com)
- [Automatic vehicle trajectory extraction for traffic analysis from aerial video data](researchgate.net)

**Visualization and Interaction Tools:**
- [travia: Traffic data Visualization and Annotation tool](github.com/tud-hri/travia)
- [pNEUMA_mastersproject: Python files to work with pNEUMA dataset](github.com/JoachimLandtmeters/pNEUMA_mastersproject)

## Getting Started

### Setting Up Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Data-Warehouse.git
   cd Data-Warehouse
   
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run Airflow Services:**
   ```bash
   docker-compose up --build

4. **Access Airflow UI:**
   - Open your browser and go to http://localhost:8080.

5. **Customize DAGs and dbt Models:**
   - Adjust Airflow DAGs in the dags folder.
   - Modify dbt models in the dwh_dbt folder based on your specific requirements and data transformations.

6. **Stop Airflow Services:**
   ```bash
   docker-compose down

## Conclusion

This project aligns with our mission to revolutionize traffic analytics, providing cities with actionable insights for smart urban planning. We invite you to explore, contribute, and leverage our data warehouse solution to make impactful decisions for a more connected and efficient future.

[Read my Blog for in-depth explanation🔗](https://medium.com/@natnaelbekele142/data-warehousing-the-engine-of-business-intelligence-2dac8adeb921)

[![Read my Blog for in-depth explanation](images/blog_preview.jpg)](https://medium.com/@natnaelbekele142/data-warehousing-the-engine-of-business-intelligence-2dac8adeb921)

