# import scrapy

# class NoberoSpider(scrapy.Spider):
#     name = "nobero"
#     # allowed_domains = ["nobero.com"]
#     start_urls = ["https://nobero.com/pages/men"]

#     def parse(self, response):
#         category_urls = response.css('div.custom-page-season-grid::attr(href)').getall()
#         for url in category_urls:
#             yield scrapy.Request(url=response.urljoin(url), callback=self.parse_category)

#     def parse_category(self, response):
#         product_urls = response.css('main.collection-container::attr(href)').getall()
#         for url in product_urls:
#             yield scrapy.Request(url=response.urljoin(url), callback=self.parse_product)

#     def parse_product(self, response):
#         product_data = {
#             "category": response.css('h1.font-[familySemiBold]::text').getall()[-1],
#             "url": response.url,
#             "title": response.css('h1.capitalize::text').get().strip(),
#             "price": int(response.css('h2#variant-price::text').re_first(r'\d+')),
#             "MRP": int(response.css('span#variant-compare-at-price::text').re_first(r'\d+')),
#             "last_7_day_sale": int(response.css('span.font-[familyBold]::text').re_first(r'\d+')),
#             "available_skus": self.get_skus(response),
#             "fit": self.get_product_detail(response, "Fit"),
#             "fabric": self.get_product_detail(response, "Fabric"),
#             "neck": self.get_product_detail(response, "Neck"),
#             "sleeve": self.get_product_detail(response, "Sleeve"),
#             "pattern": self.get_product_detail(response, "Pattern"),
#             "length": self.get_product_detail(response, "Length"),
#             "description": self.get_description(response)
#         }
#         yield product_data

#     def get_skus(self, response):
#         skus = []
#         colors = response.css('select#Color option::text').getall()
#         sizes = response.css('select#Size option::text').getall()

#         for color in colors:
#             skus.append({
#                 "color": color.strip(),
#                 "size": [size.strip() for size in sizes if size.strip()]
#             })
#         return skus

#     def get_product_detail(self, response, detail_name):
#         return response.xpath(f"//label[contains(text(), '{detail_name}')]/following-sibling::text()").get().strip()

#     def get_description(self, response):
#         description = response.css('div.product-description__content p::text').getall()
#         return '\n'.join([desc.strip() for desc in description])


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
