def evaluate_structure(struct_data):
    """
    Evaluates a material's structure based on input XRD data.
    Returns a dictionary with a score and basic insights.
    """

    try:
        data = struct_data.get("data", [])
        if not data:
            return {
                "score": 0,
                "insights": "No data provided.",
                "crystalline": False
            }

        total_intensity = sum(point["intensity"] for point in data)
        average_intensity = total_intensity / len(data)

        score = round(average_intensity, 2)

        if score > 300:
            insights = "Highly crystalline material detected."
        elif score > 150:
            insights = "Moderately crystalline structure."
        else:
            insights = "Amorphous or weakly crystalline material."

        return {
            "score": score,
            "insights": insights,
            "crystalline": score > 150
        }

    except Exception as e:
        return {
            "error": str(e),
            "score": 0,
            "insights": "Evaluation failed.",
            "crystalline": False
        }