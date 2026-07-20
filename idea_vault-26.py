# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: IdeaVault
# --- Demo commands for quick manual testing of IdeaVault ---
def demo_run():
    """Create a sample idea, category, and connection to exercise the system."""
    from datetime import date
    now = date.today()
    
    # Create a category
    cat1 = Category(
        name="Technology", description="Tech-related ideas",
        created_by=Person("Alice"), created_on=now
    )
    cat2 = Category(
        name="Business", description="Business-related ideas",
        created_by=Person("Bob"), created_on=now
    )
    
    # Create a person (idea author)
    author = Person(name="Charlie")
    
    # Create an idea with connections and plan items
    idea1 = Idea(
        title="AI-powered search assistant", description="A search tool that uses AI to understand queries better.",
        created_by=author, created_on=now,
        status="Draft", score=4.5,
        category=cat1, tags=["AI", "Search"],
    )
    
    idea2 = Idea(
        title="E-commerce platform", description="An online store for selling handmade products.",
        created_by=author, created_on=now,
        status="Planning", score=3.8,
        category=cat2, tags=["E-commerce", "Handmade"],
    )
    
    # Add a connection between ideas
    idea1.add_connection(idea2, type="Inspires")
    
    # Add plan items to the first idea
    plan_item = PlanItem(
        title="Research AI models for search", description="Compare top AI search solutions", priority=1, status="Pending", due_on=now + timedelta(days=7)
    )
    idea1.add_plan_item(plan_item)
    
    # Print demo summary
    print(f"Demo: Created {cat1.name} and {cat2.name} categories")
    print(f"Idea 1: '{idea1.title}' (Score: {idea1.score})")
    print(f"Idea 2: '{idea2.title}' (Score: {idea2.score})")
    print(f"Connection: Idea 1 -> Idea 2 ({idea1.get_connection(idea2).type})")
    print(f"Plan item for Idea 1: {plan_item.title} (Priority: {plan_item.priority})")
    
demo_run()
