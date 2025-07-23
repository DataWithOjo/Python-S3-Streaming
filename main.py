import requests
import gzip
import io


def main():
    # Download wet.paths.gz and read first path
    index_url = "https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-10/wet.paths.gz"
    index_response = requests.get(index_url)
    index_response.raise_for_status()

    with gzip.GzipFile(fileobj=io.BytesIO(index_response.content)) as gz:
        first_path = gz.readline().decode("utf-8").strip()

    # Stream WET file (decompress and print line-by-line)
    wet_url = f"https://data.commoncrawl.org/{first_path}"
    response = requests.get(wet_url, stream=True)
    response.raise_for_status()

    # Decompress and print decoded lines from .wet.gz
    with gzip.GzipFile(fileobj=response.raw) as wet_gz:
        for line in wet_gz:
            print(line.decode("utf-8").strip())


if __name__ == "__main__":
    main()
