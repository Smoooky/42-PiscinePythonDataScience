FILEPATH = 'data.csv'
HAS_HEADER = True
NUM_OF_STEPS = 4

REPORT_TEMPLATE = """Report
We have made {} observations from tossing a coin:
{} of them were tails and {} of them were heads.
The probabilities are {:.2f}% and {:.2f}%, respectively.
Our forecast is that in the next {} observations we will have: {} tails and {} heads.\n"""