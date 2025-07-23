# 🚀 Download with Boto3

This exercise demonstrates how to work with AWS S3 using Python and the `boto3` library. You'll download and process large files from the **Common Crawl** public dataset, all while practicing efficient in-memory file handling and streaming techniques using Docker.

---

## 📝 Problem Statement

Your task is to interact with an AWS S3 public bucket using Boto3 to complete the following steps:

1. **Download** a `.gz` file from the S3 bucket:
   - **Bucket**: `commoncrawl`
   - **Key**: `crawl-data/CC-MAIN-2022-05/wet.paths.gz`

2. **Extract the file in memory** (without writing it to disk).

3. **Read the first line**, which contains a URI to another file.

4. **Download the file from that URI** using Boto3 again.

5. **Stream and print** each line of the file to the terminal (without loading the full file into memory).

---

## 📦 Setup

Make sure you are in the project direct
