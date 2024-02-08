from models.insights_model import InsightsModel

def main():
    insights_model = InsightsModel('data/test_results.csv', 'data/reference_ranges.csv')
    insights = insights_model.generate_insights()
    for test, insight in insights.items():
        print("Test: {}, Insight: {}".format(test, insight))

if __name__ == "__main__":
    main()
