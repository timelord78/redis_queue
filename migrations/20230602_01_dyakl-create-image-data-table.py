"""
create image_data table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """create table if not exists image_data (
            id serial primary key,
            size int not null,
            created_at timestamp default current_timestamp)
        """,
        """
            drop table if exists image_data
        """
    ),
]
