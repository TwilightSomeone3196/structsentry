def generate_recommendations(decoded_data, language="english"):
    """
    Generates recommendations based on decoded XRD data.
    Output is localized based on selected language.
    """

    if not decoded_data:
        return ["No data provided."]

    avg_intensity = sum([p["intensity"] for p in decoded_data]) / len(decoded_data)
    recommendations = []

    if avg_intensity > 300:
        recommendations.append("Use high-temperature synthesis to maintain crystallinity.")
        recommendations.append("Consider doping to tune properties.")
    elif avg_intensity > 150:
        recommendations.append("Anneal sample to improve structural order.")
        recommendations.append("Re-run measurement at slower scan rate.")
    else:
        recommendations.append("Check sample purity and measurement settings.")
        recommendations.append("Consider different synthesis technique.")

    # Simple language translation (placeholder)
    if language == "urdu":
        recommendations = [f"[اردو] {r}" for r in recommendations]
    elif language == "french":
        recommendations = [f"[Français] {r}" for r in recommendations]
    elif language == "german":
        recommendations = [f"[Deutsch] {r}" for r in recommendations]

    return recommendations