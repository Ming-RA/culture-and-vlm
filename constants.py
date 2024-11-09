PROMPT1 = "Categorize the objects that are culturally relevant based on their function into these categories: ['Musical', 'Architecture', 'Clothing', 'Buddhist', 'Food', 'Greeting', 'Beverage', 'Garden', 'Utensils', 'Wedding', 'Tally'] Give a one word answer only!"

MODEL = "llava:13b"

CSV_FILENAME = "analysis_results.csv"

FIELDNAMES = ['Image URL', 'Prompt', 'Analysis Result', 'Status']

SYSTEM_PROMPT = "You are an expert in the intersectionality between image analysis and cultural analysis, providing insights that integrate visual elements with cultural contexts."
