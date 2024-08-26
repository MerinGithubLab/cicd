#This is CICD integration
import json
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!welcome')
    }
if __name__ == "__main__":
    def main():
        result = lambda_handler({}, {})
        print(result)


    main()
