import requests
import pyfiglet
def main():
    name = getNameSyb()
    url=f"https://finnhub.io/api/v1/search?q={name}&token=d3u2rbpr01qvr0dl7j60d3u2rbpr01qvr0dl7j6g"

    response=requests.get(url).json()
    if not response["result"]:
        ascii_art=pyfiglet.figlet_format("Sorry ")
        print("No Company found  Try Again !!")
        print(ascii_art)
        exit()

    info=getCompanyInfo(response)
    stocks=getStockInfo(info)
    try:
        x=int(input("Press 1 for searching  Other Companies or Press 0 for exit: "))
        if(x==1):
            main()
        elif(x==0):
            print("Thank u for using Stock Tracker")
            ascii=pyfiglet.figlet_format("Thank You")
            print(ascii)
            exit()
    except ValueError:
        pass





def getCompanyInfo(response):
    symbol=response["result"][0]["symbol"]
    profile_url=requests.get(f"https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token=d3u2rbpr01qvr0dl7j60d3u2rbpr01qvr0dl7j6g").json()

    info={
        "Name":profile_url["name"],
        "Country":profile_url["country"],
        "Industry":profile_url["finnhubIndustry"],
        "Symbol":symbol,
        "Website":profile_url["weburl"]
    }
    print("------ Company Details ------\n")
    for key,value in info.items():
        print(f'{key}: {value}')

    return info
    # getStockInfo(profile_url)





def getNameSyb():
    Name=input("Enter the company Name or Symbol: ").strip()
    return Name





def getStockInfo(profile_url):
    stockInfo=requests.get(f'https://finnhub.io/api/v1/quote?symbol={profile_url["Symbol"]}&token=d3u2rbpr01qvr0dl7j60d3u2rbpr01qvr0dl7j6g').json()

    data={
        "Current Price":stockInfo["c"],
        "Highest Price":stockInfo["h"],
        "Lowest Price":stockInfo["l"],
        "Opening Price":stockInfo["o"],
        "Percent Change":stockInfo["dp"],
    }
    print("\n------Stock Information------\n")

    for key,val in data.items():
        print(f'{key}: {val}')
    print("\n----------------------------------")
    return data




if __name__ == "__main__":
    print("\n!!!!!-------Welcome to Stock Tracker Program -------!!!!!\n")
    main()
