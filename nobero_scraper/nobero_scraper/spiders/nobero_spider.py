import scrapy

class NoberoSpider(scrapy.Spider):
    name = "nobero_spider"
    start_urls = [
        'https://nobero.com/products/lunar-echo-oversized-t-shirt-1?variant=45663963218086'
    ]

    def parse(self, response):
        products = response.css('main.flex')
        for product in products:
            yield {
                'title': product.css('h1.capitalize::text').get().strip(),
                'price': product.css('spanclass::text').get(),
                'MRP': product.css('span spanclass::text').get(),
                'last_7_day_sale': product.css('span[class*="text-[#D51E20]"]::text').get().strip(),
                'available_skus': [
                    {
                        'color': product.css('span#selected-color-title::text').get().strip(),
                        'size': ["S","M","L","XL","XXL","XXXL"],
                    },
                    {
                        'color': product.css('span#selected-color-title::text').get().strip(),
                        'size': ["XXL"],
                    }
                ],
                'fit':product.css('p.text-\[\#000000\].pb-\[8px\].font-normal::text').get().strip(),
                
                
            }
            print(f"'title:'{title}")