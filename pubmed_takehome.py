import requests
from bs4 import BeautifulSoup
import csv
import re


def fetch_article_details(article_url): #fetching article details from each article
    try:
        response = requests.get(article_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract affiliations
        affiliations = []
        affiliation_section = soup.find("div", class_="affiliations")
        if affiliation_section:
            affiliation_tags = affiliation_section.find_all("li")
            for tag in affiliation_tags:
                affiliations.append(tag.text)

        # Extract corresponding author email (placeholder for now)
        email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
        
        # Extract non-academic authors
        non_academic_authors_list = soup.find("a", class_="full-name")
        non_academic_authors = non_academic_authors_list.text if non_academic_authors_list else "N/A"
        emails = email_pattern.findall("; ".join(affiliations) if affiliations else "N/A")
        # Extract publication date
        date_tag = soup.find("span", class_="cit")
        if date_tag:
            publication_date_raw = date_tag.text
            s = publication_date_raw.index(";") if ";" in publication_date_raw else len(publication_date_raw)
            publication_date = publication_date_raw[:s].strip()
        else:
            publication_date = "N/A"

        return {
            "non_academic_authors": non_academic_authors,
            "company_affiliations": "; ".join(affiliations) if affiliations else "N/A",
            "publication_date": publication_date,
            "email":emails[0] if emails else "N/A"
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching article {article_url}: {e}")
        return {"non_academic_authors": "N/A", "company_affiliations": "N/A", "publication_date": "N/A"}


def fetch_pubmed_papers(query,debug): #fetching query related articles
    base_url = "https://pubmed.ncbi.nlm.nih.gov/"
    records_fetched = 0
    paper_data = []
    offset = 0  # Start from the first page

    #while records_fetched < max_results:
    while True:
        # Construct the URL with the offset for pagination
        search_url = f"{base_url}?term={query.replace(' ', '+')}&page={offset // 10 + 1}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find articles on the current page
        articles = soup.find_all("article", class_="full-docsum")
        if not articles:
            print("No more articles found.")
            break
        
        for article in articles:
            #if records_fetched >= max_results:
            #   break

            # Extract PubMed ID
            pubmed_id = article.a['href']

            # Extract Title
            title_tag = article.find("a", class_="docsum-title")
            title = title_tag.text.strip() if title_tag else "N/A"

            
            # Fetch details from the article page
            article_url = f"{base_url}{pubmed_id}/"
            details = fetch_article_details(article_url)
            if details["company_affiliations"]=="N/A":
                continue
            
            if(debug):
                print("extracting article id: ",pubmed_id[1:-1],"title: ",title)

            # Append the record to the data list
            paper_data.append([
                pubmed_id[1:-1], title, details["publication_date"],
                details["non_academic_authors"], details["company_affiliations"],details["email"]  # Email placeholder
            ])
            records_fetched += 1

            # Add a short delay to avoid overwhelming the server
            #time.sleep(1)

        # Update the offset for the next page
        offset += 10

    return paper_data


def save_to_csv(data, filename="pubmed_papers_dynamic.csv"):
    headers = [
        "PubmedID", "Title", "Publication Date",
        "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
    ]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    query = input("Enter your PubMed query: ")
    #max_results = int(input("Enter the maximum number of results to fetch: "))
    fflag=False
    debug=False
    count=0
    while(count<3):
        count+=1
        c = input(
        "Choose an option:\n"
        "1 or -h for help or usage instructions\n"
        "2 or -d for debug info\n"
        "3 or -f for specifying .csv filename\n"
        "4 or enter any other value to exit "
        "Enter your choice: ")
        if c.lower() == "-h" or c=="1":
            print("Usage Instructions:")
            print("  -h: Display help or usage instructions.")
            print("  -d: Print debug information during execution.")
            print("  -f: Specify a .csv filename to save the results.")
        elif c.lower() == "-d" or c=="2":
            print("Debug Information: Debug mode enabled.")
            debug=True
        # Here you can implement your debug-related logic
        elif c.lower() == "-f" or c=="3":
            fflag=True
            filename = input("Enter the filename to save the results (e.g., results.csv): ")
            print(f"Results will be saved to {filename}")
        # Add your CSV saving logic here
        else:
            break
            #print("Invalid option. Please try again.")
    papers = fetch_pubmed_papers(query,debug)
    if(fflag==False):
        print("No option choosed print output to console")
        for paper in papers:
            print(paper)
    else:
        #papers = fetch_pubmed_papers(query, max_results)
        save_to_csv(papers,filename)
