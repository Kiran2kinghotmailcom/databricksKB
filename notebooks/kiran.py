# Databricks notebook source
dbutils.fs.mkdirs("dbfs:/databricks/scripts/")


# COMMAND ----------

ld dbfs

# COMMAND ----------

display (dbutils.fs.ls("dbfs:/databricks/scripts/"))

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /databricks/init_scripts/

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/databricks/scripts/")

# COMMAND ----------

dbutils.fs.put("/databricks/scripts/postgresql-install.sh","""
#!/bin/bash
wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar""", True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts/postgresql-install.sh"))

# COMMAND ----------

# MAGIC %sh

# COMMAND ----------

ls

# COMMAND ----------

# MAGIC %sh

# COMMAND ----------

ls

# COMMAND ----------

pwd

# COMMAND ----------

ls /databricks/

# COMMAND ----------

cd /databricks/

# COMMAND ----------

ls

# COMMAND ----------

pwd

# COMMAND ----------

cd /databricks/scripts

# COMMAND ----------

locate scripts

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts"))

# COMMAND ----------

cd /databricks/

# COMMAND ----------

cd hive

# COMMAND ----------

cd conf/


# COMMAND ----------

ls

# COMMAND ----------

ls -al

# COMMAND ----------

cat /databricks/hive/conf/hive-site.xml


# COMMAND ----------

# MAGIC %sh

# COMMAND ----------

cat /databricks/hive/conf/hive-site.xm
cat /databricks/hive/conf/hive-site.xml

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /databricks/hive/conf/hive-site.xml

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/databricks/scripts1/")

# COMMAND ----------

display (dbutils.fs.ls("dbfs:/databricks/scripts1/"))

# COMMAND ----------

dbutils.fs.put(
    "/databricks/scripts/external-metastore.sh",
    """#!/bin/sh
      |
      |# Quoting the label (i.e. EOF) with single quotes to disable variable interpolation.
      |cat << 'EOF' > /databricks/driver/conf/00-custom-spark.conf
      |[driver] {
      |    # Hive specific configuration options for metastores in remote mode.
      |    # spark.hadoop prefix is added to make sure these Hive specific options will propagate to the metastore client.
      |    "spark.hadoop.hive.metastore.uris" = "thrift://<metastore-host>:<metastore-port>"
      |
      |    # Spark specific configuration options
      |    "spark.sql.hive.metastore.version" = "<hive-version>"
      |    # Skip this one if <hive-version> is 0.13.x.
      |    "spark.sql.hive.metastore.jars" = "<hive-jar-source>"
      |
      |    # If any of your table or database use s3 as the file system scheme,
      |    # uncomment the next line to set the s3:// URL scheme to S3A file system.
      |    # spark.hadoop prefix is added to make sure these file system options will
      |    # propagate to the metastore client and Hadoop configuration.
      |    # "spark.hadoop.fs.s3.impl" = "com.databricks.s3a.S3AFileSystem"
      |
      |    # If you need to use AssumeRole, uncomment the following settings.
      |    # "spark.hadoop.fs.s3a.impl" = "com.databricks.s3a.S3AFileSystem"
      |    # "spark.hadoop.fs.s3n.impl" = "com.databricks.s3a.S3AFileSystem"
      |    # "spark.hadoop.fs.s3a.credentialsType" = "AssumeRole"
      |    # "spark.hadoop.fs.s3a.stsAssumeRole.arn" = "<sts-arn>"
      |}
      |EOF
      |""".stripMargin,
    overwrite = true
)

# COMMAND ----------

dbutils.fs.put(
    "/databricks/scripts/external-metastore.sh",
    """#!/bin/sh
      |
      |# Quoting the label (i.e. EOF) with single quotes to disable variable interpolation.
      |cat << 'EOF' > /databricks/driver/conf/00-custom-spark.conf
      |[driver] {
      |    # Hive specific configuration options for metastores in remote mode.
      |    # spark.hadoop prefix is added to make sure these Hive specific options will propagate to the metastore client.
      |    "spark.hadoop.hive.metastore.uris" = "thrift://<metastore-host>:<metastore-port>"
      |
      |    # Spark specific configuration options
      |    "spark.sql.hive.metastore.version" = "<hive-version>"
      |    # Skip this one if <hive-version> is 0.13.x.
      |    "spark.sql.hive.metastore.jars" = "<hive-jar-source>"
      |
      |    # If any of your table or database use s3 as the file system scheme,
      |    # uncomment the next line to set the s3:// URL scheme to S3A file system.
      |    # spark.hadoop prefix is added to make sure these file system options will
      |    # propagate to the metastore client and Hadoop configuration.
      |    # "spark.hadoop.fs.s3.impl" = "com.databricks.s3a.S3AFileSystem"
      |
      |    # If you need to use AssumeRole, uncomment the following settings.
      |    # "spark.hadoop.fs.s3a.impl" = "com.databricks.s3a.S3AFileSystem"
      |    # "spark.hadoop.fs.s3n.impl" = "com.databricks.s3a.S3AFileSystem"
      |    # "spark.hadoop.fs.s3a.credentialsType" = "AssumeRole"
      |    # "spark.hadoop.fs.s3a.stsAssumeRole.arn" = "<sts-arn>"
      |}
      |EOF
      |""".stripMargin,
    overwrite = true
)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from default.adfas

# COMMAND ----------

# MAGIC %sql

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from default.abc

# COMMAND ----------

# MAGIC %ssh curl -u kiran.bharathi@databricks.com -p <password> https://cust-success.cloud.databricks.com/api/2.0/clusters/list

# COMMAND ----------

# MAGIC %sh curl -u kiran.bharathi@databricks.com -p <password> https://cust-success.cloud.databricks.com/api/2.0/clusters/list

# COMMAND ----------

# MAGIC %sh curl -u kiran.bharathi@databricks.com -p <Atp@18062018> https://cust-success.cloud.databricks.com/api/2.0/clusters/list

# COMMAND ----------

