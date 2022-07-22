import json
import time
import random
import boto3


from logging import getLogger


logger = getLogger(__name__)

sfn = boto3.client('stepfunctions')

DRIVER_NAME = "Sally"
MAX_WAIT = 10 #Wait calculated in 100s of milliseconds
MIN_WAIT = 0 #Wait calculated in 100s of milliseconds
REJECT_THRESHOLD = 4

def sleep(s):
    time.sleep(s)

def lambda_handler(event, context):
    token = event.get("token")
    randomWait = random.randint(MIN_WAIT, MAX_WAIT)
    logger.info("Random Wait Generated (s) : " + str(randomWait));  
    
    #Driver is not available to accept delivery
    if randomWait <= REJECT_THRESHOLD:
        logger.info("Driver " + DRIVER_NAME + " is not available to accept the delivery")
    
    # Simulate random response time of driver
    sleep(randomWait)
    logger.info('Sleeping for: ' + str(randomWait) + ' s')

    # Return token to step functions


    logger.info('JSON Returned to Step Functions:'); 

    sfn.send_task_success(
        taskToken=token,
        output=json.dumps({
            "driver_name": DRIVER_NAME
        })
    )
    return

if __name__ == '__main__':
    lambda_handler({"token":"XXXX"}, [])