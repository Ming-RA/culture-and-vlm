PROMPT1 = "Categorize the objects that are culturally relevant based on their function into these categories: ['Musical', 'Architecture', 'Clothing', 'Buddhist', 'Food', 'Greeting', 'Beverage', 'Garden', 'Utensils', 'Wedding', 'Tally'] Give a one word answer only!"

PROMPT2 = "Given the image and the description given by the user, please give a one or two word answer to the question: What culture is this image from?"

MODEL = "llava:13b"

CSV_FILENAME = "gemini_analysis_results.csv"

FIELDNAMES = ['Image ID', 'Category', 'Analysis Result', 'Culture']

SYSTEM_PROMPT = "You are an expert in the intersectionality between image analysis and cultural analysis, providing insights that integrate visual elements with cultural contexts."

PROMPTS = {
    "Musical": "Examine the image for any musical instruments, performances, or symbols. How do these elements reflect the cultural heritage and musical traditions of the society depicted?",
    "Architecture": "Analyze the architectural features present in the image. What do the design, materials, and style tell you about the culture's historical and aesthetic values?",
    "Clothing": "Look at the attire of the individuals in the image. How do their garments, accessories, and styles represent the cultural identity and customs of their community?",
    "Buddhist": "Identify any Buddhist symbols, practices, or figures in the image. How do these elements illustrate the influence of Buddhism on the culture shown?",
    "Food": "Observe any food items or dining scenes in the image. What can you infer about the culture's culinary traditions and their significance in social or ceremonial contexts?",
    "Greeting": "Notice how people interact in the image. What forms of greeting or social gestures are displayed, and what do they reveal about the culture's communication styles and etiquette?",
    "Beverage": "Detect any beverages or drinking customs depicted in the image. How do these elements reflect the cultural importance of certain drinks or rituals involved in their consumption?",
    "Garden": "Examine any garden or natural elements in the image. How does landscaping, plant selection, or garden design convey aspects of the culture's relationship with nature?",
    "Utensils": "Observe any tools or utensils shown in the image. What do their design and usage tell you about the technological development and daily life in the culture?",
    "Wedding": "Identify any wedding scenes or symbols. How do the depicted rituals, attire, and ceremonies illustrate the culture's matrimonial traditions and values?",
    "Tally": "Look for any tallying methods or counting tools in the image. What do these elements indicate about the culture's numerical systems or record-keeping practices?"}
