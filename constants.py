PROMPT1 = "Carefully analyze this image and answer with which country/culture/civilization is most closely associated with this image. Make sure to incorporate multiple aspects into your analysis, such as - geographical features, postures and gestures, time period and other subtle details in the images background and foreground."

PROMPT2 = "Based on your choice of culture/country/civilization provide a list of 5 features in the image that most influenced your decision."

PROMPT3 = "Based on the features you analyzed in this image, provide a an appropriate time period that you believe the image depicts or originates from. Be as specific as possible when appropriate by including the date, year, decade or period. In cases where the time period is unclear, suggest possible intervals of time."

MODEL = "llava:13b"

CSV_FILENAME = "analysis_results.csv"

FIELDNAMES = ['Image URL', 'Prompt', 'Analysis Result', 'Status']
