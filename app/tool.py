from google.cloud import storage
import os
import json
from app.config import upload_configs

def upload_gcs_file(bucket_name, source_file_name, destination_file_name):
    credential_json = json.loads(os.environ['GCS_CREDENTIAL'])
    storage_client = storage.Client.from_service_account_info(credential_json)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_file_name)
    blob.cache_control = upload_configs['cache_control_short']
    blob.upload_from_filename(source_file_name)
    return True

def save_file(dest_filename, data):
    if data:
        dirname = os.path.dirname(dest_filename)
        if len(dirname)>0 and not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(dest_filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
        print(f'Store {dest_filename} successed')