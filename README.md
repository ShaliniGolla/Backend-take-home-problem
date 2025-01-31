## **Backend-take-home-problem**

## **PubMed Paper Scraper**
This Python script scrapes PubMed for research papers based on a user-provided query. It extracts details such as the PubMed ID, title, publication date, non-academic authors, company affiliations, and corresponding author email. The results can be saved to a CSV file or printed to the console.

## **Features**
- **Dynamic Query Handling:** Users can input any PubMed query to fetch relevant papers.

- **Detailed Extraction:** Extracts key details from each paper, including affiliations and author emails.

- **CSV Export:** Results can be saved to a CSV file for further analysis.

- **Debug Mode:** Provides debug information during execution for troubleshooting.

- **User-Friendly Options:** Offers command-line options for help, debug mode, and custom CSV filenames.

## **Requirements**

- Python 3.x
- Libraries: requests, BeautifulSoup, csv, re
## **Usage**
- Run the script:
python pubmed_scraper.py
- Enter your PubMed query when prompted.

- Choose from the following options:

  -h: Display help or usage instructions.
  
  -d: Enable debug mode to print debug information during execution.
  
  -f: Specify a custom filename to save the results in CSV format.
  
  If no CSV filename is provided, the results will be printed to the console
  
## **example**: 
  Enter your PubMed query: cancer
  
  Choose an option:
  
  1 or -h for help or usage instructions, 
  
  2 or -d for debug info,
  
  3 or -f for specifying .csv filename,
  
  4 or enter any other value to exit,
  
  Enter your choice: 1
  
  Usage Instructions:
    -h: Display help or usage instructions.
    -d: Print debug information during execution.
    -f: Specify a .csv filename to save the results.
  
  Choose an option:
  
  1 or -h for help or usage instructions
  
  2 or -d for debug info
  
  3 or -f for specifying .csv filename
  
  4 or enter any other value to exit
  
  Enter your choice: 2
  
  Debug Information: Debug mode enabled.
  
  Choose an option:
  
  1 or -h for help or usage instructions
  
  2 or -d for debug info
  
  3 or -f for specifying .csv filename
  
  4 or enter any other value to exit Enter your choice: 3
  
  Enter the filename to save the results (e.g., results.csv): examples.csv
  
  Results will be saved to examples.csv
  
  extracting article id:  28244479 title:  Cancer and cure: A critical analysis.
  
  extracting article id:  27741350 title:  Measuring cancer evolution from the genome. 
  
  extracting article id:  38175589 title:  Epidemiology of Cancer.
  
  extracting article id:  18538731 title:  Tumor cell metabolism: cancer's Achilles' heel.
   
  ...........
  
  Data saved to examples.csv
