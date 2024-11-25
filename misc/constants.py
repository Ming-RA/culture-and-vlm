PROMPT1 = "Categorize the objects that are culturally relevant based on their function into these categories: ['Musical', 'Architecture', 'Clothing', 'Buddhist', 'Food', 'Greeting', 'Beverage', 'Garden', 'Utensils', 'Wedding', 'Tally'] Give a one word answer only!"

PROMPT2 = "Given the image and the description given by the user, please give a one or two word answer to the question: What culture is this image from?"

MODEL = "llava:13b"

CSV_FILENAME = "output_data/gpt-4o_bounding_boxes.csv"

FIELDNAMES = ['Image ID', 'Category', 'Bounding Boxes + Labels']

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

BOUNDING_BOX_PROMPTS = {
    "Musical": """In this {width}x{height} image, identify any musical instruments, performances, or symbols. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Architecture": """In this {width}x{height} image, locate the architectural features. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Clothing": """In this {width}x{height} image, identify the attire of individuals. For each garment or accessory, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Buddhist": """In this {width}x{height} image, find any Buddhist symbols, practices, or figures. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Food": """In this {width}x{height} image, detect any food items or dining scenes. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Greeting": """In this {width}x{height} image, identify forms of greeting or social gestures. For each gesture, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Beverage": """In this {width}x{height} image, locate any beverages or drinking customs depicted. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Garden": """In this {width}x{height} image, find any garden or natural elements. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Utensils": """In this {width}x{height} image, identify any tools or utensils shown. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Wedding": """In this {width}x{height} image, locate any wedding scenes or symbols. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner.""",
    "Tally": """In this {width}x{height} image, identify any tallying methods or counting tools. For each element, provide a JSON with bounding box coordinates where (x1,y1) is top-left corner and (x2,y2) is bottom-right corner."""}
