from .bitcoin import main_bitcoin
from .businessinsider import main_businessinsider
from .cnbc import main_cnbc
from .coindesk import main_coindesk


def main():
    objects = main_businessinsider() + main_cnbc() + main_coindesk() + main_bitcoin()
    return objects