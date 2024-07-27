# Tokyo Olympics Data Analytics | Azure End-To-End Data Engineering Project -12


## Description
This project provides a data engineering and analytical journey on the Tokyo Olympic dataset. Starting with a CSV on GitHub, the data is ingested into the Azure ecosystem via Azure Data Factory. It's initially stored in Azure Data Lake Storage Gen2, then transformed in Azure Databricks. The enriched data, once again housed in ADLS Gen2, undergoes advanced analytics in Azure Synapse. The insights are finally visualized in Azure Synapse or Power BI, offering a comprehensive view of the dataset.
## Architecture 
<img src="Assets/Architecture.png">

## Dataset Used 
This contains the details of over 11,000 athletes, with 47 disciplines, along with 743 Teams taking part in the 2021(2020) Tokyo Olympics.
This dataset contains the details of the Athletes, Coaches, Teams participating as well as the Entries by gender. It contains their names, countries represented, discipline, gender of competitors, name of the coaches.

Source(Kaggle): [2021 Olympics in Tokyo](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo)

## Azure Services Used
1. **Azure Data Factory:** For data ingestion from GitHub.
2. **Azure Data Lake Storage Gen2**: As the primary data storage solution.
3. **Azure Databricks:** For data transformation tasks.
4. **Azure Synapse Analytics:** To perform in-depth data analytics.
   
## Workflow 

## Initial Setup
1. Create Azure Free Subscription account  
2. Create a Resource Group 'tokyo-olympic-data' to house and manage all the Azure resources associated with this project. 
3. Within the created resource group, set up a storage account. This is specifically configured to leverage Azure Data Lake Storage(ADLS) Gen2 capabilities.
4. Create a Container inside this storage account to hold the project's data. Two directories 'raw-data' and 'transformed-data' are created to store raw data and transformed data.
  <img src="Assets/folderF1.png"> 

## Data Ingestion using Azure Data Factory
1. Begin by creating an Azure Data Factory workspace within the previously established resource group.
2. After setting up the workspace, launch the Azure Data Factory Studio. 
3. Upload the Tokyo Olympics dataset from kaggle to GitHub.
4. Within the studio, initialize a new data integration pipeline. Now use the task Copy Data to move data efficiently between various supported sources and destinations.
5. Configuring the Data Source with HTTP template as we are using http request to get the data from Github repo.
6. Establishing the Linked Service for source.
7. Configuring the File Format for and setting up the Linked Service Sink.
8. Repeat above steps to load all the datasets.
9. You can connect all the copy data activity together and run them all at once.
<img src="Assets/datafactory_pipeline.png">  
10. After the pipeline completes its execution, navigate to your Azure Data Lake Storage Gen2. Dive into the "raw_data" folder and validate that the files, like "athletes.csv", "medals.csv", etc., are present and populated with the expected data.

 <img src="Assets/RAW DATA folder insideS.png">

## Data Transformation using Azure Databricks
1. Navigate to Azure Databricks within the Azure portal and create a workspace within the previously established resource group and launch it.
2. Configuring Compute in Databricks
3. Create a new notebook within Databricks and rename it appropriately, reflecting its purpose or the dataset it pertains to.
4. Establishing a Connection to Azure Data Lake Storage (ADLS).
5. Using the credentials (Client ID, Tenant ID, Secret), write the appropriate code in the Databricks notebook to mount ADLS. 
6. Writing Data Transformations mount ADLS Gen2 to Databricks.
7. Writing Transformed Data to ADLS Gen2.
 <img src="Assets/transformed data folders listS.png">
  <img src="Assets/ATHELETS folder insideS.png">
Refer below notebook to transformations and code used to mount ADLS Gen2 to Databricks.

[Tokyo Olympics Transformation.ipynb](https://github.com/zBalachandar/Tokyo-Olympic-Data-Analytics-Azure-End-To-End-Data-Engineering-Project.-/blob/main/Data%20Bricks%20Notebooks/Tokyo%20Olympic%20Transformation%20.ipynb)

## Setting Up and Using Azure Synapse Analytics
1. Creating a Synapse Analytics Workspace.
2. Within Workspace navigate to the "Data" section, choose "Lake Database"  and create a Database "TokyoOlympicDB"
3. Creating Table from Data Lake from the Transformed Data folder within your ADLS Gen2 storage.
 <img src="Assets/db query.png">
 
## Performing Data Analysis on the Data

Create SQL script to Perform Exploratory data analysis using SQL.
You can also use PowerBI to generate your analysis reports.
 <img src="Assets/vizS.png">
 Dashboard Created.
 <img src="Data Reporting/Data-visualisation.png">

Refer to the SQL scripts used for data analysis 
[Tokyo Olympics SQL script.sql](https://github.com/zBalachandar/Tokyo-Olympic-Data-Analytics-Azure-End-To-End-Data-Engineering-Project.-/blob/main/Sql%20query/SQL%20script%201.sql)
