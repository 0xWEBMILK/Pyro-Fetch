import requests


async def priceFetch(coin, currencyList):

    # Fetch coin price with in custom currency
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin.lower()}&vs_currencies={','.join(currencyList).lower()}'
    response = requests.get(url)
    data = response.json()


    # Creating memory case for prices 
    listOfPrices = []

    print(data)


    if data[coin]:
        for index in range(len(currencyList)):
            
            if data[coin][currencyList[index]]:

                # Add coin price in memory case
                listOfPrices.append([currencyList[index], data[coin][currencyList[index]]])


                # Create pretty result
                result = f"```Current price of {coin}:\n"

                for item in listOfPrices:
                    result += f"{item[0]}: {item[1]}\n"

                result += "```"


        return result.strip()