import pandas as pd

class TestResultsParser:
    def __init__(self, test_results_file, reference_ranges_file):
        self.test_results_df = pd.read_csv(test_results_file)
        self.reference_ranges_df = pd.read_csv(reference_ranges_file)

    def get_test_trends(self):
        test_trends = {}
        for _, row in self.test_results_df.iterrows():
            test_name = row['TestName']
            result = row['Result']
            min_value, max_value = self.get_reference_range(test_name)
            if min_value is not None and max_value is not None:
                if result < min_value:
                    test_trends[test_name] = "decreasing"
                elif result > max_value:
                    test_trends[test_name] = "increasing"
                else:
                    test_trends[test_name] = "stable"
        return test_trends

    def get_reference_range(self, test_name):
        reference_range_row = self.reference_ranges_df[self.reference_ranges_df['TestName'] == test_name]
        if not reference_range_row.empty:
            return reference_range_row.iloc[0]['MinValue'], reference_range_row.iloc[0]['MaxValue']
        else:
            return None, None
