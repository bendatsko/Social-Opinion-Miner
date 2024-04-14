import subprocess

def main():
    print("Starting the setup process...")
    subprocess.call("python3 setup.py", shell=True)  # Use flag --clear to drop all tables

    print("Fetching New York Times articles...")
    subprocess.call("python3 get_articles.py", shell=True)

    print("Searching for Reddit discussions related to fetched articles...")
    for i in range(5):
        print(f"Initiating search for batch {i+1}/5...")
        subprocess.call("python3 search_reddit.py", shell=True)
    print("Reddit searches completed and data stored.")

    print("Summarizing articles and Reddit discussions...")
    subprocess.call("python3 get_summaries.py", shell=True)
    print("Summaries generated and stored.")

    print("Compiling all data into a single CSV file...")
    subprocess.call("python3 dump_to_csv.py", shell=True)
    print("Data compilation complete. CSV file ready.")

    print("Generating sentiment analysis visualizations...")
    subprocess.call("python3 plot_12_sentiments.py", shell=True)
    print("Sentiment analysis plots created.")

    print("All processes completed successfully.")



if __name__ == "__main__":
    main()
