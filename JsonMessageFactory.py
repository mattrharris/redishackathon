import random
import uuid
import json
import datetime

class MessageFactory:
 
    # Template variable
    topicName = "trades"
    tenors = ("1H","1H_1H","2H_2F","JUN23_1F","SEP23_1F","DEC23_1F","MAR24_1F","JUN24_1F","SEP24_1F","DEC24_1F","MAR25_1F",
             "JUN25_1F","SEP25_1F","DEC25_1F","MAR26:4Y","4Y_1Y","5Y_1Y","6Y_1Y","7Y_1Y","8Y_1Y","9Y_1Y","10Y_2Y",          
             "12Y_3Y","15Y_5Y","20Y_5Y","25Y_5Y","30Y_5Y","35Y_5Y","40Y_5Y","45Y_5Y","50Y_5Y","55Y_5Y","60Y_10Y")
    books = range(1,101)
    cps = ("GS","MS","CITI","HSBC","SVB")   
    ccy = ("GBP","USD","JPY","EUR","NOK","AUD","NZD")
    country = ("ldn","nyk","tky")
    system = ("RiskEngineA","RiskEngineB","RiskEngineC")
    curves = ("eur.euribor.3m","eur.euribor.6m","eur.eonia.1b","eur.disc.[eur.estr.1b]","eur.euribor.1m","eur.euribor.12m","eur.bond.de","eur.bond.fr","eur.bond.it")

    # Message template
    data = {
                "header": {
                    "sendingSystem": "",
                    "messageId": "",
                    "sentTimeStamp": datetime.datetime.now().isoformat(),
                    "seqNo": 1
                },
                "riskResult": {
                    "subject": { "bookId": 153, "productType": "IRSwap", "counterparty": "cpty" },
                    "dv01": {
                            "currency": "ABC",
                            "curveId": "something",
                            "data": {
                            },
                    } 
                }
            }
 
    # Create message in the correct structure with random content
    def getMessage(self):
        local_data = self.data
        # Slice the last 12 characters from a uuid and prepend with country code to create a trade id.
        local_data["header"]["messageId"] = str(uuid.uuid4())
        local_data["header"]["sendingSystem"] = random.choice(self.system)
        local_data["riskResult"]["subject"]["bookId"] = "BOOK" + str(random.choice(self.books))
        local_data["riskResult"]["subject"]["counterparty"] = random.choice(self.cps)
        local_data["riskResult"]["dv01"]["currency"] = random.choice(self.ccy)
        local_data["riskResult"]["dv01"]["curveId"] = random.choice(self.curves)
        for t in self.tenors:
            local_data["riskResult"]["dv01"]["data"][t] = random.uniform(0,1e6)
        # Required as the string representation of a dict uses single quotes which isn't valid json.
        return json.dumps(local_data, indent=2)

    def main():
        mf = MessageFactory()
        print(mf.getMessage())

if __name__=="__main__":
    MessageFactory.main()
