# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DataType

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "5f5ff3d8-f05b-4829-bca3-f3b743300ace",
"fs.azure.account.oauth2.client.secret": 'pu48Q~oqjTg2xsI9V7JHDHnwppTAOzVfSvkw0da9',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/1bfcf83e-1bb2-4d03-8384-8466413990a2/oauth2/token"}

dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@tokyoolympicdatachandru0.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/tokyoolympic",
extra_configs = configs)


# COMMAND ----------

# MAGIC %fs
# MAGIC ls "/mnt/tokyoolympic/"

# COMMAND ----------

spark

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").option("InferSchema","true").load("/mnt/tokyoolympic/raw-data/athletes.csv")
coaches  = spark.read.format("csv").option("header","true").option("InferSchema","true").load("/mnt/tokyoolympic/raw-data/coaches.csv")
entriesgender = spark.read.format("csv").option("header","true").option("InferSchema","true").load("/mnt/tokyoolympic/raw-data/entriesgender.csv")
medals = spark.read.format("csv").option("header","true").option("InferSchema","true").load("/mnt/tokyoolympic/raw-data/medals.csv")
teams = spark.read.format("csv").option("header","true").option("InferSchema","true").load("/mnt/tokyoolympic/raw-data/teams.csv")

# COMMAND ----------

athletes.show()

# COMMAND ----------

athletes.printSchema()

# COMMAND ----------

coaches.printSchema()

# COMMAND ----------

coaches.show()

# COMMAND ----------

entriesgender.show()

# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

entriesgender = entriesgender.withColumn("Female",col("Female").cast(IntegerType()))\
    .withColumn("Male",col("Male").cast(IntegerType()))\
    .withColumn("Total",col("Total").cast(IntegerType()))

# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

entriesgender.show()

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

medals.show()

# COMMAND ----------

medals = medals.withColumn("Gold",col("Gold").cast(IntegerType()))\
    .withColumn("Silver",col("Silver").cast(IntegerType()))\
        .withColumn("Bronze",col("Bronze").cast(IntegerType()))\
            .withColumn("Total",col("Total").cast(IntegerType()))\
                .withColumn("Rank by Total",col("Rank by Total").cast(IntegerType()))\
                

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

medals.show()

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

teams.show()

# COMMAND ----------

teams.printSchema()

# COMMAND ----------

# Find the top countries with the highest number of gold medals
top_gold_medal_countries = medals.orderBy("Gold", ascending=False).show()

# COMMAND ----------

# Find the top countries with the highest number of gold medals
top_gold_medal_countries = medals.orderBy("Gold", ascending=False).select("Team_country","Gold").show()

# COMMAND ----------

# Calculate the average number of entries by gender for each discipline
average_entries_by_gender = entriesgender.withColumn(
    'Avg_Female', entriesgender['Female'] / entriesgender['Total']
).withColumn(
    'Avg_Male', entriesgender['Male'] / entriesgender['Total']
)
average_entries_by_gender.show()

# COMMAND ----------

entriesgender.show()

# COMMAND ----------

athletes.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/tokyoolympic/transformed-data/athletes")
coaches.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/coaches")
entriesgender.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/entriesgender")
medals.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/medals")
teams.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympic/transformed-data/teams")

# COMMAND ----------

medals.show()
