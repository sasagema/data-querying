from typing import Any, Dict, List, Tuple
from sqlalchemy.orm import Query, Session, joinedload

def apply_filters(query: Query, filters: Dict[str, Any]) -> Query:
    """
    Dynamically apply filters to a SQLAlchemy query based on a dictionary of filters.
    """
    for attr, value in filters.items():
        if hasattr(query.column_descriptions[0]['entity'], attr) and value:
            query = query.filter(getattr(query.column_descriptions[0]['entity'], attr) == value)
   
    return query
