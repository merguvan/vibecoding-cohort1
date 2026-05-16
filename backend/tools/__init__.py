from backend.tools.text_insights import text_insights


TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "text_insights",
            "description": (
                "Verilen metin icin kelime sayisi, karakter sayisi, cumle sayisi "
                "ve tahmini okuma suresi dondurur."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Analiz edilecek metin",
                    },
                },
                "required": ["text"],
            },
        },
    },
]


TOOL_FUNCTIONS = {
    "text_insights": lambda args: text_insights(args.get("text", "")),
}
