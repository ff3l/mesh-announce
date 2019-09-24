import providers
from providers.util import call

class Source(providers.DataSource):
    def call(self):
        return call(['lsb_release','-ds'])[0]
