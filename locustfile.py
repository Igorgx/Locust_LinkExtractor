from locust import HttpUser, task, between

class LinkExtractorUser(HttpUser):
    wait_time = between(1, 3) 
    
    @task
    def extrair_links(self):
        urls = [
            "https://www.google.com", "https://www.wikipedia.org",
            "https://www.github.com", "https://www.python.org",
            "https://www.docker.com", "https://www.bbc.com",
            "https://www.nasa.gov", "https://www.reddit.com",
            "https://www.nytimes.com", "https://www.imdb.com"
        ]
        for url in urls:
            self.client.get(f"/?url={url}", name="Extracao de Links")