import providers
import socket

domains = { 'bat0':'default', 'bat1':'rhf', 'bat2':'wtk', 'bat3':'ssww', 'bat4':'wiese', 'bat5':'loe', 'bat6':'3land', 'bat7':'ref', 'bat8':'saek', 'bat9':'hotz', 'bat10':'sswo', 'bat11':'event', 'bat12':'swb', 'bat13':'ffng', 'bat14':'nalb', 'bat15':'test', 'bat32':'fftut', 'bat64':'fffr', 'bat65':'ffem', 'bat66':'bh'}

class Source(providers.DataSource):
    def required_args(self):
        return ['batadv_dev']

    def call(self, batadv_dev):
        return domains[batadv_dev]
