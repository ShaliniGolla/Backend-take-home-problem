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
