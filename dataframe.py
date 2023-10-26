from scrapping import Scraper
import pandas as pd


class CreateDataFrame:

    def __init__(self) -> None:
        self.df = pd.DataFrame()


    def create_dataframe(self, titles_list, authors_list, asins_list):

        max_length = max(len(titles_list), len(authors_list), len(asins_list))

        # pad shorter lists with none
        titles_list += [None] * (max_length - len(titles_list))
        authors_list += [None] * (max_length - len(authors_list))
        asins_list += [None] * (max_length - len(asins_list))

        self.df['Titles'] = titles_list
        self.df['Authors'] = authors_list
        self.df['ASIN'] = asins_list

        return self.df

    
    def convert_to_xlsx(self, dataframe):
        xlsx = dataframe.to_excel('output.xlsx', index=False)
        
        return xlsx


    def make_titles_list(self):
        scraper = Scraper()
        scraper.request()
        titles_list, authors_list, asins_list = scraper.parse_html()
        self.create_dataframe(titles_list, authors_list, asins_list)
        titles_list = self.df['Titles'].tolist()
        
        return titles_list
