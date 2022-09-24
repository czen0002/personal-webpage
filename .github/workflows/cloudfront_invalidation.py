import time
import sys
import boto3
from botocore.exceptions import ClientError


def create_invalidation(cf_client, distribution_id):
    try:
        response = cf_client.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [
                        '/*'
                    ]
                },
                'CallerReference': str(time.time()).replace(".", "")
            }
        )
        invalidation_id = response['Invalidation']['Id']
        print("Invalidation created successfully with Id: {}".format(invalidation_id))
        return invalidation_id
    except ClientError:
        print("ClientError raised when creating invalidation")
        raise


def get_invalidation_status(cf_client, distribution_id, invalidation_id):
    try:
        response = cf_client.get_invalidation(
            DistributionId=distribution_id,
            Id=invalidation_id
        )
        return response['Invalidation']['Status']
    except ClientError:
        print('ClientError raised when get invalidation status')
        raise


def cloudfront_invalidation(cf_client, distribution_id):
    invalidation_id = create_invalidation(cf_client, distribution_id)
    count = 0
    while count < 10:
        status = get_invalidation_status(cf_client, distribution_id, invalidation_id)
        if status == 'Completed':
            print("Completed cloudfront invalidation: {}".format(invalidation_id))
            sys.exit()
        count += 1
        time.sleep(30)
    raise RuntimeError('Timeout, please check cloudfront invalidation: {}'.format(invalidation_id))


if __name__ == '__main__':
    DISTRIBUTION_ID = sys.argv[1]
    CLOUD_FRONT = 'cloudfront'

    cf_client = boto3.client(CLOUD_FRONT)
    cloudfront_invalidation(cf_client, DISTRIBUTION_ID)
