import scrapy



class DataSpiderSpider(scrapy.Spider):
    name = 'movies'
    page_number = 2
    start_urls = [
    'https://yts.lt/browse-movies/0/all/all/0/downloads' #most downloaded movies.

    ]

    def parse(self, response):#datas from the site that will be extracted.          
        movie_title = response.css('.browse-movie-title::text').extract()
        movie_year = response.css('.browse-movie-year').css('::text').extract()
        movie_rating = response.css('.rating').css('::text').extract()
        movie_genre = response.css('h4+ h4 , .rating+ h4').css('::text').extract()
         
        
        for item in zip (movie_title, movie_year, movie_rating, movie_genre):#this functions is only for the arrangement into columns and rows
        
            new_item = DatascienceItem()
            new_item['movie_title'] = item[0]
            new_item['movie_year'] = item[1]
            new_item['movie_rating'] = item[2]            
            new_item['movie_genre'] = item[3]
          
            
            yield new_item
            
            next_page = 'https://yts.lt/browse-movies/0/all/all/0/downloads?page=' + str(DataSpiderSpider.page_number)#for scraping multiple pages
            if DataSpiderSpider.page_number <= 10:
               DataSpiderSpider.page_number += 1  
               yield response.follow(next_page, callback = self.parse)
    
class DatascienceItem(scrapy.Item): #items that will be called
   movie_title = scrapy.Field()
   movie_year = scrapy.Field()    
   movie_rating = scrapy.Field()
   movie_genre = scrapy.Field()    
      

        