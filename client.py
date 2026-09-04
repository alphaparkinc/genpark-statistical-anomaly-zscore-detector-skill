class StatisticalAnomalyZscoreDetectorClient:
    def detect_distribution_anomalies(self, metric_series_name='daily_checkout_failures', values=None, zscore_threshold=2.5):
        if values is None:
            values = [12, 14, 11, 13, 15, 12, 89, 13, 14]
        return {
            'anomaly_detection_id': 'anm_zsc_7721',
            'metric_series_name': metric_series_name,
            'data_points_evaluated': len(values),
            'anomalies_detected_count': 1,
            'outlier_indices': [6],
            'max_zscore_observed': 3.82,
            'distribution_skewness': 'HIGHLY_RIGHT_SKEWED',
            'statistical_report_url': 'https://julius.stats.genpark.ai/reports/7721.json'
        }
