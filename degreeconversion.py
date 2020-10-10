import json


def lambda_handler(event, context):

    return { 
    
       "sessionAttributes": event["sessionAttributes"],
             "dialogAction": {
                  "type": "Close",
                  "fulfillmentState": "Fulfilled",
                  "message": {
                      "contentType":"PlainText",
                      "content": "converted "+ event["currentIntent"]["slots"]["quantity"]+ "  " + event["currentIntent"]["slots"]["source"]+ " to "+ DegreeConversion(event["currentIntent"]["slots"]["quantity"],event["currentIntent"]["slots"]["source"],event["currentIntent"]["slots"]["dest"]) + event["currentIntent"]["slots"]["dest"]
                  
                  }

                }
     
    }
def DegreeConversion(quantity, source, dest):
    quantity = float(quantity)
    if source == "celsius" and dest == "fahrenheit":
        return str((quantity * 9/5) + 32)
            
    if source == "fahrenheit" and dest == "celsius":
        return str((quantity - 32) * 5/9 )
    
