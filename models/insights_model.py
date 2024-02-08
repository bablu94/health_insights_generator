from .test_results_parser import TestResultsParser

class InsightsModel:
    def __init__(self, test_results_file, reference_ranges_file):
        self.parser = TestResultsParser(test_results_file, reference_ranges_file)

    def generate_insights(self):
        insights = {}
        test_trends = self.parser.get_test_trends()

        for test_name, trend in test_trends.items():
            if trend == "increasing":
                insights[test_name] = f"The results for {test_name} are increasing, indicating a potential health risk."
            elif trend == "decreasing":
                insights[test_name] = f"The results for {test_name} are decreasing, indicating improvement."
            elif trend == "stable":
                insights[test_name] = f"The results for {test_name} are stable within the reference range."

        return insights
