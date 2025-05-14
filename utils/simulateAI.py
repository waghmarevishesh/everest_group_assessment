def generate_project_summary(data : str) -> dict:

    topics = ["data", "AI", "machine learning", "web", "CI/CD", "dashboard"]
    technologies = data['technologies'].split(',')

    main_topic = next((word for word in topics if word.lower() in data['description'].lower()), "general technology")
    used_techs = [tech for tech in technologies if tech.lower() in data['description'].lower()]


    return {
        "summary": (
            f"Based on the description, this project likely focuses on {main_topic}. "
            f"A generated summary emphasizes its potential impact on user experience "
            f"using technologies like {', '.join(used_techs) if used_techs else 'various tools'}."
        )
    }
