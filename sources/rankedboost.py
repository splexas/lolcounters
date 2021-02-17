from utils.soup import soup_request

def find_counters(champion):
        
    soup = soup_request("https://rankedboost.com/league-of-legends/counter/"+champion.lower())

    counters = soup.find(class_='WeakAgainstHolder')
    counters = counters.find_all(class_="WeakAgainstBorder")
    counter_list = [counter.find(class_='WeakAgainstName').get_text()+" | "+counter.find_all(class_='WeakAgainstWinRateContent')[1].get_text()+" WR" for counter in counters]
    return counter_list

