from client import StatisticalAnomalyZscoreDetectorClient

def main():
    client = StatisticalAnomalyZscoreDetectorClient()
    res = client.detect_distribution_anomalies('api_latency_ms')
    print('Anomaly Z-Score Detector: ' + res['anomaly_detection_id'])
    print('Outliers Detected: ' + str(res['anomalies_detected_count']) + ' | Max Z-Score: ' + str(res['max_zscore_observed']))
    print('Report URL: ' + res['statistical_report_url'])

if __name__ == '__main__':
    main()
