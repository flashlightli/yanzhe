from elasticsearch import Elasticsearch


class ElasticSearchClass(object):

    def __init__(self):
        self.host = 'http://127.0.0.1'
        self.port = 9200
        self.user = ''
        self.password = ''
        self.connect()

    def connect(self):
        Elasticsearch(hosts=[{'host': self.host, 'port': self.port}],
                             http_auth=(self.user, self.password))


es = ElasticSearchClass()
res = es.search(index="weather", doc_type="person", body={})
print(res)