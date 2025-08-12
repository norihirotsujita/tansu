import json
from datetime import datetime, timezone, timedelta
 
def lambda_handler(event, context):
    # JSTの現在時刻を取得
    jst = timezone(timedelta(hours=9))  # UTC+9
    now = datetime.now(jst).strftime('%Y-%m-%d %H:%M:%S')
 
    response = {
        "message": f"Hello, world! Date: {now}"
    }
 
    # CloudWatch Logsに出力
    print("Lambda Response:", json.dumps(response))
 
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps(response)
    }
