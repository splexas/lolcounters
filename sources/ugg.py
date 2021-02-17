from utils.soup import soup_request


def find_counters(champion):

    soup = soup_request("https://u.gg/lol/champions/"+champion.lower()+"/counter")
    counters = soup.find(class_='counters-list best-win-rate')
    counters = counters.find_all(class_="counter-list-card best-win-rate")


    #counter_list = [counter.find(class_='champion-name').get_text() for counter in counters]
    
    counter_list = [counter.find(class_='champion-name').get_text()+" | "+counter.find(class_='win-rate').get_text() for counter in counters]
    return counter_list
