from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

print(sentiment_pipeline("A look at the day ahead in U.S. and global markets from Mike Dolan\r\n A buoyant U.S. economy, hawkish Federal Reserve and dysfunctional Congress are sending Treasury bond yields soaring through 5% and… [+4415 chars]"))