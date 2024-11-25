def extract_costs(input_string):
    costs = []
    for line in input_string.split('\n'):
        if "Total Cost: $" in line:
            cost_str = line.split("Total Cost: $")[1].strip()
            try:
                cost = float(cost_str)
                costs.append(cost)
            except ValueError:
                continue
    return costs


def get_total_cost(input_string):
    costs = extract_costs(input_string)
    return sum(costs)


if __name__ == "__main__":
    input_str = """
    Input tokens: 356
Output tokens: 2
Total Cost: $0.00091
Image Cateegory: Clothing
PROMPT: Look at the attire of the individuals in the image. How do their garments, accessories, and styles represent the cultural identity and customs of their community?
Input tokens: 321
Output tokens: 165
Total Cost: $0.0024525
Input tokens: 490
Output tokens: 2
Total Cost: $0.001245
Results appended to analysis_results.csv
Input tokens: 1206
Output tokens: 1
Total Cost: $0.0030250000000000003
Image Cateegory: Greeting
PROMPT: Notice how people interact in the image. What forms of greeting or social gestures are displayed, and what do they reveal about the culture's communication styles and etiquette?
Input tokens: 1173
Output tokens: 121
Total Cost: $0.0041425
Input tokens: 1296
Output tokens: 3
Total Cost: $0.0032700000000000003
Results appended to analysis_results.csv
Input tokens: 866
Output tokens: 3
Total Cost: $0.0021950000000000003
Image Cateegory: Beverage
PROMPT: Detect any beverages or drinking customs depicted in the image. How do these elements reflect the cultural importance of certain drinks or rituals involved in their consumption?
Input tokens: 830
Output tokens: 181
Total Cost: $0.003885
Input tokens: 1016
Output tokens: 1
Total Cost: $0.0025499999999999997
Results appended to analysis_results.csv
Input tokens: 1206
Output tokens: 3
Total Cost: $0.0030450000000000004
Image Cateegory: Beverage
PROMPT: Detect any beverages or drinking customs depicted in the image. How do these elements reflect the cultural importance of certain drinks or rituals involved in their consumption?
Input tokens: 1170
Output tokens: 252
Total Cost: $0.005445
Input tokens: 1427
Output tokens: 1
Total Cost: $0.0035775000000000004
Results appended to analysis_results.csv
Input tokens: 526
Output tokens: 2
Total Cost: $0.001335
Image Cateegory: Clothing
PROMPT: Look at the attire of the individuals in the image. How do their garments, accessories, and styles represent the cultural identity and customs of their community?
Input tokens: 491
Output tokens: 120
Total Cost: $0.0024275
Input tokens: 615
Output tokens: 1
Total Cost: $0.0015475
Results appended to analysis_results.csv
Input tokens: 866
Output tokens: 2
Total Cost: $0.0021850000000000003
Image Cateegory: Clothing
PROMPT: Look at the attire of the individuals in the image. How do their garments, accessories, and styles represent the cultural identity and customs of their community?
Input tokens: 831
Output tokens: 113
Total Cost: $0.0032075
Input tokens: 948
Output tokens: 1
Total Cost: $0.0023799999999999997
Results appended to analysis_results.csv
Input tokens: 1206
Output tokens: 1
Total Cost: $0.0030250000000000003
Image Cateegory: Architecture
PROMPT: Analyze the architectural features present in the image. What do the design, materials, and style tell you about the culture's historical and aesthetic values?
Input tokens: 1170
Output tokens: 383
Total Cost: $0.006755000000000001
Input tokens: 1558
Output tokens: 2
Total Cost: $0.003915
Results appended to analysis_results.csv
Input tokens: 526
Output tokens: 1
Total Cost: $0.001325
Image Cateegory: Greeting
PROMPT: Notice how people interact in the image. What forms of greeting or social gestures are displayed, and what do they reveal about the culture's communication styles and etiquette?
Input tokens: 493
Output tokens: 114
Total Cost: $0.0023724999999999996
Input tokens: 609
Output tokens: 1
Total Cost: $0.0015325
Results appended to analysis_results.csv
Input tokens: 1206
Output tokens: 1
Total Cost: $0.0030250000000000003
Image Cateegory: Architecture
PROMPT: Analyze the architectural features present in the image. What do the design, materials, and style tell you about the culture's historical and aesthetic values?
Input tokens: 1170
Output tokens: 308
Total Cost: $0.006005
Input tokens: 1483
Output tokens: 4
Total Cost: $0.0037475
Results appended to analysis_results.csv
Input tokens: 866
Output tokens: 2
Total Cost: $0.0021850000000000003
Image Cateegory: Clothing
PROMPT: Look at the attire of the individuals in the image. How do their garments, accessories, and styles represent the cultural identity and customs of their community?
Input tokens: 831
Output tokens: 142
Total Cost: $0.0034974999999999997
Input tokens: 977
Output tokens: 1
Total Cost: $0.0024525000000000003
Results appended to analysis_results.csv
Input tokens: 1206
Output tokens: 1
Total Cost: $0.0030250000000000003
Image Cateegory: Garden
PROMPT: Examine any garden or natural elements in the image. How does landscaping, plant selection, or garden design convey aspects of the culture's relationship with nature?
Input tokens: 1172
Output tokens: 267
Total Cost: $0.0056
Input tokens: 1442
Output tokens: 3
Total Cost: $0.0036349999999999998
Results appended to analysis_results.csv
Input tokens: 866
Output tokens: 3
Total Cost: $0.0021950000000000003
Image Cateegory: Buddhist
PROMPT: Identify any Buddhist symbols, practices, or figures in the image. How do these elements illustrate the influence of Buddhism on the culture shown?
Input tokens: 828
Output tokens: 221
Total Cost: $0.00428
Input tokens: 1056
Output tokens: 3
Total Cost: $0.00267
Results appended to analysis_results.csv
Input tokens: 526
Output tokens: 1
Total Cost: $0.001325
Image Cateegory: Greeting
PROMPT: Notice how people interact in the image. What forms of greeting or social gestures are displayed, and what do they reveal about the culture's communication styles and etiquette?
Input tokens: 493
Output tokens: 115
Total Cost: $0.0023825
Input tokens: 610
Output tokens: 1
Total Cost: $0.001535
Results appended to analysis_results.csv
Input tokens: 1206
Output tokens: 1
Total Cost: $0.0030250000000000003
Image Cateegory: Food
PROMPT: Observe any food items or dining scenes in the image. What can you infer about the culture's culinary traditions and their significance in social or ceremonial contexts?
Input tokens: 1171
Output tokens: 198
Total Cost: $0.0049075
Input tokens: 1373
Output tokens: 3
Total Cost: $0.0034625000000000003
Results appended to analysis_results.csv
Input tokens: 356
Output tokens: 3
Total Cost: $0.0009199999999999999
Image Cateegory: Beverage
PROMPT: Detect any beverages or drinking customs depicted in the image. How do these elements reflect the cultural importance of certain drinks or rituals involved in their consumption?
Input tokens: 320
Output tokens: 213
Total Cost: $0.00293
Input tokens: 538
Output tokens: 2
Total Cost: $0.001365
Results appended to analysis_results.csv
Input tokens: 526
Output tokens: 1
Total Cost: $0.001325
Image Cateegory: Greeting
PROMPT: Notice how people interact in the image. What forms of greeting or social gestures are displayed, and what do they reveal about the culture's communication styles and etiquette?
Input tokens: 493
Output tokens: 154
Total Cost: $0.0027725
Input tokens: 649
Output tokens: 3
Total Cost: $0.0016524999999999999"""
    print(f"${get_total_cost(input_string=input_str)}")
