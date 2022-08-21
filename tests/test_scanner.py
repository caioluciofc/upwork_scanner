from scanners.upwork_scanner import UpworkScanner
import asyncio

def test_scanner():
    my_scanner = UpworkScanner()
    data_collect = asyncio.run(my_scanner.collect_user_data("bobbybackupy", "Argyleawesome123!"))
    assert data_collect is not None