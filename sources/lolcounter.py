from utils.soup import soup_request

def find_counters(champion):
        
    soup = soup_request("https://lolcounter.com/champions/"+champion.lower())

    counters = soup.find(class_='weak-block')
    counters = counters.find_all(class_="champ-block")
    counter_list = [counter.find(class_='name').get_text() for counter in counters]
    return counter_list